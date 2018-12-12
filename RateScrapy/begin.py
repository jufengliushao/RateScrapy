from scrapy import cmdline
from RateScrapy.Request import RequestManager as requestM

datas = requestM.request_rmyh_hl()
print(len(datas))

# cmdline.execute("scrapy crawl RateScrapyHL".split())