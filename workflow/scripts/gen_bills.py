from cbsserverbilling import billing

billing.generate_all_pi_bills([snakemake.input[0],
                               snakemake.input[1],
                               snakemake.input[2],
                               snakemake.input[3]],
                              snakemake.config["quarter"],
                              "results")
billing.summarize_all_pi_bills([snakemake.input[0],
                               snakemake.input[1],
                               snakemake.input[2],
                               snakemake.input[3]],
                              snakemake.config["quarter"],
                              f"results/summary_{snakemake.config['quarter']}.xlsx")
