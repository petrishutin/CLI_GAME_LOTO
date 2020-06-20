from typing import Union

import pytest

from players import Player, Computer, Human

class TestPlayerHumanComputer:

    @pytest.mark.parametrize('player, given_piece, exp_res',
                             [pytest.param(Computer('1', []), 1, 'win', id='Empty check_set -> win'),
                              pytest.param(Computer('1', [1, ]), 1, 'win', id='Get a piece and win'),
                              pytest.param(Computer('1', [2, ]), 1, 'pass', id='Get a piece and pass'),
                              pytest.param(Computer('1', [2, 1]), 1, 'take', id='Get a piece and take'), ])
    def test_computer_choice(self, player: Computer, given_piece: list, exp_res: str):
        """Testing if Computer class gives right answers"""
        assert player.take_piece(given_piece) == exp_res

    @pytest.mark.parametrize('player, exp_res',
                             [pytest.param(Player('Player1', [1,]), 'Name: Player1\nHand: [1]', id='Player'),
                              pytest.param(Human('Player1', [1,]), 'Name: Player1\nHand: [1]', id='Human'),
                              pytest.param(Computer('Player1', [1,]), 'Name: Player1\nHand: [1]', id='Computer'), ])
    def test_repr(self, player: Union[Player, Human, Computer], exp_res: str):
        """Testing if Players and children classes return right representation"""
        assert str(player) == exp_res