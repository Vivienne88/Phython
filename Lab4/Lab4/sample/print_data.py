def print_data (data, level=0):
    for item in data:
        if isinstance(item, list):
            print_data(item, level+1)
        else:
            for i in range(level):
                print("\t",end="")
            print(item)