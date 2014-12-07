var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {

var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  args: ['value1', 'value2', 'value3']
};

PythonShell.run('hello.py', function (err, results) {
  if (err) throw err;
  console.log('results: %j', results);
});

  return res.render('index');
});

module.exports = router;
