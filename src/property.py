class Property():
    def __init__(self, uprn, epc_rating, epc_score, address_line_one, postcode):
        self.uprn = uprn
        self.epc_rating = epc_rating
        self.epc_score = epc_score
        self.address = f'{address_line_one}, {postcode}'