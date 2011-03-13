from models import VesselDetail, Passage
from dbindexer.api import register_index
register_index(VesselDetail, {'ship_name': 'istartswith'})
register_index(Passage, {'ship_name': 'icontains'})
#register_index(Passage, {'date_added': 'day'})
#register_index(Passage, {'date_added': 'month'})
#register_index(Passage, {'date_added': 'year'})