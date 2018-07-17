import pytest
from helga_productpages.task import ReleaseTask


values = [
    ('RHCS 1.3.4',       ReleaseTask('ceph',  '1-3.4', 'ga')),
    ('rhcs 2.5',         ReleaseTask('ceph',  '2-5',   'ga')),
    ('RHCS 3.0',         ReleaseTask('ceph',  '3-0',   'ga')),
    ('RHCS 3.0 release', ReleaseTask('ceph',  '3-0',   'ga')),
    ('RHCS 3.0 z2',      ReleaseTask('ceph',  '3-0',   'z2')),
    ('RHCS 3.0z2',       ReleaseTask('ceph',  '3-0',   'z2')),
    ('rhceph-3.0',       ReleaseTask('ceph',  '3-0',   'ga')),
    ('RHCEPH 3.0',       ReleaseTask('ceph',  '3-0',   'ga')),
    ('OSP 12 z2',        ReleaseTask('rhosp', '12.0',  'z2')),
    ('OSP 13',           ReleaseTask('rhosp', '13.0',  'ga')),
    ('OSP 13 Beta',      ReleaseTask('rhosp', '13.0',  'beta')),
    ('RHEL 7.5',         ReleaseTask('rhel',  '7-5',   'ga')),
    ('RHEL 8',           ReleaseTask('rhel',  '8-0',   'ga')),
    ('RHEL 8 beta',      ReleaseTask('rhel',  '8-0',   'beta')),
]


@pytest.mark.parametrize('test_input,expected', values)
def test_from_text(test_input, expected):
    result = ReleaseTask.from_text(test_input)
    assert result == expected


no_product_values = [
    ('3.0',           ReleaseTask('ceph', '3-0', 'ga')),
    ('3.0z5',         ReleaseTask('ceph', '3-0', 'z5')),
    ('3.0z5 release', ReleaseTask('ceph', '3-0', 'z5')),
]


class FakeSettings(object):
    """ Fake Helga settings with a DEFAULT_PRODUCT. """
    DEFAULT_PRODUCT = 'ceph'


@pytest.mark.parametrize('test_input,expected', no_product_values)
def test_from_text_default_product(monkeypatch, test_input, expected):
    """ Test with settings.DEFAULT_PRODUCT """
    monkeypatch.setattr('helga_productpages.task.settings', FakeSettings)
    result = ReleaseTask.from_text(test_input)
    assert result == expected


@pytest.mark.parametrize('test_input,_', no_product_values)
def test_from_text_no_default_product(monkeypatch, test_input, _):
    """ Test with no DEFAULT_PRODUCT """
    result = ReleaseTask.from_text(test_input)
    assert result is None
