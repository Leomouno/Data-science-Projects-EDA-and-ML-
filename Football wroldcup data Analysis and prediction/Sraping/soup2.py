from bs4 import BeautifulSoup
import requests
import pandas as pd

web = 'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
response = requests.get(web)
content = response.text
soup = BeautifulSoup(content, 'lxml')

matches = soup.find_all('div', class_='footballbox')
home=[]
score=[]
away=[]
for match in matches:

    home.append(match.find('th', class_='fhome').get_text())
    score.append(match.find('th', class_='fscore').get_text())
    away.append(match.find('th', class_='faway').get_text())

dict_football={'home': home, 'score': score, 'away' : away }
df_ficture=pd.DataFrame(dict_football)
df_ficture['year']= '2022'
df_ficture.to_csv('fixture 2022.csv',index=False)

