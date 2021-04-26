import scrapy
import os

basedir = os.path.dirname(os.path.realpath('__file__'))


class CellPhonesSpider(scrapy.Spider):
    name = 'cellphones'
    base_url = 'https://cellphones.com.vn/mobile.html?p=%s'
    start_urls = [base_url % 1]
    download_delay = 5

    def parse(self, response):
        self.log('Visited ' + response.url)

        products = response.css('.products-container .cols-5 .cate-pro-short')

        self.log('products ' + str(len(products)))
        for product in products:
            item = {
                'title': product.css('a > #product_link::text').get(),
                'image_url': product.css('.lt-product-group-image a > img::attr(src)').get(),
                'price': product.css('.lt-product-group-info .price-box .special-price .price::text').get(),
                'old_price': product.css('.lt-product-group-info .old-price .price::text').get()
            }
            yield item

        #
        #
        # next_page_url = response.css('div.row.searchPagination > div > nav > ul > li:nth-child(2) a::attr(href)').extract_first()
        # next_page_url = response.urljoin(next_page_url)
        # yield scrapy.Request(url=next_page_url, callback=self.parse)
