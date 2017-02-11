
import webbrowser, requests, sys, bs4, re

if len(sys.argv) > 2:
    search = ' '.join(sys.argv[1:])  # if more than one search term, combines into one string
else:
    search = sys.argv[1]

search_string = 'https://google.com/search?q={0}'.format(search)
results = requests.get(search_string).text  # loads search page

soup = bs4.BeautifulSoup(results, 'html.parser')
elements = soup.select('div > div > div > div h3 a') # CSS selector for search result links

linkRegex = re.compile(r"""(http[s]?://(?:[A-Za-z0-9./-])+)""")  # Regex from urls
links = linkRegex.findall(str(elements))
links = [webbrowser.open(i) for i in links]
links

