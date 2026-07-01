# Data dictionary: data/clean/clean_online_retail.csv

The cleaned sales file has 522,504 rows and 11 columns. Each row is one product line on a completed (non-cancelled) invoice. Here is what each column means.

| Column | Type | Meaning | Units or values |
|--------|------|---------|-----------------|
| invoice_no | int64 | Invoice (order) number. Cancellations were removed, so every value is numeric. | integer; one invoice covers several rows |
| stock_code | text | Product code. Every code that is left matches a five-digit pattern, sometimes with a letter (for example 85123A). | code string |
| description | text | Product description, cleaned up by trimming spaces and putting it in title case. | text |
| quantity | int64 | Units sold on this line. Always above zero in the clean data. | count |
| invoice_date | text | Invoice timestamp in the original M/D/YYYY H:MM format. The notebook parses it to a datetime for the time-series work. | timestamp text |
| unit_price | float64 | Price per unit. Always above zero in the clean data. | GBP |
| customer_id | float64 | Customer number. Empty for about 25% of rows (guest or unscanned sales). | numeric id, can be empty |
| country | text | Destination country, with the labels standardised (for example EIRE became Ireland). Unspecified was set to empty. | country name |
| has_customer | bool | True if the row has a customer_id, otherwise False. Use it to filter down to identified customers. | True or False |
| revenue | float64 | Line revenue, quantity times unit_price. | GBP |
| region | text | Sales region from the country lookup. Countries with no match are labelled Other. | UK&IE, Western Europe, APAC, North America, Middle East, South America, Africa, Other |

A few notes:

- Total revenue across the file is £10,246,820.87.
- customer_id is a float rather than an integer because the missing IDs are stored as empty values. Filter on has_customer (or on customer_id not being empty) for customer-level work.
- This file leaves out cancellations, returns, non-product lines, zero or negative prices and quantities, blank descriptions and exact duplicates. See cleaning_decisions_log.md for the details.
