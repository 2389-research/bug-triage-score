# shopq

Order queue for the warehouse kiosk. One kiosk, one nightly export job.

## How it is used today

- Staff enter orders on the kiosk. Quantity comes from a dropdown of whole numbers 1-10.
- The kiosk stamps every order with `created_at` (a `datetime`) before calling `store.save_orders`.
- Catalog prices are whole dollars plus .00, .49 or .99. Nothing is priced in fractions of a cent.
- The nightly export writes `export.csv` for about 40 customers. Customer names come from the CRM;
  three of them contain commas today ("Acme, Inc.", "Bolt, Nut & Co.", "Rivera, LLC").
- `retry.call_with_retry` wraps the label printer. The printer times out a few times a month.
