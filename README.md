# restaurant-ai-agent

Backend-first AI platform for restaurant operations, designed with modular domains for faster iteration and long-term maintainability.

## Tech Stack

- **Python**
- **FastAPI**
- **SQLite** (MVP persistence target)

## Project Structure

```text
restaurant-ai-agent/
├── app/
│   ├── core/
│   │   └── config.py
│   ├── modules/
│   │   ├── reservations/
│   │   │   └── router.py
│   │   ├── inventory/
│   │   │   └── router.py
│   │   ├── payroll/
│   │   │   └── router.py
│   │   ├── scheduling/
│   │   │   └── router.py
│   │   └── marketing/
│   │       └── router.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Module Design (MVP placeholders)

Each module currently exposes a placeholder router with a `/health` endpoint:

- `/reservations/health`
- `/inventory/health`
- `/payroll/health`
- `/scheduling/health`
- `/marketing/health`

This keeps initial contracts explicit while business logic is implemented incrementally.

## Running the API

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the API:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Open docs:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Architecture Notes

- **Domain modules first:** reservations, inventory, payroll, scheduling, and marketing are independent units wired through FastAPI routers.
- **Shared core layer:** `app/core` is reserved for cross-cutting concerns such as settings, logging, DB session management, and auth.
- **Scalable API composition:** `app/main.py` is kept thin and focused on application assembly.

## Next Steps

1. Add SQLite integration (SQLAlchemy models + migrations).
2. Define request/response schemas per module.
3. Add service layer and repository abstractions in each domain.
4. Introduce authentication/authorization for internal staff roles.
5. Add background jobs for AI/automation workflows (notifications, campaign tasks, forecasting).
6. Add test coverage (unit + API integration tests).
