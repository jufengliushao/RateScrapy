class RateModel():
    """
    rate 类型model
    """

    def __init__(self, moneyN, currency_buy_rate, cash_buy_rate, currency_sloe_rate, cash_sole_rate, zh_rate, date, time):
        # self.country_name = country                                       # 国家名字
        self.money_name = moneyN                                            # 货币名字
        self.date = date                                                    # 更新时间
        self.time = time                                                    # time
        self.currency_buy = currency_buy_rate                               # 现汇的买入价
        self.currency_sole = currency_sloe_rate                             # 现汇卖出价
        self.cash_buy = cash_buy_rate                                       # 现钞买入价
        self.cash_sole = cash_sole_rate                                     # 现钞卖出价
        self.zh_rate = zh_rate                                              # 中行结算价
