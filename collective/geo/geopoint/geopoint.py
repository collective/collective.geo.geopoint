from zope import interface
from collective.geo.geopoint.interfaces import IGeoPoint

class GeoPoint(object):
    interface.implements(IGeoPoint)

    def __init__(self, latitude=None, longitude=None):
        self.latitude, self.longitude = latitude, longitude

    def __repr__(self):
        return "<GeoPoint with longitude=%r, latitude=%r>" % (self.longitude, self.latitude)


