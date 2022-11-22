class Airport:
    def __init__(self, airport_id, location, city,  country, code, lat, long, curr):
        self.airport_id = airport_id
        self.location = location
        self.city = city
        self.country = country
        self.code = code
        self.latitude = lat
        self.longitude = long
        self.currency = curr

    def __repr__(self):
        return f''' airport_id = {self.airport_id} location = {self.location} city = {self.city} country = {self.country} code = {self.code} latitude = {self.latitude} longitude = {self.longitude} currency = {self.currency}
         '''
