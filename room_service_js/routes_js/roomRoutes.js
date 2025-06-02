const express = require('express');
const router = express.Router();
const Room = require('../models/Room');

router.get('/', async (req, res) => {
  const rooms = await Room.findAll();
  res.json(rooms);
});

router.post('/', async (req, res) => {
  const { name, capacity } = req.body;
  const exists = await Room.findOne({ where: { name } });
  if (exists) return res.status(400).json({ message: 'Room already exists' });

  await Room.create({ name, capacity });
  res.status(201).json({ message: 'Room created successfully' });
});

router.get('/:id', async (req, res) => {
  const room = await Room.findByPk(req.params.id);
  if (!room) return res.status(404).json({ message: 'Room not found' });
  res.json(room);
});

router.put('/:id', async (req, res) => {
  const { name, capacity } = req.body;
  const room = await Room.findByPk(req.params.id);
  if (!room) return res.status(404).json({ message: 'Room not found' });

  room.name = name;
  room.capacity = capacity;
  await room.save();
  res.json({ message: 'Room updated successfully' });
});

router.delete('/:id', async (req, res) => {
  const room = await Room.findByPk(req.params.id);
  if (!room) return res.status(404).json({ message: 'Room not found' });

  await room.destroy();
  res.json({ message: 'Room deleted successfully' });
});

module.exports = router;
