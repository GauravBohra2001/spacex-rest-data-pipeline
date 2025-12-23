# def add_numbers (a,b):
#     return a + b

# print(add_numbers(2,3))
# print(add_numbers(2.0,3))

with open("sample.txt", "a") as s:
    s.write("\nI am good\n")

with open("sample.txt") as s:
    print(s.read())


