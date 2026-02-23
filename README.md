# restaurant-ai-agent

AI-powered restaurant operations assistant for calls, reservations, inventory, payroll, scheduling, and marketing automation.

## AI Router Endpoint

This project now includes a simple AI routing endpoint that classifies a restaurant owner's natural-language question into one of these modules:

- `inventory`
- `scheduling`
- `payroll`
- `reservations`
- `marketing`

### Run the server

```bash
python3 server.py
```

The server listens on `http://localhost:8000`.

### Call `POST /ask`

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"Can you help me fill weekend shifts?"}'
```

Example response:

```json
{
  "module": "scheduling",
  "response": "Placeholder: route this question to the 'scheduling' module."
}
```

> Note: This is a placeholder router only (no OpenAI integration yet).
