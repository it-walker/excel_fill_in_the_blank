import pytest

from wareki import Wareki

class TestWareki:

    @pytest.mark.parametrize("test_input, expected", [
        (1868, '明治1'),
        (1900, '明治33'),
        (1911, '明治44'),
        (1912, '大正1'),
        (1920, '大正9'),
        (1926, '昭和1'),
        (1978, '昭和53'),
        (1989, '平成1'),
        (2000, '平成12'),
        (2019, '令和1'),
        (2020, '令和2'),
    ])
    def test_seireki_wareki_input(self, test_input, expected):
        assert Wareki().seireki_wareki(test_input) == expected

    @pytest.mark.parametrize("test_input", [
        (''),
        (0),
        (10000),
        (-1)
    ])
    def test_seireki_wareki_exception(self, test_input):
        with pytest.raises(ValueError):
            Wareki().seireki_wareki(test_input)

    @pytest.mark.parametrize("test_input, expected", [
        ('1868/12/12', ['明治', '',  '1', '1', '2', '1', '2']),
        ('1900/1/1',   ['明治', '3', '3', '',  '1', '',  '1']),
        ('1911/3/21',  ['明治', '4', '4', '',  '3', '2', '1']),
        ('1912/10/3',  ['大正', '',  '1', '1', '0', '',  '3']),
        ('1920/11/30 20:29:39', ['大正', '',  '9', '1', '1', '3', '0']),
        ('1926-12-20', ['昭和', '',  '1', '1', '2', '2', '0']),
    ])
    def test_wa_yymmdd_input(self, test_input, expected):
        assert Wareki().wa_yymmdd(test_input) == expected

    @pytest.mark.parametrize("test_input", [
        (''),
        ('1000/2/3'),
        ('1978/13/31')
    ])
    def test_wa_yymmddd_exception(self, test_input):
        with pytest.raises(ValueError):
            Wareki().wa_yymmdd(test_input)
    
    @pytest.mark.parametrize("test_input, expected", [
        ('昭和', '⑤.昭和\n\n7.平成\n\n9.令和'),
        ('平成', '5.昭和\n\n⑦.平成\n\n9.令和'),
        ('令和', '5.昭和\n\n7.平成\n\n⑨.令和')
    ])
    def test_check_wareki_input(self, test_input, expected):
        assert Wareki().check_wareki(test_input) == expected

    def test_check_wareki_exception(self):
        with pytest.raises(ValueError):
            Wareki().check_wareki('')
