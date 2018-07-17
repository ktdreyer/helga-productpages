import pytest
from helga_productpages.util import match_release_phrase
from helga_productpages.task import ReleaseTask


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
