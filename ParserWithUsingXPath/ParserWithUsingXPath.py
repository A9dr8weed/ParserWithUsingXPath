import csv
from lxml import etree
import lxml.html
import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)

    return response.text

def parse(api, url):
    tree = lxml.html.document_fromstring(api)
    railBioInfoItem = tree.xpath('//*[@id="two_column-4"]/div//*[@class="railBioInfoItem__label"]/text()')
    railBioLinks = tree.xpath('//*[@id="two_column-4"]/div//*[@class="railBioLinks"]/li/text()')
        
    title = tree.findtext('.//title')

    for rail in range(len(railBioInfoItem)):
        data = {"railBioInfoItem": railBioInfoItem, "railBioLinks": railBioLinks, "title": title, "url": url}
        save(data)

def save(data):
    with open("C://Users//Andrew//Desktop//text.csv", "w", newline = '') as csv_file:
        write = csv.writer(csv_file, delimiter = " ")
        write.writerow("Name: " + data["title"])
        write.writerow((data["url"], data["railBioInfoItem"], data["railBioLinks"]))

def main():
    url = 'https://www.marvel.com/characters/3-d-man-chandler'
    parse(get_html(url), url)

if __name__ == "__main__":
    main()