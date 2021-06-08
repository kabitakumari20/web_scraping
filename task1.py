from pprint import pprint
import json
import requests
from bs4 import BeautifulSoup
var=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
res= BeautifulSoup(var.text,"html.parser")
def scrap_top_list():
    main_div=res.find("div",class_="lister")
    table=main_div.find("tbody",class_="lister-list")
    trs=table.find_all("tr")

    movie_name=[] 
    year_of_realase = []
    movie_rank=[]
    movie_url=[]
    movie_rating = []
    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=" "
        for i in position:
            if "." not in i:
                rank=rank+i
            else: 
                break
            
        movie_rank.append(rank)
        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)

        year=tr.find("td",class_="titleColumn").span.get_text()
        year_of_realase.append(year)

        imbd_rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(imbd_rating)

        link=tr.find("td",class_="titleColumn").a ["href"]
        movie_link="https://www.imdb.com"+link
        movie_url.append(movie_link)

    top_movie=[]
    details={"position":" ","name":" ","year":" ","Rating":" ","url":" "}

    for  i in range(0,len(movie_rank)):
        details["position"]=int(movie_rank[i])

        details["name"]=str(movie_name[i])
        
        year_of_realase[i]=year_of_realase[i][1:5]
        
        details["year"]=int(year_of_realase[i])
        
        details["Rating"]=float(movie_rating[i])
        
        details["url"]=movie_url[i]
        
        top_movie.append(details.copy())
        
    with open("task1.json","w+") as f:
        json.dump(top_movie,f,indent=4)
    return top_movie
# scrap_top_list()
return_value=scrap_top_list()
# pprint(return_value)



