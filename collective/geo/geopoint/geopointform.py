from zope.app.pagetemplate import viewpagetemplatefile

class GeopointBaseForm(object):
    template = viewpagetemplatefile.ViewPageTemplateFile('geopointform.pt')
    css_class = "geopointform"

    @property
    def geopoint_js(self):
        latitude_id = self.widgets['latitude'].id
        longitude_id = self.widgets['longitude'].id
        return "var latitude_widget_id = '%s';\nvar longitude_widget_id = '%s';" % (latitude_id, longitude_id)


class GeopointMacros(object):
    template = viewpagetemplatefile.ViewPageTemplateFile('geopointmacros.pt')

    def __getitem__(self, key):
        return self.template.macros[key]