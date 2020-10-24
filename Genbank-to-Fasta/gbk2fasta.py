f = open("ls_orchid.gbk")
all_data = f.read()
for data in all_data.split("//"):
    if data.strip() != '':
        lines = data.split("\n")
        print("-"*20)
        for line in lines:
            print(line)
