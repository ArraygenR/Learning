class BlastHit:
    def __init__(self, TranscriptID, SwisprotID, identity, mismatch):
        self.TranscriptID = TranscriptID
        self.SwisprotID =SwisprotID
        self.identity = identity
        self.mismatch = mismatch

    def __repr__(self):
        return ('BlastHit("{}", "{}", "{}", "{}")'.format(self.TranscriptID,self.SwisprotID, self.identity,self.mismatch))

    def __lt__(self, other):
        if float(other.identity) > float(self.identity):
            return True
            #print("Second object is having greater percent identity than first")
        else:
            return False
            #print("Second object is having lesser percent identity than first")

    def check_good_match(self):
        if float(self.identity) > 99:
            return True
        else:
            return False

if __name__ == "__main__":
    # for testig purpose
    data = "c0_g1_i1|m.1	gi|74665200|sp|Q9HGP0.1|PVG4_SCHPO	100.00	372	0	0	1	372	1	372	0.0	  754".split("\t")
    bh = BlastHit(data[0], data[1].split("|")[3].split(".")[0], data[2], data[4])

    data = "c1018_g1_i1|m.818	gi|122178461|sp|Q1EPG7.1|CSPL1_MUSAC	26.76	71	51	1	12	82	53	122	1.0	32.0".split("\t")
    bh1 = BlastHit(data[0], data[1].split("|")[3].split(".")[0], data[2], data[4])

    print(bh1 > bh)
    print(bh)