import scrapy

class RateProject(scrapy.Spider):
    name = "RateScrapy"

    start_urls = ["http://www.boc.cn/sourcedb/whpj"]

    def parse(self, response):
        data_list = response.css("div[id='DefaultMain']+table tr")
        print("success")