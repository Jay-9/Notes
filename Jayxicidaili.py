# -*- coding: utf-8 -*-
import scrapy


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nt/']
    # start_urls = [f'https://www.xicidaili.com/nt/{page}'for page in range(1,10)]

    # custom_settings = None # 反爬

    def parse(self, response):        
        selectors = response.xpath('//tr')
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()
            port = selector.xpath('./td[3]/text()').extract_first()
            print(ip, port)
            items = {
                'ip': ip,
                'port': port
                }
            yield items

        next_page = response.xpath('//a[@class="next_page"]/@href').get()
        if next_page:
            print(next_page)
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)
