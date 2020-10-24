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
