from task2 import dec_arg
import json
from pprint import pprint

def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=index%10

        decade=index-mod
        if decade not in list1:
            list1.append(decade)

    list1.sort()

    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9

        for x in movies:
            if x <=dec10 and x>=i:
                for v in movies[x]:
                    pprint(v)
                    moviedec[i].append(v)

    with open("task3.json","a") as f3:
        json.dump(moviedec,f3,indent=4)

    return moviedec
# pprint(group_by_decade(dec_arg)) 
group_by_decade(dec_arg)

