const express = require('express');
const { getCropsByEcozone } = require('../controllers/cropController');
const router = express.Router();

router.get('/:ecozone', getCropsByEcozone);

module.exports = router;
