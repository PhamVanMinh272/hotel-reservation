from flask import Blueprint, jsonify, request

hotels_bp = Blueprint('hotels', __name__)

# Mock data
hotels = [
    {"id": 1, "name": "Grand Hotel", "location": "New York", "roomsAvailable": 20},
    {"id": 2, "name": "Ocean View", "location": "Miami", "roomsAvailable": 15}
]

rooms = [
    {"id": 101, "hotelId": 1, "type": "Deluxe", "price": 150.00, "available": True, "maxOccupancy": 2},
    {"id": 102, "hotelId": 1, "type": "Standard", "price": 100.00, "available": True, "maxOccupancy": 2},
    {"id": 201, "hotelId": 2, "type": "Suite", "price": 200.00, "available": False, "maxOccupancy": 4}
]

# Get all hotels
@hotels_bp.route('/', methods=['GET'])
def get_hotels():
    name_filter = request.args.get('name')
    filtered_hotels = [hotel for hotel in hotels if name_filter.lower() in hotel['name'].lower()] if name_filter else hotels
    return jsonify(filtered_hotels), 200

# Get hotel by ID
@hotels_bp.route('/<int:hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotel = next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)
    if hotel:
        return jsonify(hotel), 200
    return jsonify({"error": "Hotel not found"}), 404

# Get rooms for a specific hotel
@hotels_bp.route('/<int:hotel_id>/rooms', methods=['GET'])
def get_rooms(hotel_id):
    hotel = next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)
    if not hotel:
        return jsonify({"error": "Hotel not found"}), 404
    hotel_rooms = [room for room in rooms if room['hotelId'] == hotel_id]
    return jsonify(hotel_rooms), 200

# Get a specific room in a hotel
@hotels_bp.route('/<int:hotel_id>/rooms/<int:room_id>', methods=['GET'])
def get_room(hotel_id, room_id):
    hotel = next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)
    if not hotel:
        return jsonify({"error": "Hotel not found"}), 404
    room = next((room for room in rooms if room['hotelId'] == hotel_id and room['id'] == room_id), None)
    if room:
        return jsonify(room), 200
    return jsonify({"error": "Room not found"}), 404