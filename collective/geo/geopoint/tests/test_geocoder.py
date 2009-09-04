import unittest

from collective.geo.geopoint.tests import base

from zope.component import queryUtility
from collective.geo.geopoint.interfaces import IGeocoder
#queryUtility(IGeocoder)

class DummyContext(object):
    def __init__(self):
        pass 
    
    def getLocation(self):
        return 'Napoli Italy'


class TestGeocoder(base.TestCase):

    def afterSetUp(self):
        self.dummyContext = DummyContext()
        
    def test_utility(self):
        self.failUnless(queryUtility(IGeocoder),'IGeocoder not found')

    def test_geocoding(self):
        geocoder = queryUtility(IGeocoder)(self.dummyContext)
        self.assertEqual(geocoder.getPoint('Torino, Italy'), (45.070602899999997, 7.6867102000000003))

    def test_geocoding_from_location_attribute(self):
        geocoder = queryUtility(IGeocoder)(self.dummyContext)
        self.assertEqual(geocoder.getPoint(), (40.840096899999999, 14.2516357))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeocoder))
    return suite

