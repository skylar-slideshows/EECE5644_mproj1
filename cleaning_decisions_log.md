# Cleaning decisions log

This is a list of the choices I made while turning the raw export into the cleaned sales file, with the reason for each one and how many rows it affected. The raw frame (df_raw) is never changed. All the cleaning creates new objects, and I never use inplace=True.

Starting point: df_raw has 541,909 rows and 8 columns.
Ending point: df_sales has 522,504 rows and 11 columns, which is 96.4% of the raw rows.

1. Keep the raw data untouched. I loaded the file into df_raw with encoding="ISO-8859-1" and did all the work on copies. The file is Latin-1, so it breaks on the £ sign if you read it as UTF-8.

2. Standardise country names. I changed EIRE to Ireland, RSA to South Africa, and Unspecified to missing, using replace. The same country under two labels would otherwise split its revenue, and Unspecified is not a real place.

3. Missing customer_id (135,080 rows, about 25%). I kept these rows in the sales data and added a has_customer flag, then built df_identified (391,150 rows) for the customer-level questions. A sale with no loyalty ID is still a real sale, so it should count for revenue. Only the questions about customers need an actual ID.

4. Blank description (1,454 rows). I dropped these with dropna. They mostly line up with the zero-price adjustment rows we remove anyway, so there was nothing worth keeping.

5. Dropped the helper column line_id. It was only used for the loc and iloc examples and is not needed later.

6. Cancellations (9,288 rows). I removed rows where invoice_no starts with C, but saved them first as df_returns for Question 6. A cancelled order is not a completed sale.

7. Non-product lines (about 2,980 rows). I kept only stock codes that match a five-digit pattern, optionally with a letter on the end. That drops POST, DOT, M, BANK CHARGES, AMAZONFEE, C2, PADS, D and similar codes, which are postage, fees and manual adjustments rather than products.

8. Impossible quantities (10,624 rows). I removed rows with a quantity of zero or less, since those are returns or adjustments, not sales.

9. Impossible prices (2,517 rows). I removed rows with a unit price of zero or less, because a real sale cannot have one.

10. Exact duplicates (5,221 rows). I found them with duplicated().sum() and removed them with drop_duplicates, since identical repeated lines double-count revenue.

11. Added columns for the analysis: revenue (quantity times unit price), a tidied title-case description, and a region column from a left join on the country lookup (any country with no match becomes Other).

Net rows removed: 541,909 minus 522,504 is 19,405, or 3.6% of the raw rows. The per-step counts above overlap (a cancelled line usually also has a negative quantity), which is why they add up to more than the net figure.

Assumptions worth knowing:

- Rows without a customer_id are treated as real sales and kept for the revenue, product and time questions, but left out of the customer questions. That means about a quarter of sales cannot be attributed to a customer.
- Products are identified by the five-digit stock code pattern rather than a fixed list of service codes, which is more robust.
- For Question 6, returns and cancellations are any cancelled invoice or any negative-quantity line, which comes to 10,624 lines.
- invoice_date is kept as the original text timestamp in the export and parsed to a datetime inside the notebook for the time-series part.
