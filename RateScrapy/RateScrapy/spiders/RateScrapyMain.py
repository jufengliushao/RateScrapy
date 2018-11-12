import scrapy
from ..Models.RateModel import RateModel

class RateProject(scrapy.Spider):
    name = "RateScrapy"

    start_urls = ["http://www.boc.cn/sourcedb/whpj"]

    def parse(self, response):
        data_list = response.css("div[id='DefaultMain']+table tr")
        index = 0
        rate_values = []
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
            print(rateItem)
            index += 1
            rate_values.append(rateItem)
        print("success")