import scrapy
from ..items import AmazonscraperItem
from scrapy.loader import ItemLoader

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?k=iphones&crid=WUZ3G1GCZ65K&sprefix=iphone%2Caps%2C105&ref=nb_sb_noss_2'] #url for some Iphones on amazon
    count = 0
    amount_of_pages = 4 #Enter the amount of pages you want the bot to check
    
    def parse(self, response):
        product = AmazonscraperItem()
        for products in response.css(".s-include-content-margin"):
            name = products.css(".a-color-base.a-text-normal::text").extract()
            reviews = products.css(".a-spacing-top-small .s-link-style .s-underline-text").css("::text").extract()
            price = products.css(".a-price-whole::text").extract()
            image_url = products.css(".s-image::attr(src)").extract()
            
            if name == []: #This removes the horizontal tabs of products
                continue
            product["name"] = name
            product["reviews"] = reviews
            product["price"] = price
            product["url"] = image_url
            
            yield product
            
        AmazonSpider.count += 1 #Increment the count every time a page is checked
        next_page = response.css('.s-pagination-separator').attrib['href'] #stores the link of the next page
        if (next_page is not None ) and (AmazonSpider.count < AmazonSpider.amount_of_pages):
            yield response.follow(next_page,callback=self.parse) #loop back to the loop if the new page opens
        
      
        