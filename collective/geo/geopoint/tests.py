import unittest

from zope.testing import doctestunit, doctest, renormalizing
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
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


def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.geo.geopoint',
            test_class=ptc.PloneTestCase,
            ),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
