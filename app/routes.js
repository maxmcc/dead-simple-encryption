var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {
  return res.render('index');
});

/*router.get('/upload', function(req, res) {
  return;
});*/

module.exports = router;
