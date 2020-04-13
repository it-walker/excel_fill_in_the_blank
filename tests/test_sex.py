import pytest

from sex import Sex

class TestSex:

    @pytest.mark.parametrize("test_input, expected", [
        ('男', Sex.TEMPLATE_MALE),
        ('女', Sex.TEMPLATE_FEMALE)
    ])
    def test_sex_input(self, test_input, expected):
        assert Sex().text(test_input) == expected

    def test_exception(self):
        with pytest.raises(ValueError):
            Sex().text('')
