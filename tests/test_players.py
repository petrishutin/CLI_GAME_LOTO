import pytest

from unittest.mock import patch
from typing import Union

from players import Player, Computer, Human


class TestPlayerHumanComputer:

    @pytest.mark.parametrize('player, exp_res',
                             [pytest.param(Player('Player1', [1, ]), 'Name: Player1\nHand: [1]', id='Player'),
                              pytest.param(Human('Player1', [1, ]), 'Name: Player1\nHand: [1]', id='Human'),
                              pytest.param(Computer('Player1', [1, ]), 'Name: Player1\nHand: [1]', id='Computer'), ])
    def test_repr(self, player: Union[Player, Human, Computer], exp_res: str):
        """Testing if Players and children classes return right representation"""
        assert str(player) == exp_res

    @pytest.mark.parametrize('player, given_piece, exp_res',
                             [pytest.param(Computer('1', []), 1, 'win', id='Empty check_set -> win'),
                              pytest.param(Computer('1', [1, ]), 1, 'win', id='Get a piece and win'),
                              pytest.param(Computer('1', [2, ]), 1, 'pass', id='Get a piece and pass'),
                              pytest.param(Computer('1', [2, 1]), 1, 'take', id='Get a piece and take'), ])
    def test_computer_choice(self, player: Computer, given_piece: list, exp_res: str):
        """Testing if Computer class gives right answers"""
        assert player.take_piece(given_piece) == exp_res


class TestHumanAnswers:
    """Testing human input and reaction"""

    @patch('test_players.Human._user_input', return_value='y')
    def test_human_right_choice_and_win(self, _user_input):
        assert Human('1', [1, ]).take_piece(1) == 'win'

    @patch('test_players.Human._user_input', return_value='n')
    def test_human_wrong_choice_and_lose(self, _user_input):
        assert Human('1', [1, ]).take_piece(1) == 'lose'

    @patch('test_players.Human._user_input', return_value='y')
    def test_human_right_choice_and_take(self, _user_input):
        assert Human('1', [2, 1]).take_piece(1) == 'take'

    @patch('test_players.Human._user_input', return_value='n')
    def test_human_right_choice_and_pass(self, _user_input):
        assert Human('1', [2, ]).take_piece(1) == 'pass'

    @patch('test_players.Human._user_input', return_value='sfdas')
    def test_human_wring_input(self, _user_input):
        assert Human('1', [2, ]).take_piece(1) == 'wrong input'
