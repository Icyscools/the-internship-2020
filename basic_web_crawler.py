"""
Basic Web Crawler
Author: Woramat Ngamkham
"""

import requests
from bs4 import BeautifulSoup


def sorting_partner(partner):
    return len(partner['description'])


if __name__ == "__main__":
    r = requests.get("https://theinternship.io/")

    soup = BeautifulSoup(r.content, 'html.parser')
    partner_crawler = soup.select('.partner')
    partner = {"companies": []}

    for i in partner_crawler:
        logo = i.select_one('.logo-box > a > img')['src']
        description = i.select_one('.box-textbox > span').text
        _partner = {
            "logo": logo,
            "description": description
        }
        partner["companies"].append(_partner)

    partner["companies"].sort(key=sorting_partner)
    for companie in partner["companies"]:
        print(companie['logo'])
