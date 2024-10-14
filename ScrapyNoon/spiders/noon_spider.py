import scrapy
from ..items import ScrapynoonItem
import datetime as dt

class NoonSpiderSpider(scrapy.Spider):
    name = "noon_spider"
    page_number = 2
    start_urls = ["https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page=1&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"]

    def parse(self, response):
        items = ScrapynoonItem()
        all_div_items = response.css('.bwele')

        for div in all_div_items:

            Name = div.css(".fPskJH::attr('title')").extract()
            #Brand = div.css(".fPskJH > span > span > span:nth-child(1)::text").extract()
            Brand = []
            for name in Name:
                    Brand.append(name.split()[0])

            Sponsered = "Y" if div.css('.AkmCS::text').extract() else ""
        #Sponsored = []
        #for spons in Sponsored_all:
        #    if spons is not None:
        #        Sponsored.append('Y')
        #    else:
        #        Sponsored.append("N")
            Rating = div.css('.dGLdNc::text').extract()
            Rating_count = div.css('.gBbbhg span::text').extract()
            Expressed =  div.css('.hnMlkQ::attr(alt)').extract()
            Express = []
            for Ex in Expressed:
                if Ex == 'noon-express':
                    Express.append('Y')
            Price = div.css('.amount::text').extract()
            OldPrice = "".join(div.css('.cnynyB .oldPrice::text').extract())
            Sale_price = OldPrice.strip() 
            Get_It_BY = div.css('b::text').extract()
            Links = div.css('.bwele a::attr("href")').extract()
            Link = ["https://www.noon.com/"+i for i in Links]
            Date = dt.date.today()

            items['Date'] = str(Date)
            items['Get_It_BY'] = Get_It_BY
            items['Name'] = Name
            items['Brand'] = Brand
            items['Average_Rating'] = Rating
            items['Rating_count'] = Rating_count
            items['Sponsered'] = Sponsered
            items['Price'] = Price
            items['Sale_price'] = OldPrice
            items['Express'] = Express
            items['Link'] = Link


        #yield {'Date':Date,'Name':Name,'Brand':Brand, 'Sponserd':Sponsored, 'Rating':Rating, 'Rating_count':Rating_count, 'Expressed':Express, 'Price':Price, 'OldPrice':OldPrice, 'Link':Link}
            yield items

        #this is for next page data
        next_page = "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page="+str(NoonSpiderSpider.page_number)+"&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"

        #if you want more data you can increase the condition value,
        # i want only greater then 200 and less then 300 that's why take condition is <= 4
        if NoonSpiderSpider.page_number <= 4:
            NoonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
            