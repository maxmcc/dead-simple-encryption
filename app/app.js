var path = require('path');
var logger = require('morgan');
var express = require('express');
var bodyParser = require('body-parser')
var multer = require('multer'); 
// var cookieParser = require('cookie-parser');
// var session = require('cookie-session');
var app = express();

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 

app.use('/public/css', express.static(__dirname + '/public/css'));
app.use('/public/js', express.static(__dirname + '/public/js'));
app.use('/public/fonts', express.static(__dirname + '/public/fonts'));
app.use('/public/img', express.static(__dirname + '/public/img'));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hjs');
app.set('port', process.env.PORT || 3000);

app.use(logger('dev'));
// app.use(bodyParser.urlencoded({extended: false}));
// app.use(cookieParser());
// app.use(session({secret: 'codeweekend'}));
// app.use(express.static(path.join(__dirname, 'public')));

// Our own middleware which runs for every request
// app.use(function(req, res, next) {
//   if (req.session.message) {
//     res.locals.message = req.session.message;
//     req.session.message = null;
//   }

//   if (!req.session.notes) {
//     req.session.notes = [];
//   }

//   next();
// });

var routes = require('./routes');
app.use('/', routes);

// handle file uploads
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(multer());

app.post('/upload', function(req, res, next) {
    res.status(200).end();
});

app.post('/_upload', function(req, res) {
  console.log(req.body.files);
  var data = req.body.files;

  var PythonShell = require('python-shell');

  var options = {
    args: data
  };

  PythonShell.run('hello.py', options, function (err, results) {
    if (err) throw err;
    console.log('results: %j', results);
  });

    res.status(200).end();
  });

// If no routes activated by now, catch the 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// Handle any errors by rendering the error page
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    errorMessage: err.message,
    error: app.get('env') === 'development' ? err : {}
  });
});

// Start listening for requests
app.listen(app.get('port'), function() {
  console.log('Express server listening on port ' + app.get('port'));
});
