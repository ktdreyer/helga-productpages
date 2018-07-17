import pytest
from helga_productpages.util import match_release_phrase
from helga_productpages.util import release_not_found
from helga_productpages.util import release_to_text
from helga_productpages.task import ReleaseTask
from txproductpages import Connection
from txproductpages.release import Release
from twisted.internet import defer


date_values = [
    ('helga: rhcs 3.0 beta date', ReleaseTask('ceph',  '3-0', 'beta')),
    ('helga: rhcs 3.0z5 date', ReleaseTask('ceph',  '3-0', 'z5')),
    ('helga: rhcs 3.0z5 date?', ReleaseTask('ceph',  '3-0', 'z5')),
    ('helga: rhcs 3.0z5 release date', ReleaseTask('ceph',  '3-0', 'z5')),
]


@pytest.mark.parametrize('test_input,expected', date_values)
def test_release_phrase_with_date(test_input, expected):
    result = match_release_phrase(test_input, 'date')
    assert result == expected


class MockPPConnection(Connection):
    """ Mocked txproductpages.Connection """
    def upcoming_releases(self, product):
        release = Release(shortname='fooproduct-11.0')
        return defer.succeed([release])


@pytest.inlineCallbacks
def test_release_not_found():
    pp = MockPPConnection()
    release_task = ReleaseTask('fooproduct', '10.0', 'z99')
    result = yield release_not_found(pp, release_task, 'ktdreyer')
    expected = 'ktdreyer, I could not find release fooproduct-10.0 '\
               'in https://pp.engineering.redhat.com/pp/product/fooproduct ' \
               '. Maybe you meant "fooproduct 11.0"?'
    assert result == expected


def test_release_to_text():
    release = Release(shortname='ceph-3-0')
    result = release_to_text(release)
    assert result == 'ceph 3.0'
