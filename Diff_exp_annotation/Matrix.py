class Matrix:
    def __init__(self, expressions):
        self.expressions = expressions

    def __repr__(self):
        return ",".join([str(e) for e in self.expressions])

    def __iter__(self):
        return iter(self.expressions)

if __name__ == "__main__":
    # for testig purpose
    from DiffExp import DiffExp
    #f2 = open("diffExpr.P1e-3_C2.matrix")
    f2 = ["c3833_g1_i2	4.00	0.07	16.84	26.37",
          "c4832_g1_i1	24.55	116.87	220.53	28.82"]
    mat = Matrix([DiffExp(data.split("\t")[0], data.split("\t")[1], data.split("\t")[2], data.split("\t")[3],
                          data.rstrip().split("\t")[4]) for data in f2])
    #f2.close()
    for m in mat:
        print(m)
