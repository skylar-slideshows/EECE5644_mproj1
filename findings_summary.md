# Findings summary

These are the answers to the seven business questions for Cobblestone Gifts, covering December 2010 to December 2011. Every number here comes from running notebooks/cleaning_online_retail.ipynb on the cleaned sales data (522,504 lines). Customer-level numbers only use the roughly 75% of sales that have a customer ID, and I point that out where it matters.

## 1. Seasonality

Total revenue for the year was about £10.25 million. Sales build up through the autumn and peak in November 2011 at £1.45 million, which is around 84% above the average month of £0.79 million. The business is clearly seasonal and the run-up to Christmas is the most important period, so stock, staffing and marketing should be weighted toward September through November.

![Monthly revenue trend](monthly_revenue_trend.png)

## 2. Best sellers

The top product by revenue is the Regency Cakestand 3 Tier at about £174k. The top product by units sold is Paper Craft, Little Birdie at about 81k units. Only 6 of the 10 names show up on both lists. That gap is really a pricing story: some products make their money from a higher price (cake stands, bunting) and others from selling in huge volume at a low price (popcorn holders, cake cases). Both matter, and they should be managed separately.

![Top 10 products by revenue](top_products_revenue.png)

## 3. Markets

Outside the UK, the biggest countries by revenue are the Netherlands (£284k), Ireland (£271k), Germany (£205k), France (£184k) and Australia (£138k). By number of separate customers the leaders are Germany (94), France (87) and Spain (30). Grouped into regions, Western Europe brings in about £1.03 million, far ahead of any other non-UK region, with APAC next at £194k. If we want to expand, Western Europe is the obvious place to focus, and Germany and France stand out because they pair strong revenue with the widest customer base.

![Top non-UK markets by revenue](top_markets.png)

## 4. Customer concentration

Out of 4,334 identified customers, the top 1% (44 customers) bring in about 32% of identified revenue. The largest single account (customer 14646) spent £279k, and the biggest accounts tend to buy in large, repeated orders. This looks like a business that leans on wholesale buyers sitting on top of a long tail of smaller retail customers, which is a concentration risk worth keeping an eye on.

## 5. Order value

The average order, measured as revenue per invoice, is about £518. UK orders average £487 and non-UK orders average £813, so overseas orders are roughly two-thirds larger. That fits with the idea that a lot of the overseas demand is wholesale.

## 6. Returns and cancellations

Returns and cancellations come to 10,624 lines, which is about 2% of all the raw rows. In money terms they are around £0.90 million, or about 8.8% of gross sales value, so they matter more by value than by count. They cluster in a few high-value products and a handful of bulk accounts, so a focused look at the top returned products and customers would cover most of the value.

## 7. Data-quality memo

Out of 541,909 raw rows we kept 522,504 (96.4%) as trustworthy completed sales and removed 19,405 (3.6%). The rows we removed were cancellations (9,288), quantities of zero or less (10,624), prices of zero or less (2,517), non-product lines such as postage and bank charges (about 3,000), blank descriptions (1,454) and exact duplicate rows (5,221). Those groups overlap, so they add up to more than the net figure of 19,405. On top of that, 135,080 rows (24.9%) have no customer ID. We kept those as real sales but left them out of the customer-level questions. So the data is fine to trust for revenue, product, market and seasonality reporting. For anything at the customer level it should carry a note that about a quarter of sales cannot be tied to a customer.

See cleaning_decisions_log.md for the specific cleaning choices and data_dictionary.md for the columns in the cleaned file.
