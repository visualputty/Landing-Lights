from models import VesselDetail
from dbindexer.api import register_index
register_index(VesselDetail, {'ship_name': 'istartswith'})