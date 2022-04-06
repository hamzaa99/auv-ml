import scrapy
from scrapping.AdopteUneVille import recupurl


class VilleidealeSpider(scrapy.Spider):
    name = "villeideale"

    def start_requests(self):
        urls = recupurl.constructurls()
        urls = urls[:20]
        urls = {}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log(f' test scrapping : {response.body}')




