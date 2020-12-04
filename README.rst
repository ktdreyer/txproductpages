Async interface to Red Hat Product Pages, using Twisted
=======================================================

.. image:: https://github.com/ktdreyer/txproductpages/workflows/tests/badge.svg
             :target: https://github.com/ktdreyer/txproductpages/actions

.. image:: https://badge.fury.io/py/txproductpages.svg
             :target: https://badge.fury.io/py/txproductpages

Access Red Hat Product Pages's REST API asyncronously (non-blocking) using the
Twisted framework.


Simple example: Fetching a release
----------------------------------

.. code-block:: python

    from txproductpages import Connection
    from twisted.internet import defer
    from twisted.internet.task import react


    @defer.inlineCallbacks
    def example(reactor):
        pp = Connection()
        # fetch a release
        try:
            release = yield pp.release('ceph-3-0')
            # release is a Munch (dict-like) object.
            print(release.name)
        except Exception as e:
            print(e)


    if __name__ == '__main__':
        react(example)


More Examples
-------------

See ``examples/`` directory

Packages that use this package
------------------------------

* `helga-productpages <https://pypi.org/project/helga-productpages/>`_
