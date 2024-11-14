def convert(a):
    dict1={}
    for item in a:
        dict1[item[0]]=item[1:]
    return dict1

a=[[1,"abc","V"],[2,"xyz","VII"],[3,"pqr",'VIII']]
print(convert(a))
