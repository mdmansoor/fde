from fastapi import APIRouter

from .model import Invoice
from .store import next_invoice_id, read_invoices, write_invoices

router = APIRouter()


@router.post("/createinvoice")
def create_invoice(invoice: Invoice):
    invoices = read_invoices()
    if invoice.invoice_id is None:
        invoice.invoice_id = next_invoice_id(invoices)
    invoices.append(invoice.model_dump())
    write_invoices(invoices)
    return invoices
