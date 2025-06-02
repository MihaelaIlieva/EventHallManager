const express = require('express');
const router = express.Router();
const controller = require('../controllers/roomController');

router.get('/', controller.getRooms);
router.get('/:id', controller.getRoom);
router.post('/', controller.createRoom);

module.exports = router;
