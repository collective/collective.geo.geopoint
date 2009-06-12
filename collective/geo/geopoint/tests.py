import unittest

from zope.testing import doctestunit, doctest, renormalizing
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

from zope.component import provideUtility
# I don't like this ...
from collective.geo.settings import geoconfig 
from collective.geo.settings import interfaces

ptc.setupPloneSite()

import collective.geo.geopoint

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             collective.geo.geopoint)
            fiveconfigure.debug_mode = False
        @classmethod
        def tearDown(cls):
            pass

def setUp(test):
    # registrazione della mia utility .. componentregistry.xml
    provideUtility(
              geoconfig.GeoSettings, 
              provides = interfaces.IGeoSettings
              )


def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.geo.geopoint',
            test_class=ptc.PloneTestCase,
            setUp=setUp 
            ),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
