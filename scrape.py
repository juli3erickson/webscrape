import requests
from bs4 import BeautifulSoup
import pprint

# res = requests.get(f'https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select('.storylink')
# subtext = soup.select('.subtext')

num_pages = 2
links = []
subtext = []

for pg in range(1, num_pages+1):
        res = requests.get(f'https://news.ycombinator.com/news?p={pg}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links.extend(soup.select('.storylink'))
        subtext.extend(soup.select('.subtext'))

print(len(links))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes':points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))
