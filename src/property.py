class Property():
    def __init__(self, uprn):
        self.uprn = uprn
        self.epc_rating = ''
        self.epc_score = ''
        self.address = ''
        self.age = 0
        self.connectivity = ''
        self.material = ''

    def calculate_score(self):
        score = 0
        age_is_int = type(self.age) is int
        if not age_is_int:
            self.age = int(self.age[-4:])
    
        if self.connectivity == "Standalone":
            score += 1
        if self.material != "Brick Or Block Or Stone" and self.material != "" and self.material != 'Concrete':
            score += 1
        if self.epc_rating > "C":
            score += 1
        if self.age < 1960 and self.age > 0:
            score += 1
        return score