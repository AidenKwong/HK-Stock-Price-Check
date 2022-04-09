import csv, sqlite3, os
from pathlib import Path
import pandas as pd

data_folder_path = Path(__file__).parent / "data"

con = sqlite3.connect("db.sqlite3")

cur = con.cursor()

for filename in os.listdir(data_folder_path):
    if filename.endswith(".csv"):
        code = filename.replace("Equities_", "").replace(".csv", "")
        df = pd.read_csv(data_folder_path / filename)
        df["Code"] = code
        for idx, row in df.iterrows():
            cur.execute(
                """INSERT INTO stocks_stock (time, code, closed_price, volume)
                            VALUES (?, ?, ?, ?)""",
                (
                    row["Time"].replace("/", "-"),
                    row["Code"],
                    row["Closed Price"],
                    row["Volume"],
                ),
            )

con.commit()
con.close()
