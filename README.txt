Introduction
============

collective.geo.geopoint provides some generic classes for collective.geo.* packages.


Requirements
------------
* plone >= 3.2.1
* plone.app.z3cform
* collective.geo.openlayers
* collective.geo.settings

Installation
============
Just a simple easy_install collective.geo.geopoint is enough.

Alternatively, buildout users can install collective.geo.geopoint as part of a specific project's buildout, by having a buildout configuration such as: ::

        [buildout]
        ...
        eggs = 
            zope.i18n>=3.4
            collective.geo.geopoint
        ...
        [instance]
        ...
        zcml = 
            collective.geo.geopoint


Contributors
============

* Giorgio Borelli - gborelli
* Silvio Tomatis - silviot

