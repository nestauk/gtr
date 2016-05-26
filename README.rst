===
gtr
===

.. image:: https://travis-ci.org/nestauk/gtr.png?branch=master
   :target: https://travis-ci.org/nestauk/gtr

.. image:: https://coveralls.io/repos/Nesta/gtr/badge.svg?branch=master&service=github
    :target https://coveralls.io/r/Nesta/gtr

A Python interface to the Gateway To Research `GTR-2 API <http://gtr.rcuk.ac.uk/resources/GtR-2-API-v1.4.pdf>`_.
Returns `requests.Response objects <http://docs.python-requests.org/en/latest/api/#requests.Response>`_.

Services
========

- **Funds** `examples <./docs/funds.md#funds>`__, `api <http://gtr.rcuk.ac.uk/gtr/api/fund>`__

  - Retrieve a fund by fund id
  - Search for funds by

    - Funded project title
    - Fund amount
    - Funder organisation name
    - Fund type
|
- **Projects** `examples <./docs/projects.md#projects>`__, `api <http://gtr.rcuk.ac.uk/gtr/api/projects>`__

  - Retrieve project by project reference
  - Search for projects by

    - Project title
    - Project Abstract
|
- **Organisation** `examples <./docs/organisations.md#organisations>`__, `api <http://gtr.rcuk.ac.uk/gtr/api/organisations>`__

  - Retrieve organisation by organisation reference
  - Search for organisations by

    - Organisation name
    - Project title
    - Project abstracts
|
- **Persons** `examples <./docs/persons.md#persons>`__, `api <http://gtr.rcuk.ac.uk/gtr/api/persons>`__

  - Search for persons by:

    - First name
    - Family name
    - Other name
    - Organisation name
    - Project titles
    - Project abstracts
|
- **Outcomes** `examples <./docs/outcome.md#outcome>`__, `api <http://gtr.rcuk.ac.uk/gtr/api/outcome>`__

  - Search for organisations by:

    - Organisation name
    - Project title
    - Project abstracts

Installation
============

Get the Code
------------

gtr is available on `GitHub <https://github.com/nestauk/gtr>`_.

You can either clone the public repository::

    $ git clone git://github.com/nestauk/gtr.git

Download the `tarball <https://github.com/jamesgardiner/nestauk/tarball/master>`_::

    $ curl -OL https://github.com/nestauk/gtr/tarball/master

Or, download the `zipball <https://github.com/jamesgardiner/nestauk/zipball/master>`_::

    $ curl -OL https://github.com/nestauk/gtr/zipball/master


Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily::

    $ python setup.py install
