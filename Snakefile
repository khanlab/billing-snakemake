FILENAMES, = glob_wildcards("build/{filename}.tex")

rule all:
    input: expand("build/{filename}.pdf", filename=FILENAMES)

rule process_all_billing:
    input:
        pi="resources/Computational Core Server New PI Form (Responses).xlsx",
        user="resources/Computational Core Server New User Form (Responses).xlsx"
    shell:
        "python3 cbs-server-billing/cbsserverbilling/billing.py \"{input.pi}\" \"{input.user}\" {config[quarter]} build/"

rule process_billing:
    input:
        pi="resources/Computational Core Server New PI Form (Responses).xlsx",
        user="resources/Computational Core Server New User Form (Responses).xlsx"
    output:
        "build/pi-{pi}_quarter-{quarter}_bill.tex"
    shell:
        "python3 cbs-server-billing/cbsserverbilling/billing.py \"{input.pi}\" \"{input.user}\" {wildcards.quarter} build/"

rule generate_pdf:
    input:
        "build/{filename}.tex"
    output:
        "build/{filename}.pdf"
    shell:
        "pdflatex -output-directory build {input} && cd build/ && latexmk -c"
