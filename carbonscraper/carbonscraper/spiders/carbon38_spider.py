import scrapy
from..items import CarbonscraperItem

class Carbon38SpiderSpider(scrapy.Spider):
    name = 'carbon38_spider'
    page_num=1
    # allowed_domains = ['carbon38.in']
    start_urls = [' https://carbon38.com/collections/tops?page_num=1 ']

    def parse(self, response):
        op_dict={}
        items=CarbonscraperItem()

        breadcrumbs = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "HorizontalList--spacingExtraLoose", " " ))]/text()').extract()
        image_url = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "isp_product_image", " " ))]//attr[src]()').extract()
        brand = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "isp_product_vendor", " " ))]/text()').extract()
        product_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "isp_product_title", " " ))]/text()').extract()
        price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "money", " " ))]/text()').extract()
        reviews = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "okeReviews-reviewsSummary-ratingCount", " " ))]/text()').extract()
        colour = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "isp_swatch_selected", " " ))]/text()').extract()
        sizes = response.xpath('//*[(@id = "single_facet_Size")]/text()').extract()
        description = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "Rte", " " ))]/text()').extract()
        sku = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "isp_product_sku", " " ))]/text()').extract()
        product_id = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "isp_product_id", " " ))]/text()').extract()


        items["bredcrumbs"]=breadcrumbs
        items["image_url"]=image_url
        items["brand"] = brand
        items["product_name"]=product_name
        items["price"]=price
        items["reviews"]=reviews
        items["colour"]=colour
        items["sizes"]=sizes
        items["description"]=description
        items["sku"]=sku
        items["product_id"]=product_id

        yield items
        for x in range (len(product_name)):
            try:
                temp_dict={}
                temp_dict ["bredcrumbs"]=breadcrumbs[x]
                temp_dict ["image_url"]=image_url[x]
                temp_dict ["brand"] = brand[x]
                temp_dict ['product_name']=product_name[x]
                temp_dict ["price"]=price[x]
                temp_dict ["reviews"]=reviews[x]
                temp_dict ["colour"]=colour[x]
                temp_dict ["sizes"]=sizes[x]
                temp_dict ["description"]=description[x]
                temp_dict ["sku"]=sku[x]
                temp_dict ["product_id"]=product_id[x]
                op_dict[x]=temp_dict
            except:
                pass
            print(op_dict)

            import json

            with open('output.json', 'w') as fp:
                json.dump(op_dict,fp)


        Carbon38SpiderSpider.page_num += 1
        next_url = ' https://carbon38.com/collections/tops?page_num=' + str(
            Carbon38SpiderSpider.page_num) + 'https://carbon38.com/collections/tops?page_num=15narrow=%5B%5B%22Tag%22%2C%2210%22%5D%5D'
        if True:
            yield response.follow(next_url, callback=self.parse)

