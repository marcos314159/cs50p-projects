from twttr import shorten

def test_shorten():
    assert shorten('No') == 'N'
    assert shorten('0') == '0'
    assert shorten ('TWITTER') == 'TWTTR'
    assert shorten('Will') != 'WLL'
    assert shorten('.py') != 'py'


