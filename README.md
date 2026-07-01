# Cobblestone Gifts: Online Retail cleaning and analysis

This project profiles and cleans the UK Online Retail dataset (about 542k order lines from December 2010 to December 2011) for a made-up UK gift retailer called Cobblestone Gifts. It takes one raw order-system export, cleans it into a trustworthy set of completed sales, and uses that to answer seven business questions for a non-technical Head of Commercial.

The notebook works through 21 labelled pandas techniques (3.1 to 3.21) across five phases: load and profile, select and filter, clean and fix, engineer and summarise, and combine. It keeps the raw data unchanged and never uses inplace=True.

## What is in here

All files sit at the top level of the repo.

```
cleaning_online_retail.ipynb   the main notebook (all 21 techniques)
clean_online_retail.csv        cleaned sales data (522,504 rows)
data.csv                       raw export (not committed, see below)
findings_summary.md            the seven questions answered
cleaning_decisions_log.md      the cleaning choices and row counts
data_dictionary.md             columns in the cleaned file
requirements.txt               pinned package versions
monthly_revenue_trend.png      chart used in the findings
top_markets.png                chart used in the findings
top_products_revenue.png       chart used in the findings
```

## Getting the data

The raw dataset is not committed because it is large and git-ignored. It is the Kaggle dataset carrie1/ecommerce-data, a single data.csv (about 45 MB, 541,909 rows). The file is Latin-1 encoded, so it has to be read with encoding="ISO-8859-1".

From the website: download it from https://www.kaggle.com/datasets/carrie1/ecommerce-data, unzip it, and put data.csv in the project folder, next to the notebook.

With kagglehub (the notebook falls back to this on its own):

```python
import kagglehub, shutil, os
p = kagglehub.dataset_download("carrie1/ecommerce-data")
shutil.copy(os.path.join(p, "data.csv"), "data.csv")
```

With the Kaggle CLI (needs a ~/.kaggle/kaggle.json token):

```bash
kaggle datasets download -d carrie1/ecommerce-data -p . --unzip
```

If data.csv is already in the folder the notebook just uses it. Otherwise it downloads it with kagglehub, so a fresh clone still runs from top to bottom.

## Setup and run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name cobblestone --display-name "Cobblestone (.venv)"

jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.kernel_name=cobblestone \
  cleaning_online_retail.ipynb
```

Or just open the notebook in Jupyter and run everything from the top.

## Main findings

- Revenue for the year was about £10.25 million and it is very seasonal. November 2011 was roughly 84% above the average month, which points to a Christmas-driven business.
- The revenue leaders and the volume leaders are not the same list (only 6 of 10 overlap). Some products earn on price, like the Regency Cakestand 3 Tier at £174k, and others earn on volume.
- Outside the UK, Western Europe brings in the most money, with the Netherlands, Ireland, Germany and France in front. Germany and France also have the most customers.
- The business leans wholesale. The top 1% of customers (44 of 4,334) bring in about 32% of identified revenue, and non-UK orders (£813 on average) are about two-thirds bigger than UK orders (£487).
- We kept 96.4% of the raw rows as clean sales. Returns and cancellations are small by count (2%) but bigger by value (about 8.8%), and about a quarter of sales have no customer ID, which is fine for revenue reporting but worth a note for anything at the customer level.
