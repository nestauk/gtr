===
gtr
===

.. image:: https://travis-ci.org/Nesta/gtr.png?branch=master
   :target: https://travis-ci.org/Nesta/gtr

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

.. todo:: Add install instructions