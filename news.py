from bs4 import BeautifulSoup
import re # import Regular expression operations module
import requests
from time import gmtime, strftime
# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.doh.gov.ae/en/covid-19/news"

# opens the connection and downloads html page from url
 # Add header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

r = requests.get(page_url, headers=headers)

# print(r) # print request to see if Response 200

page_soup = BeautifulSoup(r.content, "html.parser")


 
# finds each product from the store page
containers = page_soup.findAll("div", {"class": "newsBox"})

 

# name the output file to write to local disk
out_filename = "news.csv"
# header of csv file to be written
headers = "day,month,text,link \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)


# loops over each product and grabs attributes about
# each product
for container in containers:
    # Finds all link tags "a" from within the first div.
    make_rating_sp = container.div.select("a")
