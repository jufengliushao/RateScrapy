
class HLModel():
    """
    从中国银行的汇率获取的数据
    """
    def __init__(self, approvedTime, approvedTimeEn, bannerCss, bannerPic, bp, bpDouble, foreignCName, price, vrtCode, vrtEName, vrtName):
            self.approvedTime = approvedTime
            self.approvedTimeEn = approvedTimeEn
            self.bannerCss = bannerCss
            self.bannerPic = bannerPic # 图片后缀
            self.bp = bp # 相比上涨还是下降 + 上涨 - 下降
            self.bpDouble = bpDouble # 同上
            self.foreignCName = foreignCName # 货币英文缩写
            self.price = price # 对应的汇率
            self.vrtCode = vrtCode
            self.vrtEName = vrtName # 对应的是rmb转换成外币，还是外币转换成人民币
            self.vrtName = vrtName # 上述对应的中文名