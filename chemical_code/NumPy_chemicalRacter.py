class ChemicalReactor:
    def __init__(self, name, volume, temperature):
        self.name = name
        self.volume = volume
        self.temperature = temperature

    def calculate_ideal_pressure(self, moles):
        R = 0.08206
        return (moles * R * self.temperature) / self.volume
    def calculate_vdw_pressure(self, moles, a, b):
        R = 0.08206
        # P = (nRT)/(V-nb) - (an^2)/(V^2)
        term1 = (moles * R * self.temperature) / (self.volume - moles * b)
        term2 = (a * (moles ** 2)) / (self.volume ** 2)
        return term1 - term2


if __name__ == "__main__":
    reactor_A = ChemicalReactor("一号反应器", volume=10.0, temperature=300.0)
    
    # CO2的范德华常数
    a = 3.592
    b = 0.04267
    
    ideal_P = reactor_A.calculate_ideal_pressure(moles=2.0)
    vdw_P = reactor_A.calculate_vdw_pressure(moles=2.0, a=a, b=b)
    
    print(f"理想气体压力: {ideal_P:.4f} atm")
    print(f"范德华方程压力: {vdw_P:.4f} atm")


    