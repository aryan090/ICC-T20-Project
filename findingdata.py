
# data_url = "https://stats.espncricinfo.com/ci/content/records/283277.html"
# data_page = requests.get(data_url)
# # data_page.content
# soup = BeautifulSoup(data_page.content, 'html.parser')
# # soup
# question = soup.findAll(attrs = {'class': 'div630Pad'})
# # answer1 = question[0].text.replace('\n\n\n\n\n\n\n',"")
# # answer2 = question[0].text.replace(',,,',",")
# # answer1
# # main_data = [[answer1]]
# # main_data
# # df = pd.DataFrame(main_data, columns=['Winner', 'Margin', 'Balls Rem', 'Target',	'Overs', 'Opposition', 'Ground', 'Match Date', 'Scorecard'])
# #
# answer1 = question[0].text.replace('\n',"")
# import numpy as np
# import pandas as pd
# import csv
# import requests
# from bs4 import BeautifulSoup as soup

# # data1 = requests.get("https://stats.espncricinfo.com/ci/content/records/283277.html")

# webpage = soup(data1.content, features="html.parser")
# # print((webpage.prettify()))

# list = soup.find_all('tr', class_="data1")

from bs4 import BeautifulSoup
import requests
from csv import writer

# url= "https://www.pararius.com/apartments/amsterdam?ac=1"
url = "https://stats.espncricinfo.com/ci/content/records/283277.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
# , class_="listing-search-item"
lists = soup.find_all('div', class_="div630Pad")
# lists = soup.find_all('div', class_="en")


# with open('housing.csv', 'w', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     header = ['Winner', 'Margin', 'Balls Rem', 'Target', 'Overs',
#               'Opposition', 'Ground', 'Match', 'Date', 'Scorecard']
#     # header = ['Winner']
#     thewriter.writerow(header)
with open('main_source.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Winner', 'Margin', 'Balls Rem', 'Target', 'Overs',
              'Opposition', 'Ground', 'Match', 'Date', 'Scorecard']
    # thewriter.writerow(header)
    # thewriter.writerow(info)
    thewriter.writerow(lists)

    # for list in lists:
    #     line2 = list.find('tr', class_="data1",
    #                       data_days_="733074").text.replace('\n', ',')
    #     line3 = list.find('tr', class_="data1",
    #                       data_days_="733004").text.replace('\n', ',')
    #     # line3 = list.find('tr', class_="data1",).text.replace('\n', ',')

    # # info = [winner, margin, ballsRem, target, overs,
    # #         opposition, ground, match, date, scorecard]
    # info = [line2, '\n', line3]
    # thewriter.writerow(info)

# margin = list.find(
#             'div', title="result margin").text.replace('\n', '')
#         ballsRem = list.find(
#             'span', title="balls remaining").text.replace('\n', '')
#         target = list.find(
#             'span', title="target to win").text.replace('\n', '')
#         overs = list.find('span', title="nowrap").text.replace('\n', '')
#         opposition = list.find(
#             'span', title="opposition").text.replace('\n', '')
#         ground = list.find(
#             'span', title="ground played on").text.replace('\n', '')
#         match = list.find(
#             'span', title="match start date").text.replace('\n', '')
#         date = list.find(
#             'span', title="match start date").text.replace('\n', '')
#         scorecard = list.find(
#             'span', title="match scorecard").text.replace('\n', '')
