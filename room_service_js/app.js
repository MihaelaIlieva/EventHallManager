const express = require('express');
const bodyParser = require('body-parser');
const sequelize = require('./config');
const Room = require('./models/Room');
const roomRoutes = require('./routes/roomRoutes');

const app = express();
app.use(bodyParser.json());
app.use('/room', roomRoutes);
app.use('/rooms', roomRoutes);

(async () => {
  try {
    await sequelize.sync();
    app.listen(5003, () => console.log('Room service running on port 5003'));
  } catch (err) {
    console.error('Failed to start app:', err);
  }
})();
