from datetime import date
from txproductpages import Connection
from twisted.internet import defer
from twisted.internet.task import react
from pprint import pprint

# Compare the upcoming releases for the RH Ceph Storage product
# with RHEL 7's upcoming releases.

# Map of layered products to RHEL versions
CONFIG = {
    'ceph-3': 'rhel-7',
    'rhosp-14.0': 'rhel-7',
}

@defer.inlineCallbacks
def example(reactor):
    pp = Connection()

    layered_releases = yield pp.upcoming_releases('rhosp')

    rhel_releases = yield pp.upcoming_releases('rhel')
    for release in layered_releases:
        ga_date = to_date(release.ga_date)
        print(release.name)
        print(ga_date)
        # url = pp.schedule_url(release.shortname)
        # print(url)
        if 'relgroup_shortname' in release:
            config_key = release.relgroup_shortname  # 'ceph-3'
        else:
            # Eg. RHOSP does not have relgroup_shortname
            config_key = release.shortname  # 'rhosp-13.0'
        base_shortname = CONFIG[config_key]  # 'rhel-7'
        base_rhel = None
        for rhel_release in rhel_releases:
            if rhel_release.relgroup_shortname != base_shortname:
                continue
            if to_date(rhel_release.ga_date) < ga_date:
                base_rhel = rhel_release
        if base_rhel:
            print('will be based on %s' % base_rhel.name)
        else:
            print('will be based on latest GA %s' % base_shortname)


def to_date(date_string):
    (y, m, d) = date_string.split('-')
    return date(int(y), int(m), int(d))


if __name__ == '__main__':
    react(example)
