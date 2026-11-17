# ledgerly

Bookkeeping service for one 30-person company. It runs on a small box in the office.

## How it is used today

- The web server listens on the office LAN. Staff laptops reach it, and so does the guest Wi-Fi,
  which shares the LAN with visitors and contractors.
- `/download?name=...` serves invoice PDFs from `invoices/`. The UI links to names like `INV-0042.pdf`.
- The accountant runs the monthly report on the 1st. The office is in America/Chicago; the server
  clock and stored timestamps are UTC. About 600 transactions a month; about 20 of them land in
  the last six hours of a month, Chicago time.
- Invoices are created only through the UI, which requires at least one line item.
- Categories come from a fixed dropdown: `rent`, `payroll`, `supplies`, `travel`.
- `python -m ledgerly.cli --help` is run by the accountant maybe twice a year.
