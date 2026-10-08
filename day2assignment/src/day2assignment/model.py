from pydantic import BaseModel, ConfigDict


class Invoice(BaseModel):
    invoice_id: int | None = None
    amount: float
    status: str
    company: str


class InvoiceUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    amount: float | None = None
    status: str | None = None
