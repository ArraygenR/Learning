f =open("old_report.tsv")
s1 = set()
for line in f:
    s1.add(line.split("\t")[0])
print(len(s1))