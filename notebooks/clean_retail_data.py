

from pathlib import Path
import pandas as pd

# Find the project folder
project_dir = Path(__file__).resolve().parent.parent
data_dir = project_dir / "data"


file_path = data_dir / "online_retail_II.xlsx"

# Load one year of transactions
df = pd.read_excel(
    file_path,
    sheet_name="Year 2010-2011"
)

# Display original dataset information
print("Original rows:", len(df))
print("\nMissing values:")
print(df.isnull().sum())

# Rename columns
df.columns = [
    "Invoice", "StockCode", "Description",
    "Quantity", "InvoiceDate", "Price",
    "CustomerID", "Country"
]

# Remove rows with missing essential values
df = df.dropna(subset=[
    "Invoice", "StockCode", "InvoiceDate",
    "Quantity", "Price"
])

# Convert data types
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)

df["Price"] = pd.to_numeric(
    df["Price"], errors="coerce"
)

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)

# Remove invalid numeric or date values
df = df.dropna(subset=[
    "Quantity", "Price", "InvoiceDate"
])

# Identify canceled invoices
df["IsCancelled"] = (
    df["Invoice"].astype(str).str.startswith("C")
)

# Separate valid sales from returns/cancellations
sales = df[
    (df["Quantity"] > 0) &
    (df["Price"] > 0) &
    (~df["IsCancelled"])
].copy()

# Add revenue
sales["Revenue"] = (
    sales["Quantity"] * sales["Price"]
).round(2)

# Create monthly reporting field
sales["YearMonth"] = (
    sales["InvoiceDate"].dt.strftime("%Y-%m")
)

# Export for SQLite and Power BI
output = data_dir / "retail_sales_clean.csv"
sales.to_csv(output, index=False)

print("\nOriginal rows:", len(df))
print("Valid sales rows:", len(sales))
print("Total sales revenue:", round(sales["Revenue"].sum(), 2))
print("Saved to:", output)
