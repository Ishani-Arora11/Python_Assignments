with open('output.txt' , 'wt') as fh:
    data = input("Enter text to write to the file: ")
    fh.write(data)

print("Data successfully written to output.txt.\n")

with open('output.txt' , 'at') as fh:
    data = input("Enter additional text to append: ")
    fh.write(f"\n{data}")

print('Data successfully appended.\n')
print('Final content of output.txt:')

with open('output.txt' , 'rt') as fh:
    data = fh.readlines()
    for d in data:
        print(d)