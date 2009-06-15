import unittest

from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc

from zope.component import provideUtility
# I don't like this ...
from collective.geo.settings import geoconfig
from collective.geo.settings import interfaces

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

class TestCase(ptc.PloneTestCase):
    pass

def setUp(test):
    # registering the utility 
    # usually done by componentregistry.xml
    provideUtility(
              geoconfig.GeoSettings,
              provides = interfaces.IGeoSettings
              )


def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.geo.geopoint',
            test_class=TestCase,
            setUp=setUp
            ),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
