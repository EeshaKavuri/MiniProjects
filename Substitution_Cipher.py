import string
dict = {}
data = ""
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-1]
with open("student_data.py") as file:
    while True:
        c = file.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        print(data,end='')
