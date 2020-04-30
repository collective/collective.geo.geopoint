Introduction
============

collective.geo.geopoint provides some generic classes for collective.geo.* packages.


Requirements
------------
* plone >= 3.2.1
* plone.app.z3cform
* collective.geo.openlayers
* collective.geo.settings


Documentation
=============

Full documentation for end users can be found in the "docs" folder.
It is also available online at https://collectivegeo.readthedocs.io/


Translations
============

This product has been translated into

- Dutch.

- Spanish.

- Italian.

You can contribute for any message missing or other new languages, join us at 
`Plone Collective Team <https://www.transifex.com/plone/plone-collective/>`_ 
into *Transifex.net* service with all world Plone translators community.


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


Tests status
============

This add-on is tested using Travis CI. The current status of the add-on is:

.. image:: https://img.shields.io/travis/collective/collective.geo.geopoint/master.svg
    :target: https://travis-ci.org/collective/collective.geo.geopoint

.. image:: http://img.shields.io/pypi/v/collective.geo.geopoint.svg
   :target: https://pypi.org/project/collective.geo.geopoint


Contribute
==========

Have an idea? Found a bug? Let us know by `opening a ticket`_.

- Issue Tracker: https://github.com/collective/collective.geo.geopoint/issues
- Source Code: https://github.com/collective/collective.geo.geopoint
- Documentation: https://collectivegeo.readthedocs.io/


Contributors
============

* Giorgio Borelli - gborelli
* Silvio Tomatis - silviot
* David Breitkreutz - rockdj
* Leonardo J. Caballero G. - macagua


License
=======

The project is licensed under the GPL.

.. _`opening a ticket`: https://github.com/collective/collective.geo.bundle/issues
