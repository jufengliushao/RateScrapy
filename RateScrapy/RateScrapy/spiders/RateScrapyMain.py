import scrapy
from ..Models.RateModel import RateModel

page_total = 0
page_current = 0
zh_web_address_pre = 'http://www.boc.cn/sourcedb/whpj/index_'
rate_list = []

class RateProject(scrapy.Spider):
    name = "RateScrapy"

    start_urls = ["http://www.boc.cn/sourcedb/whpj"]

    def parse(self, response):
        """判断当前的页面"""
        global page_current
        global page_total
        global rate_list
        page_total = response.css("div[class='turn_page'] span::text").extract_first()
        """进行数据的读取"""
        data_list = response.css("div[id='DefaultMain']+table tr")
        index = 0
        for sel in data_list:
            if index == 0:
                index += 1
                continue
            ths = sel.css("td")
            values = []
            for i, tds in enumerate(ths):
                data = ths[i].css('td::text').extract()
                tmp_data = ('null' if len(data) == 0 else data[0])
                values.append(tmp_data)
            rateItem = RateModel(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7])
            index += 1
            rate_list.append(rateItem)
            print(rateItem.money_id)

        page_current = page_current + 1

        """
        if page_current <= int(page_total):
            # 继续查询下一个页面
            new_start = zh_web_address_pre + str(page_current) + '.html'
            next_url = response.urljoin(new_start)
            yield scrapy.Request(next_url, callback=self.parse)
        """