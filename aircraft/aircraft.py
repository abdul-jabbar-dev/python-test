class Aircraft:
    def __init__(self, company, model, air_type, flight_range):
        self.company = company
        self.model = model
        self.air_type = air_type
        self.flight_range = flight_range

    def __repr__(self):
        return f'company_name:{ self.company}, air_model:{ self.model},  air_type: {self.air_type}, flight_range: {self.flight_range}'
        # return [self.company,self.model]


B812 = Aircraft('AirBurn', 'Air B812', 'Passenger', 450)
print(B812)
