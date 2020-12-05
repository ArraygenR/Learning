from BlastHit import BlastHit
from Blast import Blast
from DiffExp import DiffExp
from Matrix import Matrix
def tup_to_str(tup): return "\t".join(tup)
fw = open("output_diff.txt","w")
f1 = open("blastp.outfmt6")
f2 = open("diffExpr.P1e-3_C2.matrix")
mat = Matrix([DiffExp(data.split("\t")[0], data.split("\t")[1] , data.split("\t")[2], data.split("\t")[3], data.rstrip().split("\t")[4]) for data in f2])
dict2= {b.TranscriptID : b.SwisprotID for b in Blast([BlastHit(data.strip().split("\t")[0].split("|")[0], data.strip().split("\t")[1].split("|")[3].split(".")[0], data.strip().split("\t")[2], data.strip().split("\t")[4]) for data in f1]) if b.check_good_match()}
for m in mat:
    print(dict2.get(m.transcript, m.transcript)+"\t"+tup_to_str(m.attr_tup()), file=fw)
f1.close()
f2.close()
fw.close()