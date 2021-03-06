from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Listing
import os

map_routes = Blueprint('map', __name__)


@map_routes.route('/key', methods=['POST'])
@login_required
def load_map_key():
    key = os.environ.get('MAPS_API_KEY')
    return {'googleMapsAPIKey': key}


@map_routes.route('/<string:address>')
@login_required
def get_places(address):
    print(address, '@@@@@@@@@@')
    parsed_city = address[:-9]
    print(parsed_city)
    if ',' in parsed_city:
        i = parsed_city.index(',')
        parsed_city = parsed_city[i+2:]
    print('!!!!!!!!!!!!!!!!!!', parsed_city, '!!!!!!!!!!!!!!!!!!')
    places = Listing.query.filter(Listing.city == parsed_city).all()
    print([place.to_dict() for place in places], places)
    return {'places': [place.to_dict() for place in places]}
