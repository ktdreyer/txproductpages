from datetime import date
from txproductpages import Connection
from txproductpages.exceptions import ProductPagesException
from txproductpages import milestones
from twisted.internet import defer
from twisted.internet.task import react
from pprint import pprint

# Print the development freeze date for the RH Ceph Storage 3.0 release.


@defer.inlineCallbacks
def example(reactor):
    pp = Connection()

    try:
        release = yield pp.release('ceph-3-0')
        result = yield release.task_date(milestones.DEV_FREEZE)
        # Print the datetime.date object.
        pprint(result)
        # Calculate offset from today.
        today = date.today()
        delta = result - today
        if delta.days > 0:
            message = '%d days from today' % delta.days
        if delta.days == 0:
            message = 'today'
        if delta.days < 0:
            message = '%d days ago' % -delta.days
        print(message)
    except ProductPagesException as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    react(example)
