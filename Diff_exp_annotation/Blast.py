class Blast:
    def __init__(self, hits):
        self.hits = hits

    def __repr__(self):
        return ",".join([str(h) for h in self.hits])

    def __iter__(self):
        return iter(self.hits)

if __name__ == "__main__":
    # for testig purpose
    from BlastHit import BlastHit
    #f1 = open("blastp.outfmt6")
    f1 = ["c0_g1_i1|m.1	gi|74665200|sp|Q9HGP0.1|PVG4_SCHPO	100.00	372	0	0	1	372	1	372	0.0	  754",
          "c1018_g1_i1|m.818	gi|122178461|sp|Q1EPG7.1|CSPL1_MUSAC	26.76	71	51	1	12	82	53	122	1.0	32.0"]
    blast = Blast([BlastHit(data.strip().split("\t")[0].split("|")[0],
                            data.strip().split("\t")[1].split("|")[3].split(".")[0], data.strip().split("\t")[2],
                            data.strip().split("\t")[4]) for data in f1])
    #f1.close()
    for b in blast:
        print(b)
