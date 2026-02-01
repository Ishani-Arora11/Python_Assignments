"""
Create a list of numbers from 1 to 10.
Extract the first five elements from the list.
Reverse these extracted elements.
Prints the original list , the extracted list and the reversed list
"""



l1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
extracted_list = l1[0 : 5]
reversed_extracted_list = extracted_list[::-1]
print(f"Original list: {l1}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_extracted_list}")