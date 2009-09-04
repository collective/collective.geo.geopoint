import unittest

from Testing import ZopeTestCase as ztc

from collective.geo.geopoint.tests import base


def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.geo.geopoint',
            test_class=base.TestCase,
            setUp=base.setUp
            ),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
