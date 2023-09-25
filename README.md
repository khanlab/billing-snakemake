# CBS Server Billing Workflow

This is a Snakemake workflow that automatically invokes the CBS Server billing script on a set of spreadsheets, then converts the resulting .tex files into PDFs using tectonic.

## Installation

1. Install the python dependencies with `pip install -e .`
2. Either install Singularity, or install tectonic on your system.

## Running the workflow

1. Download the four CBS Server excel sheets to `billing_snakemake/resources`
2. Run `snakemake --config quarter={quarter} --cores --use-singularity`, replacing `{quarter}` with the date of the first day of the quarter you'd like to format, in ISO 8601 extended format (`YYYY-MM-DD`). E.g. to process the quarter from May 1, 2023 to July 30, 2023, you would run `snakemake --config quarter=2023-05-01`.
  Note: If you have tectonic installed directly, you can drop `--use-singularity`.
3. Results will be generated in two directories:
  - `billing_snakemake/results/tex_{quarter}` will contain the raw tex files, *and* an excel sheet summarizing the bills for the quarter.
  - `billing_snakemake/results/pdf_{quarter}` will contain the PDF files for all the bills.
