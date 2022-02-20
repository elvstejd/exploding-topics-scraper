from bs4 import BeautifulSoup
import requests
from models.Trend import Trend
import json
from datetime import date
import os

base_url = 'https://explodingtopics.com'

time_span = {
    '1 month': '/topics-this-month',
    '3 months': '/topics-right-now',
    '6 months': '/topics-last-6-months',
    '1 year': '/topics-this-year',
}

link = base_url + time_span['3 months']
page_response = requests.get(link, timeout=5000)
page_content = BeautifulSoup(page_response.content, "html.parser")


def scrape(page):
    trends = []
    cards_container = page.find(class_="gridInstance")

    for element in cards_container:
        if element.find(class_="proTopicTileButton"):
            continue

        name = element.find(class_="tileKeyword").get_text()
        description = element.find(class_="tileDescription").get_text()
        category = element.find(class_="typeTagInnerContainer").get_text()
        score_tags = element.find_all(class_="scoreTagItem")

        search_volume = None
        growth = score_tags[0].get_text()

        if len(score_tags) == 2:
            search_volume = score_tags[0].get_text()
            growth = score_tags[1].get_text()

        trend = Trend(
            name=name,
            description=description,
            category=category,
            search_volume=search_volume,
            growth=growth
        )

        trends.append(trend.get_dict())
    
    return trends


def main():
    all_trends = []

    # loop: scrape each page
    index = 1 # starting page
    while True:
        if index == 1:
            page_response = requests.get(link, timeout=5000)
        else:
            page_response = requests.get(link + f'?page={index}', timeout=5000)

        page_content = BeautifulSoup(page_response.content, "html.parser")

        # break loop if page doesnt exist
        if page_content.find(class_="gridInstance") == None:
            print(f'Page {index} not found. Stopped loop. ')
            break

        trends = scrape(page_content)
        all_trends += trends
        print(f'Page {index} scrapped. {len(trends)} trends found.')
        index += 1

    if not os.path.exists('output'):
        os.makedirs('output')

    # save results
    today = date.today()
    with open(f'output/trends_{today.strftime("%d-%m-%Y")}.json', 'w', encoding='utf-8') as f:
        json.dump(all_trends, f)
    print('Results file saved.')

main()
