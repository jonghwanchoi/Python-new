class Rest:
    def __init__(self, stdRestNm, itemNm , detail):
        self.stdRestNm = stdRestNm
        self.itemNm= itemNm
        self.detail = detail
    def __str__(self):
        return f"stdRestNm : '{self.stdRestNm}' itemNm : '{self.itemNm}' detail : '{self.detail}'"

