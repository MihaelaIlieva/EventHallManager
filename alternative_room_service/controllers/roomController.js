const model = require('../models/roomModel');

function getRooms(req, res) {
    res.json(model.getAllRooms());
}

function getRoom(req, res) {
    const id = parseInt(req.params.id);
    const room = model.getRoomById(id);
    if (!room) return res.status(404).json({ error: 'Room not found' });
    res.json(room);
}

function createRoom(req, res) {
    const { name } = req.body;
    if (!name) return res.status(400).json({ error: 'Name is required' });
    const newRoom = model.createRoom(name);
    res.status(201).json(newRoom);
}

module.exports = { getRooms, getRoom, createRoom };
