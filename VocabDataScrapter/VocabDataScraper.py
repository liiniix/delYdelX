import requests, pandas, os
from bs4 import BeautifulSoup

# input files are csv with delmeter ;
# get definitions from https://www.english-bangla.com/
# to look up definition of 'failing', url is https://www.english-bangla.com/dictionary/failing
# Bangla definition is at class format1. could be severa; format1

INPUT_FILE = 'group_4.csv'
WORDGROUPS_DIR = 'WordGroups/'

filename = os.path.join(WORDGROUPS_DIR, INPUT_FILE)
df = pandas.read_csv(filename, sep=';', header=None)

for i in range(df.shape[0]):
    english_word = df[0][i]
    print(f"Finding definition of '{english_word}'")
    url = f"https://www.english-bangla.com/dictionary/{english_word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    definitions_html = soup.find_all(class_='format1')
    definitions = [definition_html.text for definition_html in definitions_html]
    
    for definition in definitions:
        df[i][1] = definition
        df[i][1] = definition
        print(df[i][1])
