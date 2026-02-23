require('dotenv').config();

const express = require('express');
const healthRouter = require('./routes/health');

const app = express();
const port = Number(process.env.PORT) || 3000;

app.use(express.json());
app.use('/health', healthRouter);

app.get('/', (_req, res) => {
  res.json({ message: 'Restaurant AI Agent backend is running.' });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
