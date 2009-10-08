from zope.app.pagetemplate import viewpagetemplatefile

class GeopointBaseForm(object):
    template = viewpagetemplatefile.ViewPageTemplateFile('geopointform.pt')
    css_class = "geopointform"

    @property
    def geopoint_js(self):
        longitude_id = self.widgets['longitude'].id
        latitude_id = self.widgets['latitude'].id
        return "var longitude_widget_id = '%s';\nvar latitude_widget_id = '%s';" % (longitude_id, latitude_id)


class GeopointMacros(object):
    template = viewpagetemplatefile.ViewPageTemplateFile('geopointmacros.pt')

    def __getitem__(self, key):
        return self.template.macros[key]
