var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {

// var PythonShell = require('python-shell');

// var options = {
//   mode: 'text',
//   args: ['value1', 'value2', 'value3']
// };

// PythonShell.run('hello.py', function (err, results) {
//   if (err) throw err;
//   console.log('results: %j', results);
// });

  return res.render('index');
});

router.get('/index', function(req, res) {
    return res.render('index');
});

/*router.get('/upload', function(req, res) {
  return;
});*/

router.get('/_upload', function(req, res) {
  var data = req.params.data
  console.log(data);
  return 'Thanks!';
});

router.get('/test', function(req, res) {
    return res.render('test');
});

module.exports = router;
