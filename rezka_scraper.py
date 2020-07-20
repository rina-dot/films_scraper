import requests
from scrapy import Selector
import csv

csv_file = csv.writer(open('rezka_scraper.csv', 'w'))

for page in range(1, 5):
    print(page)
    response = requests.get(f'https://rezka.ag/films/best/page/{page}/')
    page = Selector(response=response)

    all_films = page.xpath('//div[contains(@class, "b-content__inline_item")]')

    for film in all_films:

       title = film.xpath('.//div[2]/a/text()').extract_first()
       year = film.xpath('.//div/div/text()').extract_first()
       if title is None:
           continue
       print(title, year)
       csv_file.writerow([title, year])
