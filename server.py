#!/usr/bin/env python3
"""Simple AI router endpoint for restaurant owner questions."""

from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Dict

HOST = "0.0.0.0"
PORT = 8000

DOMAIN_KEYWORDS = {
    "inventory": [
        "inventory",
        "stock",
        "supplier",
        "purchase order",
        "ingredient",
        "waste",
        "shrinkage",
        "reorder",
    ],
    "scheduling": [
        "schedule",
        "shift",
        "staffing",
        "availability",
        "coverage",
        "time off",
        "rota",
    ],
    "payroll": [
        "payroll",
        "wage",
        "salary",
        "overtime",
        "timesheet",
        "tip",
        "tax",
    ],
    "reservations": [
        "reservation",
        "booking",
        "table",
        "guest",
        "waitlist",
        "seat",
        "party",
    ],
    "marketing": [
        "marketing",
        "campaign",
        "promotion",
        "social",
        "email",
        "loyalty",
        "ad",
        "discount",
    ],
}


def choose_module(question: str) -> str:
    lowered_question = question.lower()
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(keyword in lowered_question for keyword in keywords):
            return domain
    return "marketing"


class AIRouterHandler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, payload: Dict[str, str]) -> None:
        response_body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()
        self.wfile.write(response_body)

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/ask":
            self._send_json(
                HTTPStatus.NOT_FOUND,
                {"error": "Not found. Use POST /ask."},
            )
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        if content_length <= 0:
            self._send_json(
                HTTPStatus.BAD_REQUEST,
                {"error": "Request body is required."},
            )
            return

        try:
            body = self.rfile.read(content_length)
            payload = json.loads(body)
        except json.JSONDecodeError:
            self._send_json(
                HTTPStatus.BAD_REQUEST,
                {"error": "Invalid JSON payload."},
            )
            return

        question = payload.get("question")
        if not isinstance(question, str) or not question.strip():
            self._send_json(
                HTTPStatus.BAD_REQUEST,
                {"error": "'question' must be a non-empty string."},
            )
            return

        selected_module = choose_module(question)
        self._send_json(
            HTTPStatus.OK,
            {
                "module": selected_module,
                "response": f"Placeholder: route this question to the '{selected_module}' module.",
            },
        )


def run() -> None:
    server = ThreadingHTTPServer((HOST, PORT), AIRouterHandler)
    print(f"AI router listening on http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()
