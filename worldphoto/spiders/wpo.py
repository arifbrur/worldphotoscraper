import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WpoSpider(CrawlSpider):
    name = 'wpo'
    start_urls = ['https://www.worldphoto.org/photographers-directory']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h2/a'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'name': response.xpath('//h1/text()').get(),
            'website': response.xpath('//div[@class="field-body"]/p/a/@href').get(),
            'note': response.xpath('(//div[@class="field-body"]/p/text())[1]').get(),
            'url': response.url
        }
