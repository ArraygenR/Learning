import re


# Open files for reading and writing.
gene_to_go_filename = "gene_association_subset.gaf"
blast_filename = "blastp.outfmt6"
diff_exp_filename = "diffExpr.P1e-3_C2.matrix"
go_terms_filename = "go-basic.obo"
report_filename = "old_report.tsv"
gene_to_go_file = open(gene_to_go_filename)
blast_file = open(blast_filename)
diff_exp_file = open(diff_exp_filename)
go_terms_file = open(go_terms_filename)
report_file = open(report_filename, "w")

# Create dictionaries.
gene_to_go = {}
go_to_desc = {}
transcript_to_protein = {}
diffexp_to_samples = {}

# Load transcript IDs of query sequence (qseqid) and SwissProt IDs of subject
# sequence (sseqid) without version number to the dictionary.
for line in blast_file:
    qseqid, sseqid, pident, length, mismatch, gapopen, qstart, qend, sstart, send, evalue, bitscore = line.rstrip().split("\t")
    transcript, isoform = qseqid.split("|")
    gi_type, gi, sp_type, sp, sp_name = sseqid.split("|")
    sp_id, sp_version = sp.split(".")
    transcript_to_protein[transcript] = sp_id

# Load protein IDs and corresponding GO terms to the dictionary.
for line in gene_to_go_file:
    db, object_id, object_symbol, qualifier, go_id, *others = line.split("\t")

    # Check if both protein and GO IDs have a value before adding.
    if object_id and go_id:
        gene_to_go[object_id] = go_id

# Load GO IDs and their names to the dictionary.
terms = go_terms_file.read()
terms = re.findall(r"\[Term]\n(.*?)\n\n", terms, re.DOTALL)

for term in terms:
    go_id = re.search(r"^id:\s+(GO:\d+?)\n", term)
    go_name = re.search(r"^name:\s+(.+?)\n", term, re.M)

    # Check if both ID and name have a value before adding.
    if go_id and go_name:
        go_to_desc[go_id.group(1)] = go_name.group(1)

# Loop through differential expression file; lookup the protein ID and
# GO term + GO name; print results to REPORT output.
diff_exp_file.readline()  # skip header
for line in diff_exp_file:
    transcript, sp_ds, sp_hs, sp_log, sp_plat = line.rstrip().split("\t")

    protein = transcript_to_protein.get(transcript, "NA")
    go_id = gene_to_go.get(protein, "NA")
    go_desc = go_to_desc.get(go_id, "NA")

    report_file.write("\t".join([transcript, protein, sp_ds, sp_hs, sp_log, sp_plat, go_id, go_desc]) + "\n")

# Close files.
gene_to_go_file.close()
blast_file.close()
diff_exp_file.close()
go_terms_file.close()
report_file.close()
