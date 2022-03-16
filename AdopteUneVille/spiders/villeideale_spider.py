import scrapy
from AdopteUneVille import recupurl

class VilleidealeSpider(scrapy.Spider):
    name = "villeideale"

    def start_requests(self):
        urls = recupurl.constructurls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
