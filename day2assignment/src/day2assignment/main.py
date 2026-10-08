from fastapi import FastAPI
from src.day2assignment.create_invoice import router as create_invoice
from src.day2assignment.get_invoices import router as get_invoices
from src.day2assignment.delete_invoice import router as delete_invoice
from src.day2assignment.update_invoice import router as update_invoice

app = FastAPI()

app.include_router(create_invoice)
app.include_router(get_invoices)
app.include_router(update_invoice)
app.include_router(delete_invoice)
