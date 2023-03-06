import pandas as pd
from pathlib import Path


bike_sales_frame: pd.DataFrame = pd.read_csv(f"{Path.parent(Path.cwd())}/resources/ebike-sales.csv")