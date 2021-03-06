A Red Hat Product Pages plugin for helga chat bot
=================================================

.. image:: https://github.com/ktdreyer/helga-productpages/workflows/tests/badge.svg
             :target: https://github.com/ktdreyer/helga-productpages/actions

.. image:: https://badge.fury.io/py/helga-productpages.svg
          :target: https://badge.fury.io/py/helga-productpages

About
-----

Helga is a Python chat bot. Full documentation can be found at
http://helga.readthedocs.org.

This Product Pages plugin allows Helga to respond to product commands in IRC
and print information about releases. For example::

  03:14 < ktdreyer> helgabot: rhcs 3.0 date
  03:14 < helgabot> ktdreyer, Red Hat Ceph Storage 3.0 ga is on Tue Dec 5,
                    2017 (14 business days from today)

Or specific milestones, like "z2" or "beta"::

  03:14 < ktdreyer> helgabot: osp 12 beta date
  03:14 < helgabot> ktdreyer, Red Hat OpenStack Platform 12 beta is on Wed Nov
                    8, 2017 (50 business from today)

The bot can also provide the link to the full schedule for a release::

  03:14 < ktdreyer> helgabot: osp 12 schedule
  03:14 < helgabot> Red Hat OpenStack Platform 12 schedule:
                    https://pp.engineering.redhat.com/pp/product/rhosp/release/rhosp-12.0/schedule/tasks

(Obviously this bot plugin requires network access to
https://pp.engineering.redhat.com.)

Installation
------------
This Product Pages plugin is `available from PyPI
<https://pypi.python.org/pypi/helga-productpages>`_, so you can simply install
it with ``pip``::

  pip install helga-productpages

If you want to hack on the helga-productpages source code, in your virtualenv
where you are running Helga, clone a copy of this repository from GitHub and
run
``python setup.py develop``.


Optional: Default product configuration
---------------------------------------

In your ``settings.py`` file (or whatever you pass to ``helga --settings``),
you can specify a ``DEFAULT_PRODUCT``. For example::

  DEFAULT_PRODUCT = 'ceph'

If you omit the product when asking Helga for release dates, Helga will use
this product value.


Security
--------

**Note**: This plugin can expose private information (milestone dates) about
Red Hat products. If you use this plugin, be sure that the networks to which
Helga connects are restricted. Everyone in Helga's channels will see the
private information, so the assumption is that they already have rights to
read the data on Product Pages.
