import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "invoices.json"


def read_invoices() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text())


def write_invoices(invoices: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(invoices, indent=4))


def next_invoice_id(invoices: list[dict]) -> int:
    return max((invoice["invoice_id"] for invoice in invoices), default=0) + 1
