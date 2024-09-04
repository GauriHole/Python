lst = ["Gauri",19.4,(25,9,2002),"Info"]
print(lst)
for item in lst:
    print("Info : ",item)
lst.append("Pizza")
print(lst)
lst.remove((25,9,2002))
print(lst)
lst.pop(2)
print(lst)