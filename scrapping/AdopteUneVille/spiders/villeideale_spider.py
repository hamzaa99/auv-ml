import scrapy
from scrapy import Selector

from AdopteUneVille import recupurl

class VilleidealeSpider(scrapy.Spider):
    name = "villeideale"

    def start_requests(self):
        urls = recupurl.constructurls()
        #urls = ['https://www.ville-ideale.fr/aix-les-bains_73008',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        infos = response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[2]').extract()
        self.log(infos)
        yield {
            'Nom' : response.request.url,
            'Environnement': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[1]/td/text()').extract_first(),
            'Transports' : response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[2]/td/text()').extract_first(),
            'Sécurité': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[3]/td/text()').extract_first(),
            'Santé': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[4]/td/text()').extract_first(),
            'SportsEtLoisirs': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[5]/td/text()').extract_first(),
            'Culture': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[6]/td/text()').extract_first(),
            'Enseignement': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[4]/td/text()').extract_first(),
            'Commerce': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[4]/td/text()').extract_first(),
            'QualiteDeVie': response.xpath('/html/body/div/div/table[@id="tablonotes"]/tr[4]/td/text()').extract_first(),
        }


