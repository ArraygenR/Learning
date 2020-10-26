def split_records(path):
    f = open(path)
    records = []
    all_data = f.read()
    for data in all_data.split("//"):
        if data.strip() != '':
            records.append(data)
    return records

def get_header(record):
    lines = record.split("\n")
    version =''
    defination =''
    part = ''
    for line in lines:
        if line[:5].strip()== '':
            part += line+"\n"
        else:
            if "DEFINITION" in part:
                defination = part.replace("DEFINITION", "").strip()
            elif "VERSION" in part:
                version = part.replace("VERSION", "").strip()
            part =line+"\n"
    return ">"+version+" "+defination

def get_sequence(record):
    lines = record.split("\n")
    seq = ''
    part = ''
    for line in lines:
        if line[:5].strip()== '':
            part += line+"\n"
        else:
            if "ORIGIN" in part:
                seq = part.replace("ORIGIN","").strip()
            part =line+"\n"
    if "ORIGIN" in part:
        seq = part.replace("ORIGIN","")
    seq = "\n".join(list(filter(None, [s[9:].replace(" ","").strip() for s in seq.split("\n")])))
    return seq
records = split_records("ls_orchid.gbk")

record = records[0]
header = get_header(record)
seq = get_sequence(record)
print(header)
print(seq)


import textwrap , sys
def split_records(path):
    # opening file in reading mode
    f = open(path)
    # this empty list will be helpfull for storing records
    records = []
    all_data = f.read()
    for data in all_data.split("//\n"):
        if data.strip() != '':
            # if record is not empty add it to list
            records.append(data)
    return records

def get_header(record):
    lines = record.split("\n")
    version =''
    defination =''
    for line in lines:
        if "DEFINITION" in line:
            defination = line.replace("DEFINITION", "").strip()
        elif "VERSION" in line:
            version = line.replace("VERSION", "").strip()

    return ">"+version+" "+defination

def get_sequence(record):
    lines = record.split("\n")
    seq = ''
    part = ''
    for line in lines:
        if line[:5].strip() == '':
            part += line+"\n"
        else:
            part = line+"\n"

    if "ORIGIN" in part:
        seq = part.replace("ORIGIN","")

    seq = "".join(list(filter(None, [s[9:].replace(" ","").strip() for s in seq.split("\n")])))
    wrapper = textwrap.TextWrapper(width=70)
    seq_list = wrapper.wrap(text=seq)
    return "\n".join(seq_list).upper()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].strip("'").strip('"').endswith("gb"):
            ## first argument will be input file name..
            input_file = sys.argv[1].strip("'").strip('"')
            # second arg will be o/p file name
            # check if given or not..
            if len(sys.argv) > 2:
                output_file_name =  sys.argv[2]+".fasta"
            else:
                output_file_name = sys.argv[1].strip("'").strip('"').replace(".gb",".fasta")
            # open file in which we want to write o/p
            fw = open(output_file_name, "w")
            # calling split function to get records
            records = split_records(input_file)
            for record in records:
                header = get_header(record)
                seq = get_sequence(record)
                print(header , file=fw)
                print(seq, file=fw)
                print(file=fw)
        else:
            print("Provide a GenBank file to convert to FASTA.")
    else:
        print("<input_file> not found.  Check the file path and try again.")

