def read_lines():
    with open(r"tp08/MOCK_DATA.csv") as f:
        for line in f:
            yield line.strip()

def get_male(gen):
    for data in gen:
        l = data.split(",")
        if l[-2] == "Male":
            yield data


def main01():
    i= get_male(read_lines())
    all_data = list(i)
    print(len(all_data))


def main():
    file_name = "tp08/MOCK_DATA.csv"
    
    lines = (line for line in open(file_name))
    list_lines = (line.strip() for line in lines)   
    male = (l for l in get_male(list_lines))

    print(len(list(male)))    
if __name__=='__main__':
    main()

