from munch import unmunchify
from txproductpages import Connection
from txproductpages.exceptions import ProductPagesException
from twisted.internet import defer, reactor
from pprint import pprint

# Print the upcoming releases for the RH Ceph Storage product.


@defer.inlineCallbacks
def example():
    pp = Connection()

    try:
        result = yield pp.upcoming_releases('ceph')
        pprint(unmunchify(result))
    except ProductPagesException as e:
        print(e)


if __name__ == '__main__':
    example().addCallback(lambda ign: reactor.stop())
    reactor.run()
