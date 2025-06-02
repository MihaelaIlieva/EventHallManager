const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const roomRoutes = require('./routes/roomRoutes');

const app = express();
const PORT = 5003;

app.use(cors());
app.use(bodyParser.json());

app.use('/room', roomRoutes);

app.listen(PORT, () => {
    console.log(`Room service listening on http://localhost:${PORT}`);
});
