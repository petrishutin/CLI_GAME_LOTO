import pytest

from cards import deal_cards, pool_of_numbers


class TestDealCards:

    @pytest.mark.parametrize('num, exp',
                             [pytest.param(2, 2),
                              pytest.param(3, 3),
                              pytest.param(4, 4),
                              pytest.param(5, 5),
                              pytest.param(6, 6),
                              ])
    def test_deal_cards_diff_num_of_players(self, num, exp):
        assert len(deal_cards(num)) == exp

    @pytest.mark.parametrize('error, input',
                             [pytest.param(TypeError, None),
                              pytest.param(AssertionError, 1),
                              pytest.param(AssertionError, 7)])
    def test_deal_cards_invalid_input(self, error, input):
        with pytest.raises(error) as exp:
            deal_cards(input)
            assert exp == error


class TestPoolOfNumbers:
    def test_pool_of_numbers_len_is_list(self):
        assert isinstance(pool_of_numbers(), list)

    def test_pool_of_numbers_len(self):
        assert len(pool_of_numbers()) == 90
