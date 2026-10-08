from fastapi import APIRouter, HTTPException

from .model import InvoiceUpdate
from .store import read_invoices, write_invoices

router = APIRouter()


@router.put("/updateinvoice/{invoice_id}")
def update_invoice(invoice_id: int, update: InvoiceUpdate):
    invoices = read_invoices()
    for invoice in invoices:
        if invoice["invoice_id"] == invoice_id:
            invoice.update(update.model_dump(exclude_unset=True))
            write_invoices(invoices)
            return invoice

    raise HTTPException(status_code=404, detail="Invoice not found")
