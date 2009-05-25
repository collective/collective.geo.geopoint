from zope.app.pagetemplate import viewpagetemplatefile

class GeopointBaseForm(object):
    template = viewpagetemplatefile.ViewPageTemplateFile('geopointform.pt')
    css_class = "geopointform"

