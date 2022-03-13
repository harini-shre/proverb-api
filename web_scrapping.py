# this python file is used to scrape proverbs from a website and store the scrapped data in csv format
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.inc.com/sujan-patel/101-inspiring-quotes-from-the-most-successful-people-in-history.html")
soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find_all('div', class_='standardText')
print(type(result), len(result))
print(result[0].get_text())
print("\n")

df = pd.DataFrame(None, columns=['Proverb_Num','Author','Proverb'])
for ind in range(1,len(result)):
    txt = result[ind].get_text()
    Proverb_Num = int(ind)
    Author = txt[ (txt.rfind("-")+1) :].rstrip().lstrip()
    Author = Author.lower()
    Proverb = txt[ (txt.find("\"")+1) : (txt.rfind("\"")-1)].rstrip().lstrip()
    df.loc[len(df.index)] = [Proverb_Num, Author, Proverb]

print(df.tail())

df.to_csv("proverb_scrapping.csv", index=False)
# go the csv file and remove the lines that are not proverb or not in format manually and save the file

