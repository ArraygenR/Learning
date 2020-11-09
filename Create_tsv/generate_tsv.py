import re

filename = "go-basic.obo"
def split_term(filename):
    f = open(filename)
    data = f.read()
    f.close()
    all_term = [d.strip() for d in data.split("[Term]") if "id:" in d and "[Typedef]" not in d]
    return  all_term

def parse_go_term(term):
    ID = term.strip()[term.find("id") + len("id:"): term.find("\n", term.find("id"))].strip()
    is_id = re.findall(r'is_a:(.*?)!', term)
    is_id = [id1.strip() for id1  in is_id]
    return (ID , is_id)

def map_protien_to_go(filename):
    f = open(filename)
    protien_dict = {}
    for line in f:
        if not line.startswith("!"):
            splitted = line.strip().split("\t")
            if splitted[1] in protien_dict.keys():
                val = protien_dict[splitted[1]]
                val.add(splitted[4])
                protien_dict[splitted[1]] = val
            else:
                val = {splitted[4],}
                protien_dict[splitted[1]] = val
    return protien_dict

def find_parent_term(go_id, go_dict):
    list1 = []
    if go_id in go_dict.keys():
        list1 = go_dict[go_id]
        for l in list1:
            if l in go_dict.keys():
                list1.extend(go_dict[l])
    return(list(set(list1)))


go_dict ={}
for term in split_term(filename):
    ID , is_id  = parse_go_term(term)
    go_dict[ID] = is_id
find_parent_term("GO:0000166", go_dict)

dict1 = map_protien_to_go("goa_human_subset.gaf")
for k, v in dict1.items():
    print(k, list(v))


