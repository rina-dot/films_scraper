import requests
from scrapy import Selector
import csv

csv_file = csv.writer(open('kinogo.csv', 'w'))


for page in range(1, 5):
    print(page)
    response = requests.get(f"https://kinogo.by/film/premie/page/{page}/")
    selector = Selector(response=response)

    all_films = selector.xpath('//div[contains(@class, "shortstory shid")]')

    for film in all_films:
        title = film.xpath('.//h2/a/text()').extract_first()
        rating_imdb = film.xpath('.//div[@class="r-imdb"]/text()').extract_first()
        print(title, rating_imdb)
        csv_file.writerow([title, rating_imdb])
