from zope.interface import Interface
from collective.geo.geopoint.schema import Geopointschema
from zope import schema
from collective.geo.geopoint import GeopointMessageFactory as _

class IGeoPoint(Interface):
    longitude = Geopointschema(title=_(u'Longitude'),
                                         description=_(u"Enter the Longitude"),
                                         default=None,
                                         required=True)

    latitude  = Geopointschema(title=_(u'Latitude'),
                                         description=_(u"Enter the Latitude"),
                                         default=None,
                                         required=True)

