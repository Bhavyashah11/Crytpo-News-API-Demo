import requests
from pprint import pprint 
from bs4 import BeautifulSoup
url = "https://cryptocurrency-new-live.p.rapidapi.com/news"

#Use this endpoints to request data from a particular website.
#url = "https://cryptocurrency-new-live.p.rapidapi.com/news/moneycontrol"
#url = "https://cryptocurrency-new-live.p.rapidapi.com/news/economictimes"
#url = "https://cryptocurrency-new-live.p.rapidapi.com/news/financialexpress"
headers = {
	"X-RapidAPI-Host": "cryptocurrency-new-live.p.rapidapi.com",
	"X-RapidAPI-Key": "Add your API KEY"
}

response = requests.request("GET", url, headers=headers)

pprint(response.json())