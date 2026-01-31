try:
    with open("sample.txt" , 'r') as fh:
        data = fh.readlines()
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found")
else:
    i = 1
    print('Reading file content:')
    for d in data:
        print(f"Line{i}:{d}")
        i += 1
