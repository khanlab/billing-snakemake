from pathlib import Path
from cbsserverbilling import billing

out_dir = Path(snakemake.output["quarter_dir"])
out_dir.mkdir()
billing.generate_all_pi_bills(
    [snakemake.input[0], snakemake.input[1], snakemake.input[2], snakemake.input[3]],
    snakemake.wildcards["quarter"],
    str(out_dir),
)
billing.summarize_all_pi_bills(
    [snakemake.input[0], snakemake.input[1], snakemake.input[2], snakemake.input[3]],
    snakemake.wildcards["quarter"],
    str(out_dir / f"summary_{snakemake.wildcards['quarter']}.xlsx"),
)
