from fastapi import APIRouter

from .store import read_invoices

router = APIRouter()


@router.get("/invoices")
def get_invoices():
    return read_invoices()


@router.get("/invoices/{invoice_id}")
def get_invoice_byid(invoice_id: int):
    invoices = read_invoices()
    for invoice in invoices:
        if invoice["invoice_id"] == invoice_id:
            return invoice

    return "None"
