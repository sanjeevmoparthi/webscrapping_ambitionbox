import pandas as pd
import requests
from bs4 import BeautifulSoup

for j in range(1,20):
    url = 'https://www.ambitionbox.com/list-of-companies?page={}'.format(j)
    headers=headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}
    webpage = requests.get(url,headers = headers).text
    soup = BeautifulSoup(webpage,'lxml')
    company=soup.find_all('div' ,class_="companyCardWrapper__primaryInformation")
    
    name = []
    rating = []

    for i in company:
        name.append(i.find('h2').text.strip())
        rating.append(i.find_all('div',class_="rating_star_container")[0].text.strip())

    d = {'name':name,'rating':rating}
    df = pd.DataFrame(d)

print(df) 