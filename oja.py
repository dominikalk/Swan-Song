string = "hello"
string_list = string.split()
string = ""
print(string_list)
for x in string_list:
    if x.upper() != x:
        x = x[0].upper()+ x[1:]
    string = string + x + " "
print(string)
