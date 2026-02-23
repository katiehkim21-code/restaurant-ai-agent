# restaurant-ai-agent

Minimal Express backend scaffold for a restaurant AI agent.

## Requirements

- Node.js 18+
- npm

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```
2. Create your environment file:
   ```bash
   cp .env.example .env
   ```
3. Start the server:
   ```bash
   npm start
   ```

For development with file watching:

```bash
npm run dev
```

## Environment variables

- `PORT`: Server port (default: `3000`)

## API endpoints

- `GET /` — basic service message
- `GET /health` — health check endpoint

### Example health response

```json
{
  "status": "ok",
  "service": "restaurant-ai-agent",
  "timestamp": "2026-01-01T00:00:00.000Z"
}
```
