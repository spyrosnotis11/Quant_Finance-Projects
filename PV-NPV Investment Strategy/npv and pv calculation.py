import numpy as np
class short_rate:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def get_discount_factors(self, time_list):
        time_list = np.array(time_list)
        return np.exp(-self.rate * time_list)


class Strategy(short_rate):
    def __init__(self, cash_flow, rate, name, time_list):
        super().__init__(name, rate)
        self.cash_flow = cash_flow
        self.time_list = time_list
        self.disc_f = self.get_discount_factors(self.time_list).tolist()
        self.pv = []
        self.npv = 0

# PV= CF*discount_factor
# NPV= PV1+PV2+...+PVN

    def calculate_pv(self):
        for i in range(len(self.time_list)):
            self.pv.append(self.cash_flow[i] * self.disc_f[i])

    def calculate_npv(self):
        for i in range(len(self.pv)):
            self.npv = self.npv + self.pv[i]


time_list = [0, 0.5, 1.0, 1.5, 2.0,2.5]  # time list example
diff_rates = [0.02, 0.04, 0.06, 0.03, 0.05,0.07]  # rates example
cash_flow = [-1000, 500, 600, -250, 288,255]  # cash flows example
strategy_1 = Strategy(cash_flow, 0.05, 'r', time_list)
strategy_1.calculate_pv()
print(strategy_1.pv)
strategy_1.calculate_npv()
print(f'The Net Present Value of this investment is:{strategy_1.npv}')
if strategy_1.npv > 0:
    print('The current investment project should be considered')
else:
    print('Negative NPV: This investment project may generate losses')


class DifferentStrategy(Strategy):
    def __init__(self, cash_flow, rates, name, time_list):
        
        rate=rates[0]
        self.rates=rates
        self.discfactor=[]
        super().__init__(cash_flow, rate, name, time_list)

    def diff_DF(self):
        for i in range(len(self.time_list)):
            self.rate=self.rates[i]
            x=self.time_list[i]
            self.discfactor.append(self.get_discount_factors(x))

ds = DifferentStrategy(cash_flow, diff_rates, 'r', time_list)
ds.diff_DF()
print(ds.discfactor)
ds.calculate_pv()
print(ds.pv)
ds.calculate_npv()
print(f' This investment project with different discount factors has Net Present Value: {ds.npv}')

