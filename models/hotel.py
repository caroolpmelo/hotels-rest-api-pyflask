class HotelModel:
    def __init__(self, hotel_id, name, stars, daily, city):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.daily = daily
        self.city = city

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'stars': self.stars,
            'daily': self.daily,
            'city': self.city,
        }
