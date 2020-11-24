import re

class UniprotEntry:
    db = "sp"
    def __init__(self, data):
        self.seq = data[data.find("\n",data.find("SQ   ")): data.find("//",data.find("SQ   "))].replace(" ","").strip() # re.search(r"^SQ(.*);", data)
        self.accession = re.search(r"^AC\s+(.+?);", data, re.M).group(1)
        self.entry_name = re.search(r"^ID\s+(.+?)\s", data, re.M).group(1)
        self.organism = re.search(r"^OS\s+(.+?)\n", data, re.M).group(1)
        self.taxon_id = re.search(r"^OX\s+(.+?);", data, re.M).group(1).replace("NCBI_TaxID=","").strip()
        d =  re.search(r"^DE\s+(.+?);", data, re.M).group(1).replace("RecName: Full=","").strip()
        if "{" in d and "=" in d:
            d= d[d.find("=")+1:d.find("{")].strip()
        elif "{" in d:
            d = d[:d.find("{")].strip()
        self.protien_name = d
        print(">sp"+"|"+self.accession+"|"+self.entry_name+"|"+self.protien_name+" OS="+self.organism+" OX="+self.taxon_id,"\n"+self.seq)


file_name = "uniprot-neurofibromas.txt"
f = open(file_name)
data_all= f.read()
for i, data in enumerate(data_all.split("//\n")):
    if data.strip()!='':
        UniprotEntry(data+"//")