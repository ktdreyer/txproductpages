from munch import unmunchify
from txproductpages import Connection
from txproductpages.exceptions import ProductPagesException
from twisted.internet import defer
from twisted.internet.task import react
from pprint import pprint

# Print the upcoming releases for the RH Ceph Storage product.


@defer.inlineCallbacks
def example(reactor):
    pp = Connection()

    try:
        result = yield pp.upcoming_releases('ceph')
        pprint(unmunchify(result))
        for release in result:
            url = pp.schedule_url(release.shortname)
            print(url)
    except ProductPagesException as e:
        print(e)


if __name__ == '__main__':
    react(example)
