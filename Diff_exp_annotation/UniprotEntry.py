import re

class UniprotEntry:
    db = "sp"
    def __init__(self, data):
        self.entry_name = re.search(r"^ID\s+(.+?)\s", data, re.M).group(1)
        self.seq = data[data.find("\n",data.find("SQ   ")): data.find("//",data.find("SQ   "))].replace(" ","").strip() # re.search(r"^SQ(.*);", data)
        self.status = data[data.find(" ",data.find(self.entry_name)):data.find(";",data.find(" ",data.find(self.entry_name)))].strip()
        self.accession = re.search(r"^AC\s+(.+?);", data, re.M).group(1)
        self.organism = re.search(r"^OS\s+(.+?)\n", data, re.M).group(1)
        self.taxon_id = re.search(r"^OX\s+(.+?);", data, re.M).group(1).replace("NCBI_TaxID=","").strip()

        d = re.search(r"^GN\s+(.+?);", data, re.M).group(1).replace("Name=","").strip()
        if "{" in d and "=" in d:
            d = d[d.find("=") + 1:d.find("{")].strip()
        elif "{" in d:
            d = d[:d.find("{")].strip()
        self.gene_name = d

        d =  re.search(r"^DE\s+(.+?);", data, re.M).group(1).replace("RecName: Full=","").strip()
        if "{" in d and "=" in d:
            d= d[d.find("=")+1:d.find("{")].strip()
        elif "{" in d:
            d = d[:d.find("{")].strip()
        self.protien_name = d
        self.protien_evi = re.search(r"^PE\s+(.+?):", data, re.M).group(1)
        self.seq_version = data[data.find("sequence version"):data.find("\n",data.find("sequence version"))].strip().strip(".")


    def is_reviewed(self):
        if self.status == "Reviewed":
            return True
        else:
            return False

    def to_fasta(self):
        return (
            ">"+ UniprotEntry.db+ "|" + self.accession + "|" + self.entry_name + "|" + self.protien_name + " OS=" + self.organism + " OX=" + self.taxon_id + " GN=" + self.gene_name + " PE=" + self.protien_evi + " " + "\n" + self.seq)

if __name__ == "__main__" :
    file_name = "uniprot-neurofibromas.txt"
    f = open(file_name)
    op_file_name = file_name.replace(".txt","1.fasta")
    fw = open(op_file_name,"w")
    data_all= f.read()
    for i, data in enumerate(data_all.split("//\n")):
        if data.strip()!='':
            ue= UniprotEntry(data+"//")
            if ue.is_reviewed():
                print(ue.to_fasta(), file=fw)
    fw.close()