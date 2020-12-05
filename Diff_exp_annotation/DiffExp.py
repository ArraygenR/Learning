class DiffExp:
    def __init__(self, transcript, diauxic_shift, heat_lock, plateau_plate, logarithmic_growth):
        self.transcript = transcript
        self.diauxic_shift =diauxic_shift
        self.heat_lock = heat_lock
        self.plateau_plate = plateau_plate
        self.logarithmic_growth = logarithmic_growth

    def __repr__(self):
        return 'DiffExp("{}", "{}", "{}", "{}" ,"{}")'.format(self.transcript,self.diauxic_shift, self.heat_lock,self.plateau_plate,self.logarithmic_growth)

    def attr_tup(self):
        return (self.diauxic_shift, self.heat_lock, self.plateau_plate, self.logarithmic_growth)

if __name__ == "__main__":
    # for testig purpose
    data = "c3833_g1_i2	4.00	0.07	16.84	26.37"
    de = DiffExp(data.split("\t")[0], data.split("\t")[1] , data.split("\t")[2], data.split("\t")[3], data.strip().split("\t")[4])
    print(de)
    print(de.attr_tup())