import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://quotes.toscrape.com/']
    
    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
        