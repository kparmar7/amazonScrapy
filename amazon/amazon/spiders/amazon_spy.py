import scrapy
from ..items import AmazonItem

class AmazonSpySpider(scrapy.Spider):
    name = 'amazon_spy'
    #allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1612711929&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0']
    def parse(self, response):
        items = AmazonItem()
        #name = response.css(".a-color-base.a-text-normal").css("::text")[0].extract() #TESTING
        name = response.css(".a-color-base.a-text-normal").css("::text").extract()
        author = response.css(".sg-col-12-of-20 .sg-col-12-of-20 .a-size-base+ .a-size-base").css("::text").extract() 
        price = response.css(".a-spacing-top-small .a-price-whole").css("::text").extract() 
        link = response.css(".s-image-fixed-height img::attr(src)").extract() 

        items["name"] = name
        items["author"] = author
        items["price"] = price
        items["link"] = link

        yield items