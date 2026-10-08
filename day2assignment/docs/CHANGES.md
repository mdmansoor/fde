# Invoice API changes

This document explains each change made to the invoice API, and why.

## Overview

The API stores invoices in `data/invoices.json` instead of in memory. Data now survives server restarts, and every route reads from and writes to the same file.

## Files

### `data/invoices.json` (new)

The data file. It holds a JSON array of invoices, seeded with the three original invoices (IDs 100, 101, 102). Each invoice has `invoice_id`, `amount`, `status`, and `company`.

### `src/day2assignment/store.py` (rewritten)

The storage layer shared by all routes. It replaces the in-memory Python lists.

- `DATA_FILE`: the path to `data/invoices.json`, computed from the location of `store.py`, so it works no matter which directory the server starts from.
- `read_invoices()`: returns the list from the file, or an empty list if the file doesn't exist yet.
- `write_invoices(invoices)`: saves the full list back to the file, creating the `data/` folder if needed.
- `next_invoice_id(invoices)`: returns the highest existing `invoice_id` plus one.

### `src/day2assignment/create_invoice.py`

`POST /createinvoice` now:

1. Reads the file.
2. Assigns `invoice_id` from `next_invoice_id` if the request didn't include one.
3. Appends the invoice and writes the file.

It returns the full list, as before.

### `src/day2assignment/get_invoices.py`

- `GET /invoices` returns the whole list from the file.
- `GET /invoices/{invoice_id}` returns one invoice, or the string `"None"` if it doesn't exist. This matches the original behavior.

### `src/day2assignment/delete_invoice.py`

`DELETE /deleteinvoice/{invoice_id}` reads the file, removes the matching invoice, and writes the file back. It returns `"deleted successfully"`, or `"None"` if no invoice matches.

### `src/day2assignment/update_invoice.py`

`PUT /updateinvoice/{invoice_id}` reads the file, updates only the fields sent in the request, and writes the file back. It returns the updated invoice. If the invoice doesn't exist, it returns a 404.

The request body is validated by `InvoiceUpdate` in `model.py`, which only accepts `amount` and `status`. Sending `company` or `invoice_id` returns a 422.

## Behavior changes to know about

- **IDs can be reused after deletion.** The next ID is the highest current ID plus one. If you delete the invoice with the highest ID, that ID will be assigned to the next new invoice. The earlier in-memory counter never reused IDs.
- **Nothing is validated on explicit IDs.** If a request sends an `invoice_id` that already exists, a duplicate is saved.
- **Each request reads and writes the whole file.** This is fine for a small assignment dataset, but it would not scale to large data.
- **No lock.** Two requests that arrive at the same moment can overwrite each other's changes. This was removed to keep the code simple; add a lock back if concurrent writes matter.

## Testing

Each route was tested against the file: list, get by ID, create with and without an ID, partial update, rejected fields, update of a missing invoice, delete, and a second delete. The test restored the original seed data afterward.
