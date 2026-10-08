from fastapi import APIRouter

from .store import read_invoices, write_invoices

router = APIRouter()


@router.delete("/deleteinvoice/{invoice_id}")
def delete_invoice(invoice_id: int):
    invoices = read_invoices()
    for invoice in invoices:
        if invoice["invoice_id"] == invoice_id:
            invoices.remove(invoice)
            write_invoices(invoices)
            return "deleted successfully"

    return "None"
