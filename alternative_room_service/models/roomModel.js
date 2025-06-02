let rooms = [];
let idCounter = 1;

function getAllRooms() {
    return rooms;
}

function getRoomById(id) {
    return rooms.find(room => room.id === id);
}

function createRoom(name) {
    const newRoom = { id: idCounter++, name };
    rooms.push(newRoom);
    return newRoom;
}

module.exports = { getAllRooms, getRoomById, createRoom };
