from cbsserverbilling import billing

billing.generate_all_pi_bills([snakemake.input[0],
                               snakemake.input[1],
                               snakemake.input[2],
                               snakemake.input[3]],
                              snakemake.config["quarter"],
                              "results")
