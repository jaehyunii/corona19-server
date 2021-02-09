var express = require('express');
var router = express.Router();

/* GET all location */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* GET all location of specific district */
router.get('/:districtName', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
