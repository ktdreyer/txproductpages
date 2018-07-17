import os
from munch import Munch
from txproductpages import Connection
from txproductpages.release import Release
from treq.testing import StubTreq
from twisted.web.resource import Resource
import pytest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(TESTS_DIR, 'fixtures')


class _ReleaseTestResource(Resource):
    """
    A twisted.web.resource.Resource that represents a Product Pages release
    response. Return the valid JSON data for the release endpoint.
    """
    isLeaf = True

    def _fixture(self, url):
        """ Return path to our static fixture file. """
        filename = url.replace('/pp-admin/api/v1', FIXTURES_DIR)
        # If we need to represent this API endpoint as both a directory and a
        # file, check for a ".body" file.
        if os.path.isdir(filename):
            return filename + '.body'
        return filename

    def render(self, request):
        request.setResponseCode(200)
        request.setHeader(b'content-type', b'application/json; charset=utf-8')
        filename = self._fixture(request.uri)
        with open(filename) as fh:
            contents = fh.read()
        return contents.encode('utf-8')


class TestGetRelease(object):

    @pytest.inlineCallbacks
    def test_get_release(self, monkeypatch):
        monkeypatch.setattr('txproductpages.connection.treq',
                            StubTreq(_ReleaseTestResource()))
        pp = Connection()
        release = yield pp.release('ceph-3-0')
        assert isinstance(release, Release)
        assert isinstance(release, Munch)
        assert release.shortname == 'ceph-3-0'
