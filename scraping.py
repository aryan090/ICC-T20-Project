import requests
from bs4 import BeautifulSoup
url = "https://stats.espncricinfo.com/ci/content/records/283277.html"

req = requests.get(url)
htmlContent = req.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# title = soup.title

# print(type(soup))
# print(type(title))
# print(type(title.string))

# pars = soup.find_all('div')
# print(pars)

# anc = soup.find_all('a')
# print(anc)

# print(soup.find('p'))
# print(soup.find('p')['class'])

# print(soup.find_all("p", class_="message"))
# print(soup.find('p').get_text())
# print(soup.get_text())

# # Get all the anchor tags from the page
# anchors = soup.find_all('a')
# all_links = set()
# # Get all the links on page:
# for link in anchors:
#     if(link.get('href') != '#'):
#         linktext = "https://stats.espncricinfo.com/ci/content/records/283277.html" + \
#             link.get('href')
#         all_links.add(link)
#         print(linktext)
