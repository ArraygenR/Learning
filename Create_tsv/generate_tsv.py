import re,sys

# for splitting terms from obo file and making list
def split_term(filename):
    # opening file
    f = open(filename)
    # reading all data from file storing into data variable
    data = f.read()
    f.close()
    all_term =[]
    # split data by word [term] , iterate through each term
    for d in data.split("[Term]"):
        # if "id:" is there then select term
        if "id:" in d:
            # last term will have typedef data too
            if  "[Typedef]" in d:
                # therefore for last term fetching till \n\n
                all_term.append(d[:d.find("\n\n")])
            else:
                # adding other terms normally
                all_term.append(d)
    # same numbers od terms present in obo file
    #print(len(all_term))
    return  all_term

# fetch ID and its respective is_id list fetching
def parse_go_term(term):
    # fetch ID
    ID = term.strip()[term.find("id") + len("id:"): term.find("\n", term.find("id"))].strip()
    # return list of is_id by pattern match
    is_id = re.findall(r'is_a:(.*?)!', term)
    # remove empty spaces from all ids
    is_id = [id1.strip() for id1  in is_id]
    return (ID , is_id)

# create dictionary of gaf file
def map_protien_to_go(filename):
    # open file
    f = open(filename)
    # create empty dictionary
    protien_dict = {}
    # read file line by line
    for line in f:
        # if ! in line then only select line
        if not line.startswith("!"):
            # split id by tab so that we can get column wise
            splitted = line.strip().split("\t")
            # if first column data already exists in dictionary then
            # fetch existing set and add new element to it
            # else create new set of one element
            if splitted[1] in protien_dict.keys():
                val = protien_dict[splitted[1]]
                val.add(splitted[4])
                protien_dict[splitted[1]] = val
            else:
                val = {splitted[4],}
                protien_dict[splitted[1]] = val
    return protien_dict

# find parent term
def find_parent_term(go_id, go_dict):
    list1 = []
    # create list of all elements and sibling elements
    if go_id in go_dict.keys():
        # you will get is_a
        list1 = go_dict[go_id]
        # for fetching is_a of fetched is_a one by one and storing to list1
        for l in list1:
            if l in go_dict.keys():
                list1.extend(go_dict[l])
    # remove duplicates of created list using set
    return(list(set(list1)))

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        input_terms = sys.argv[1] #"go-basic.obo"
        input_annotation = sys.argv[2]#"goa_human_subset.gaf"
        output_filename = "result.tsv"
        if len(sys.argv) > 3:
            output_filename = sys.argv[3]
        #print(input_terms, input_annotation, output_filename)

        # open file for writing
        fw = open(output_filename, "w")
        # empty dict for storing go terms
        go_dict ={}
        # get all splitted terms
        for term in split_term(input_terms):
            # call parse term to create go_dict
            ID , is_id  = parse_go_term(term)
            go_dict[ID] = is_id

        # get protien dict
        dict1 = map_protien_to_go(input_annotation)
        # fetch data from protien dict
        for k, v in dict1.items():
            # print first column id
            print(k, end="\t" , file=fw)
            # for second column
            for cnt, v_ in enumerate(list(v)):
                if cnt == 0 :
                    print(v_ , end="\t", file=fw)
                else:
                    print("\t", v_, end="\t", file=fw)
                v1 = find_parent_term(v_, go_dict)
                # for third column
                for cnt1, v1_ in enumerate(v1):
                    if cnt1 == 0:
                        print(v1_, file = fw)
                    else:
                        print("\t\t",v1_ , file = fw)
    else:
        print("<input_file> not found.  Check the file path and try again.")