from pathlib import Path
from cbsserverbilling.main import process_everything

out_dir = Path(snakemake.output.quarter_dir)
out_dir.mkdir()
process_everything(
    snakemake.input.pi,
    snakemake.input.user,
    snakemake.input.user_update,
    snakemake.input.storage_update,
    snakemake.wildcards.quarter,
    out_dir,
)

