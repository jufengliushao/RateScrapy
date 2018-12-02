import scrapy
from ..DataSetting import RateHLDataIniting

class RateHL(scrapy.Spider):
    name = "RateScrapyHL"
    start_urls = ["http://www.chinamoney.com.cn/chinese/bkccpr/"] # 中国汇率网

    """
    回调
    """
    def parse(self, response):
        page_data_html = response.css("div[class='san-grid-f-m'] div").extract()
        print(len(page_data_html))
        print("success")