class Experiment:
    def __init__(self, exp_id, temperature, pressure, catalyst, yield_rate, id=None):
        self.id = id
        self.exp_id = exp_id            # 实验编号
        self.temperature = temperature  # 温度 (℃)
        self.pressure = pressure        # 压力 (MPa)
        self.catalyst = catalyst        # 催化剂名称
        self.yield_rate = yield_rate    # 收率 (%)

    def __str__(self):
        return f"实验[{self.exp_id}] 温度:{self.temperature}℃ 压力:{self.pressure}MPa 催化剂:{self.catalyst} 收率:{self.yield_rate}%"