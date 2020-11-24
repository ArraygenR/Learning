import re

def f_transcript_to_protein(blast_filename):
    """
    Load transcript IDs of query sequence (qseqid) and SwissProt IDs of subject
    sequence (sseqid) without version number to the dictionary.
    :param path: input fil path
    :return: transcript_to_protein = {}
    """
    transcript_to_protein = {}
    blast_file = open(blast_filename)

    for line in blast_file:
        qseqid, sseqid, pident, length, mismatch, gapopen, qstart, qend, sstart, send, evalue, bitscore = line.rstrip().split(
            "\t")
        transcript, isoform = qseqid.split("|")
        gi_type, gi, sp_type, sp, sp_name = sseqid.split("|")
        sp_id, sp_version = sp.split(".")
        if float(pident) > 99 and transcript not in transcript_to_protein.keys():
            transcript_to_protein[transcript] = sp_id

    blast_file.close()
    return transcript_to_protein

def f_gene_to_go(gene_to_go_filename):
    """
    :param gene_to_go_filename:
    :return:
    """
    gene_to_go = {}
    gene_to_go_file = open(gene_to_go_filename)
    # Load protein IDs and corresponding GO terms to the dictionary.
    for line in gene_to_go_file:
        db, object_id, object_symbol, qualifier, go_id, *others = line.split("\t")

        # Check if both protein and GO IDs have a value before adding.
        if object_id and go_id:

            if object_id in gene_to_go.keys():
                l1 = gene_to_go[object_id]
                l1.add(go_id)
                gene_to_go[object_id] = l1
            else:
                gene_to_go[object_id] = {go_id,}
    gene_to_go_file.close()

    return gene_to_go

def f_go_terms(go_terms_filename):
    go_terms_file = open(go_terms_filename)
    go_to_desc = {}
    is_a_dict = {}
    # Load GO IDs and their names to the dictionary.
    terms = go_terms_file.read()
    terms = re.findall(r"\[Term]\n(.*?)\n\n", terms, re.DOTALL)

    for term in terms:
        go_id = re.search(r"^id:\s+(GO:\d+?)\n", term)
        go_name = re.search(r"^name:\s+(.+?)\n", term, re.M)
        # Check if both ID and name have a value before adding.
        if go_id and go_name:
            go_to_desc[go_id.group(1)] = go_name.group(1)

    go_terms_file.close()
    return go_to_desc

def f_diff_exp(diff_exp_filename, report_filename, transcript_to_protein, gene_to_go, go_to_desc):
    """
    :param diff_exp_filename:
    :param report_filename:
    :param transcript_to_protein:
    :param gene_to_go:
    :param go_to_desc:
    :return:
    """
    diff_exp_file = open(diff_exp_filename)
    report_file = open(report_filename, "w")
    # Loop through differential expression file; lookup the protein ID and
    # GO term + GO name; print results to REPORT output.
    diff_exp_file.readline()  # skip header
    for line in diff_exp_file:
        transcript, sp_ds, sp_hs, sp_log, sp_plat = line.rstrip().split("\t")

        protein = transcript_to_protein.get(transcript, "NA")
        go_ids = gene_to_go.get(protein, ["NA"])

        go_desc=''
        go_ids = list(set(go_ids))
        go_ids.sort()
        #print(go_ids)
        for i, go_id in enumerate(go_ids):
            if i == 0:
                report_file.write(
                    "\t".join([transcript, protein, sp_ds, sp_hs, sp_log, sp_plat, go_id, go_to_desc.get(go_id, "NA")]) + "\n")
            else:
                report_file.write(
                    "\t".join(["", "", "", "", "", "", go_id, go_to_desc.get(go_id, "NA")]) + "\n")

    diff_exp_file.close()
    report_file.close()

if __name__ == "__main__":
    blast_filename = "blastp.outfmt6"
    gene_to_go_filename = "gene_association_subset.gaf"
    go_terms_filename = "go-basic.obo"
    diff_exp_filename = "diffExpr.P1e-3_C2.matrix"
    report_filename = "old_report_OP1.tsv"

    transcript_to_protein = f_transcript_to_protein(blast_filename)
    gene_to_go = f_gene_to_go(gene_to_go_filename)
    go_to_desc = f_go_terms(go_terms_filename)

    f_diff_exp(diff_exp_filename,report_filename, transcript_to_protein,gene_to_go, go_to_desc)