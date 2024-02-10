import scrapy

class SpezieSpider(scrapy.Spider):
    name = 'spezie_spider'
    start_urls = ['https://www.lennesimoblogdicucina.com/']

    def parse(self, response):
        # Estrai i titoli delle ricette
        recipe_titles = response.css('h1.entry-title a::text').extract()

        # Stampa i titoli estratti
        for title in recipe_titles:
            self.log(f'Title: {title}')

  # Salva i titoli in un file JSON
        json_file_path = 'titles.json'
        with open(json_file_path, 'w') as json_file:
            json.dump({'titles': titles}, json_file)

        # Salva i titoli in un file CSV
        csv_file_path = 'titles.csv'
        with open(csv_file_path, 'w') as csv_file:
            csv_file.write('Title\n')
            for title in titles:
                csv_file.write(f'{title}\n')