import os
import pandas as pd
from sqlalchemy import create_engine, inspect
import logging
import time

# ------------------------------
# 1️⃣ Setup custom logger to file only
# ------------------------------
if not os.path.exists('logs_new'):
    os.makedirs('logs_new')

logger = logging.getLogger("ingestion_logger")
logger.setLevel(logging.INFO)
logger.propagate = False

# Remove any existing handlers
if logger.hasHandlers():
    logger.handlers.clear()

# ❌ FIX 1: Wrong folder path in FileHandler
# It should match the folder created above ('logs_new'), not 'logs'
file_handler = logging.FileHandler("logs_new/ingest_db.log", mode='a')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# ------------------------------
# 2️⃣ Connect to MySQL database
# ------------------------------
# ✅ FIX 2: Use correct connection string and password encoding
engine = create_engine("mysql+pymysql://root:Malkhed%40123@localhost/datana")

# ------------------------------
# 3️⃣ Function to ingest data
# ------------------------------
def ingest_db(df, table_name, engine):
    inspector = inspect(engine)
    if table_name in inspector.get_table_names():
        pass
    else:
        df.to_sql(table_name, con=engine, if_exists='fail', index=False)
        logger.info(f"Table '{table_name}' created and data inserted.")

# ------------------------------
# 4️⃣ Load all CSVs from data folder
# ------------------------------
def load_data():
    start = time.time()
    data_folder = 'data'
    if not os.path.exists(data_folder):
        logger.error(f"Data folder '{data_folder}' does not exist!")
        return
    for file in os.listdir(data_folder):
        if file.endswith('.csv'):
            file_path = os.path.join(data_folder, file)
            try:
                df = pd.read_csv(file_path)
                logger.info(f"Ingesting '{file}' into database...")
                ingest_db(df, file[:-4], engine)
            except Exception as e:
                logger.error(f"Error processing '{file}': {e}")
    
    end = time.time()
    total = (end - start) / 60
    logger.info('---------Ingestion complete--------------')
    logger.info(f'Total time taken: {total:.2f} minutes')

# ------------------------------
# 5️⃣ Run the ingestion
# ------------------------------
if __name__ == '__main__':
    load_data()









import os
import pandas as pd
from sqlalchemy import create_engine
import logging
import time

# ------------------------------
# Setup logger
# ------------------------------
def setup_logger(name, log_file):
    os.makedirs('logs_new', exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.FileHandler(log_file, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = setup_logger("vendor_summary_logger", "logs_new/vendor_sumary.log")

# ------------------------------
# Database connection
# ------------------------------
engine = create_engine("mysql+pymysql://root:Malkhed%40123@localhost/datana")


# ------------------------------
# Function: Fetch vendor sales summary
# ------------------------------
def fetch_vendor_sales_summary():
    """Runs SQL query and returns vendor summary DataFrame."""
    logger.info("Starting vendor sales summary extraction...")
    start_time = time.time()

    query = """
    WITH FreightSummary AS (
        SELECT 
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),
    PurchaseSummary AS (
        SELECT 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Volume,
            pp.Price AS ActualPrice,
            SUM(p.Quantity) AS totalQuantity,
            SUM(p.Dollars) AS totalPPrice
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY 
            p.VendorNumber, p.VendorName, p.Brand, 
            p.Description, p.PurchasePrice, pp.Volume, pp.Price
    ),
    SalesSummary AS (
        SELECT 
            VendorNo,
            Brand,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )
    SELECT 
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.PurchasePrice,
        ps.Volume,
        ss.TotalSalesPrice,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalExciseTax,
        ps.totalQuantity,
        ps.totalPPrice,
        fs.FreightCost,
        ps.ActualPrice,
        ps.Description
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ss.TotalSalesDollars DESC;
    """

    try:
        df = pd.read_sql(query, engine)
        logger.info(f" Query executed successfully. Rows fetched: {len(df)}")
    except Exception as e:
        logger.error(f" Error executing vendor summary query: {e}")
        df = pd.DataFrame()

    elapsed = time.time() - start_time
    logger.info(f"Vendor summary extraction completed in {elapsed:.2f} seconds.")
    return df


# ------------------------------
# Function: Clean data
# ------------------------------
def clean_data(df):
    """Performs missing value & duplicate checks, logs summary, returns cleaned DataFrame."""
    logger.info(" Starting data cleaning...")

    if df.empty:
        logger.warning("DataFrame is empty — skipping cleaning.")
        return df

    # Missing values
    missing = df.isnull().sum()
    missing_cols = missing[missing > 0]
    if not missing_cols.empty:
        logger.warning(f" Missing values found in columns: {list(missing_cols.index)}")
    else:
        logger.info(" No missing values found.")

    # Duplicates
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        logger.warning(f" Found {duplicate_count} duplicate rows. Removing them.")
        df = df.drop_duplicates()
        logger.info(" Duplicates removed.")
    else:
        logger.info(" No duplicate rows found.")

    logger.info(f"Final cleaned DataFrame: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


# ------------------------------
# Optional: Run independently
# ------------------------------
if __name__ == "__main__":
    summary_df = fetch_vendor_sales_summary()
    if not summary_df.empty:
        print(" Top 5 records:")
        print(summary_df.head())

        clean_df = clean_data(summary_df)
        os.makedirs("data_output", exist_ok=True)
        clean_df.to_csv("data_output/vendor_sumary_clean.csv", index=False)
        print(" Cleaned vendor summary saved to data_output/vendor_summary_clean.csv")
    else:
        print("No data returned from vendor summary query.")

