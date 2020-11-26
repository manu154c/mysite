
def upload_the_file(file_location):
    
    destination_file = 'dataset.txt'
    f = open(file_location, 'r')
    with open(destination_file, 'w') as destination:
        list_of_lines = []
        for chunk in f.readlines():
            destination.writelines(chunk)
            list_of_lines.append(chunk)
    
    return list_of_lines


def extract_concepts_from_sentences():
    
    create_snt_amr_file()
    #index_the_sentence()
    
    return 1

def create_snt_amr_file():
    
    file = open('dataset.txt', 'r')
    lines = file.read()
    with open('sentences.txt', 'w') as destination:
        line_split = lines.split("\n\n")
        #print(line_split[3].split('\n')[1])
        for line_set in line_split[1:]:
            try:
                snt = line_set.split('\n')[1]
            except:
                print(snt)
            else:
                destination.write(snt[8:])
                destination.write("\n")
    
    # Linearizing to AMR String.
    with open('amrs.txt', 'w') as destination:
        line_split = lines.split("\n\n")
        #print(line_split[3].split('\n')[1])
        for i in line_split[1:]:
            amr_as_list = i.split("\n")[3:]
            amrStr = ' '.join([str(elem) for elem in amr_as_list])
            destination.write(amrStr)
            destination.write("\n")
            
    return 1


def index_the_sentence():
    file = open('sentences.txt', 'r')
    lines = file.read()
    
    
    return 1