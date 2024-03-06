import asyncio
import os
import logging
import pandas as pd

from core.config import settings
from db.engine import engine
from utils.eda import clean_column_names

script_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join(script_dir, "log", "executing.log"),
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

data_path = os.path.join(script_dir, "data", settings.DATA_FILE)
df = pd.read_csv(data_path, encoding="utf-8", sep=";")
df.columns = clean_column_names(df.columns)

df.to_sql(settings.RAW_TABLE, engine, if_exists='replace', index=False)
logging.info(f"Data loaded into {settings.RAW_TABLE} table")

