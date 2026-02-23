const express = require('express');

const router = express.Router();

router.get('/', (_req, res) => {
  res.status(200).json({
    status: 'ok',
    service: 'restaurant-ai-agent',
    timestamp: new Date().toISOString()
  });
});

module.exports = router;
