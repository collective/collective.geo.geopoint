import unittest


from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc

from zope.component import provideUtility

from collective.geo.settings.geoconfig import GeoSettings
from collective.geo.settings.interfaces import IGeoSettings

from Products.PloneTestCase.layer import onsetup

import collective.geo.geopoint

@onsetup
def setup_product():
    """
       Set up the package and its dependencies.
    """
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml',
                     collective.geo.geopoint)
    fiveconfigure.debug_mode = False

setup_product()
ptc.setupPloneSite(products=['collective.geo.geopoint'])



def setUp(test):
    # registering the utility 
    # usually done by componentregistry.xml
    provideUtility(
              GeoSettings,
              provides = IGeoSettings
              )


class TestCase(ptc.PloneTestCase):
    pass
