from pathlib import Path
from json import dump
import pandas as pd

totals = {
    Path(summary).name: pd.read_excel(summary)["total_price"].sum()
    for summary in snakemake.input["summaries"]
}
totals["grand_total"] = sum(totals.values())
with open(snakemake.output["summary_json"], "w", encoding="utf-8") as out_file:
    dump(totals, out_file)
