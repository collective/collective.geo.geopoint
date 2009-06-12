from zope import schema
from collective.geo.geopoint import GeopointMessageFactory as _
from zope import interface
from zope.schema.interfaces import IField, IMinMax
from zope.schema.interfaces import IFromUnicode
from zope.schema._bootstrapfields import Field, Orderable


class NotFloat(schema.ValidationError): 
    __doc__ = _("""Value must be a float ex. 1.111111""")


class IGeoPointField(IMinMax, IField):
    """ geopoint field """

class Geopointschema(Orderable, Field):
    __doc__ = IGeoPointField.__doc__
    interface.implements(IGeoPointField, IFromUnicode)
    _type = float

    def __init__(self, *args, **kw):
        super(Geopointschema, self).__init__(*args, **kw)

    def fromUnicode(self, u):
        """
        >>> f = Float()
        >>> f.fromUnicode("1.25")
        1.25
        >>> f.fromUnicode("1.25.6")
        Traceback (most recent call last):
        ...
        ValueError: invalid literal for float(): 1.25.6
        """
        v = float(u)
        self.validate(v)
        return v

    def validate(self,value):
        try:
            float(value)
        except:
            raise NotFloat(value)
        super(Geopointschema, self).validate(value)

