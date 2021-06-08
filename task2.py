from task1 import return_value
import json
from pprint import pprint

def group_by_year(movies):
    years=[]

    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)

    my_dict={i:[] for i in years}
    for i in movies:
        year=i["year"]


        for x in my_dict:
            if str(x)==str(year):
                my_dict[x].append(i)
    with open("task2.json","a") as f2:
        json.dump(my_dict,f2,indent=4)

    return my_dict

group_by_year(return_value)
# dec_arg=group_by_year(return_value)
# pprint(dec_arg)



