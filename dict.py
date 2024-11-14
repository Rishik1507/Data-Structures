dict1={
    "Name":"Rishik",
    "Gender": "Male",


}
dict2={
    2:"b",
    1:"a",
    3:"c",
    4:"d"
}

print(dict1["Name"])
print(dict1.get("Gender"))
dict1["Grade"]=9
print(dict1)
dict1.pop("Grade")
print(dict1)
dict1[2]=dict2[2]
dict1[1]=dict2[1]
print(dict1)

