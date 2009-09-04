from geopy import geocoders
from zope.interface import implements
from zope.component import getUtility

from collective.geo.settings.interfaces import IGeoSettings
from collective.geo.geopoint.interfaces  import IGeocoder


class Geocoder(object):
    implements(IGeocoder)

    def __init__(self, context):
        self.context = context
        geo_settings = getUtility(IGeoSettings)

        self.geocoder = geocoders.Google(geo_settings.googleapi)
        
    def getPoint(self, address = None):
        if not address:
            address = self.context.getLocation()

        place, (lat, lng) = self.geocoder.geocode(address)
        return (lat, lng)
