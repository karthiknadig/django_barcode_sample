from pybarc.utils import ean_13_checksum, ean_8_checksum


def test_ean_13_checksum():
    assert ean_13_checksum('400638133393x') == 89
    assert ean_13_checksum('4006381333930') == 89

def test_ean_8_checksum():
    assert ean_8_checksum('7351353x') == 63
    assert ean_8_checksum('73513530') == 63
