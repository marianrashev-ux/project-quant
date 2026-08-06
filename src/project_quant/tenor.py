class Tenor:
    def __init__(self, tenor: str):
        if not tenor:
            raise ValueError("Tenor cannot be empty.")
        if int(tenor[:-1]) <= 0:
            raise ValueError("Tenor value must be positive.")
        if tenor[-1] not in ["D", "W", "M", "Y"]:
            raise ValueError("Tenor must end with 'D', 'W', 'M', or 'Y'.")
        self.tenor = tenor
    def __str__(self):
        return str(self.tenor)
    def unit(self):
        return self.tenor[-1]
    def length(self):
        return int(self.tenor[:-1])
    def years(self):
        days = {
                    "D": 1,
                    "W": 7,
                    "M": 30,
                    "Y": 360
                }
        return self.length() * days[self.unit()] / 360
    