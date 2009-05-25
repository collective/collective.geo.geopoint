================
collective.geo.geopoint
================

collective.geo.geopoint is a package to manage geographical data like a point. 

First we defined a field and not just a widget to be open to further development. Geopointschema implements the IField and it stores float values.

  >>> from plone.z3cform.tests import setup_defaults
  >>> setup_defaults()

  >>> from zope.interface.verify import verifyClass
  >>> from collective.geo.geopoint.schema import Geopointschema

  >>> from zope.schema.interfaces import IField
  >>> verifyClass(IField, Geopointschema)
  True

Geopointschema implements the IGeoPointField interface.

  >>> from collective.geo.geopoint.schema import IGeoPointField
  >>> verifyClass(IGeoPointField, Geopointschema)
  True

let's see how this widget works.
In configure.zcml we register an adapter for IGeoPointSchema and IFormLayer

  >>> import zope.component
  >>> from z3c.form import interfaces
  >>> from z3c.form.testing import TestRequest
  >>> import z3c.form.browser.text

  >>> zope.component.provideAdapter(
  ...     z3c.form.browser.text.TextFieldWidget,
  ...     adapts=(IGeoPointField, interfaces.IFormLayer),
  ... )

  >>> field = Geopointschema()
  >>> widget = zope.component.getMultiAdapter((field, TestRequest()), interfaces.IFieldWidget)
  >>> widget.id = 'latitude'
  >>> widget.update()
  >>> print widget.render()
  <input type="text" id="latitude" name=""
         class="text-widget required geopointschema-field"
         value="" />
  <BLANKLINE>

Nothing special here, we just reuse TextWidget from z3c.form
Now we verifiy the schema validation

  >>> from z3c.form import validator
  >>> from collective.geo.geopoint.interfaces import IGeoPoint
  >>> latitude_validator = validator.SimpleFieldValidator(None, None, None, IGeoPoint['latitude'], None)
  >>> latitude_validator.validate(45.112211)

If we feed a string it raising a wrongType excepetion

  >>> latitude_validator.validate('wrongType')
  Traceback (most recent call last):
  ...
  NotFloat: wrongType

So far we can use Geopointschema into z3c.form to manage geographical points.
We haved create a specific interface (IGeoPoint) and a specific template that renders a form with a web map like openstreetmaps or googlemaps.
IGeoPoint interface has two properties: latitude and longitude

  >>> from z3c.form import form, field
  >>> from collective.geo.geopoint.geopointform import GeopointBaseForm

  >>> class GeoPointForm(GeopointBaseForm, form.AddForm):
  ...     fields = field.Fields(IGeoPoint)

  >>> geoform = GeoPointForm(None, TestRequest())
  >>> geoform.update()

in this case the form also has two fields: latitude and longitude 

  >>> geoform.fields.keys()
  ['latitude', 'longitude']

and the respective widgets

  >>> geoform.widgets.keys()
  ['latitude', 'longitude']

When we render the form, the template contains a placeholder div that will contain a map.

  >>> '<div class="map" style="float: right; width: 50%">' in geoform.render()
  True
