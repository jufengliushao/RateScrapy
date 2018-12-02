class RateModel():
    """
    rate 类型model
    """

    # 国家对应的id
    country_id_list = {
        "阿联酋迪拉姆" : "alqmdl",
        "澳大利亚元": "adlyy",
        "巴西里亚尔": "bxlye",
        "加拿大元": "jndy",
        "瑞士法郎": "fa_lang",
        "丹麦克朗": "dmkl",
        "欧元": "ouyuan",
        "英镑": "yingbang",
        "港币": "hk_money",
        "印尼卢比": "yinnilb",
        "印度卢比": "ydlb",
        "日元": "japan_money",
        "韩国元": "hg_money",
        "澳门元": "am_money",
        "林吉特": "ljt_money",
        "挪威克朗": "nwkl_money",
        "新西兰元": "xxl_money",
        "菲律宾比索": "flb_money",
        "卢布": "russia_money",
        "沙特里亚尔": "stly_money",
        "瑞典克朗": "kl_money",
        "新加坡元": "xjp_money",
        "泰国铢": "tg_money",
        "土耳其里拉": "teq_money",
        "新台币": "xtb_money",
        "美元": "dol_money",
        "南非兰特": "nflt_money"
    }

    def __init__(self, moneyN, currency_buy_rate, cash_buy_rate, currency_sloe_rate, cash_sole_rate, zh_rate, date, time):
        # self.country_name = country                                       # 国家名字
        self.money_name = moneyN                                            # 货币名字
        self.date = date                                                    # 更新时间
        self.time = time                                                    # time
        self.currency_buy = currency_buy_rate                               # 现汇的买入价
        self.currency_sole = currency_sloe_rate                             # 现汇卖出价
        self.cash_buy = cash_buy_rate                                       # 现钞买入价
        self.cash_sole = cash_sole_rate                                     # 现钞卖出价
        self.money_id = ""                                                  # 货币id

        self.zh_rate = zh_rate                                              # 中行结算价

        self.rate_country_id()                                              # 设置对应的id

    # 设置country id
    def rate_country_id(self):
        country_id_list = {
            "阿联酋迪拉姆": "alqmdl",
            "澳大利亚元": "adlyy",
            "巴西里亚尔": "bxlye",
            "加拿大元": "jndy",
            "瑞士法郎": "fa_lang",
            "丹麦克朗": "dmkl",
            "欧元": "ouyuan",
            "英镑": "yingbang",
            "港币": "hk_money",
            "印尼卢比": "yinnilb",
            "印度卢比": "ydlb",
            "日元": "japan_money",
            "韩国元": "hg_money",
            "澳门元": "am_money",
            "林吉特": "ljt_money",
            "挪威克朗": "nwkl_money",
            "新西兰元": "xxl_money",
            "菲律宾比索": "flb_money",
            "卢布": "russia_money",
            "沙特里亚尔": "stly_money",
            "瑞典克朗": "kl_money",
            "新加坡元": "xjp_money",
            "泰国铢": "tg_money",
            "土耳其里拉": "teq_money",
            "新台币": "xtb_money",
            "美元": "dol_money",
            "南非兰特": "nflt_money"
        }
        if self.money_name in country_id_list.keys():
            self.money_id = country_id_list[self.money_name]
        else:
            self.money_id = self.money_name