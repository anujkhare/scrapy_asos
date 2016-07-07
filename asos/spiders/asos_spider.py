from scrapy.spider import BaseSpider
from scrapy.selector import *

from asos.items import AsosItem

class AsosSpider(BaseSpider):
    name = "asos"
    allowed_domains = ["asos.com"]
    start_urls = [
        "http://www.asos.com/women/a-to-z-of-brands/asos-collection/cat/?cid=4877&refine=attribute_900:1459&currentpricerange=0-270&pgesize=204"
    ]

    def parse(self, response):
        filename = 'asos_response'

        # create a selector
        hxs = HtmlXPathSelector(response)

        # select all list element nodes (li) in ul node, which have the attribute
        # 'data-productid', which is present only in the relevant nodes
        ul = hxs.select("//ul/li[@data-productid]")

        ind = -6
        items = []

        for li in ul:
            item = AsosItem()

            # names are in a span of class "name"
            item['name'] = li.select(".//span[@class='name']/text()").extract()
            l = item['name']
            print (type(l))
            print (len(l))
            print (l[0])

            # price
            item['price_orig'] = li.select(".//div[@class='price-wrap price-previous']/span[@class='price']/text()").extract()
            item['price_cur']  = li.select(".//div[@class='price-wrap price-current']/span[@class='price']/text()").extract()

            # find the 'img' tag relative the 'li', and extract it's source attribute
            item['image_url_small'] = li.select(".//img/@src").extract()

            # the large image urls just have an extra 'x' in the url near the end
            item['image_url_large'] = map(lambda x: x[:ind] + 'x' + x[ind:], item['image_url_small'])
            # item['image_url_large'] = item['image_url_small'][0][:ind] + 'x' + item['image_url_small'][0][ind:]

            items.append(item)

            # print (item['name'])
            # print (item['price_orig'])
            # print (item['price_cur'])
            # print (item['image_url_large'])
            # print (item['image_url_small'])
            # print ('\n\n')

        return items
