import os
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem


class PItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()


class MeizituSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["meizitu.com"]
    start_urls = (
        'http://meizitu.com/a/list_1_1.html',
    )

    def parse(self, response):
        exp = u'//div[@id="wp_page_numbers"]//a[text()="下一页"]/@href'
        _next = response.xpath(exp).extract_first()
        next_page = os.path.join(os.path.dirname(response.url), _next)
        yield scrapy.FormRequest(next_page, callback=self.parse)
        for p in response.xpath('//li[@class="wp-item"]//a/@href').extract():
            yield scrapy.FormRequest(p, callback=self.parse_item)

    def parse_item(self, response):
        item = PItem()
        urls = response.xpath("//div[@id='picture']//img/@src").extract()
        name = response.xpath("//div[@id='picture']//img/@alt").extract()[0]
        item['image_urls'] = urls
        item['name'] = name.split(u'，')[0]
        return item


class MztImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})
            # 这里把item传过去，因为后面需要用item里面的书名和章节作为文件名

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0[name]}/{1}'.format(item, image_guid)
        return filename
