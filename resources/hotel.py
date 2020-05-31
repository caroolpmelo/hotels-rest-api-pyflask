from flask_restful import Resource, reqparse
from models.hotel import HotelModel


HOTELS = [
    {'hotel_id': 1, 'name': 'Alpha Hotel',
        'stars': 4.3, 'daily': 420.34, 'city': 'RJ'},
    {'hotel_id': 2, 'name': 'Bravo Hotel',
        'stars': 3.3, 'daily': 300.34, 'city': 'SP'},
    {'hotel_id': 3, 'name': 'Star Hotel',
        'stars': 5.0, 'daily': 500.81, 'city': 'REC'}
]


class Hotels(Resource):
    def get(self):
        return {'hotels': HOTELS}


class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')
    args.add_argument('stars')
    args.add_argument('daily')
    args.add_argument('city')

    def find_hotel_by_id(self, hotel_id):
        for hotel in HOTELS:
            if str(hotel['hotel_id']) == str(hotel_id):
                return hotel
        return None

    def get(self, hotel_id):
        return self.find_hotel_by_id(hotel_id) or {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        data = self.args.parse_args()
        hotel_obj = HotelModel(int(hotel_id), **data)
        updated_hotel = hotel_obj.json()
        HOTELS.append(updated_hotel)

        return updated_hotel, 200

    def put(self, hotel_id):
        data = self.args.parse_args()
        hotel_obj = HotelModel(int(hotel_id), **data)
        updated_hotel = hotel_obj.json()

        hotel = self.find_hotel_by_id(hotel_id)
        if hotel:
            hotel.update(updated_hotel)
            return updated_hotel, 200
        HOTELS.append(updated_hotel)
        return updated_hotel, 201

    def delete(self, hotel_id):
        if self.find_hotel_by_id(hotel_id):
            global HOTELS
            HOTELS = [hotel for hotel in HOTELS if str(
                hotel['hotel_id']) != str(hotel_id)]
            return {'message': 'Hotel deleted.'}, 202
        return {'message': 'Hotel not found.'}, 404
