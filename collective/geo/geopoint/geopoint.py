from zope import interface
from collective.geo.geopoint.interfaces import IGeoPoint

class GeoPoint(object):
    interface.implements(IGeoPoint)

    def __init__(self, latitude=None, longitude=None):
        self.longitude, self.latitude = longitude, latitude

    def __repr__(self):
        return "<GeoPoint with longitude=%r, latitude=%r>" % (self.longitude, self.latitude)


