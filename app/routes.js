var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {



  return res.render('index');
});

router.get('/index', function(req, res) {
    return res.render('index');
});

/*router.get('/upload', function(req, res) {
  return;
});*/



router.get('/test', function(req, res) {
    return res.render('test');
});

module.exports = router;
