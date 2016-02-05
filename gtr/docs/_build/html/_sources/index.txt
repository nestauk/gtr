gtr
===

Release v\ |version|. (:ref:`Installation <install>`)

gtr provides a Python interface to the Gateway To Research `GTR-2 API
<http://gtr.rcuk.ac.uk/resources/GtR-2-API-v1.4.pdf>`_

::

    >>> import gtr
    >>> f = gtr.Funds()
    >>> r = f.fund("Fund Name")
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json'
    >>> r.json()
    {'a': 0, 'b': 1...}


User Guide
----------

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart
   user/api