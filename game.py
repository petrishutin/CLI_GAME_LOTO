import os
import sys
import time
import random

from typing import Union, List

from cards import pool_of_numbers, deal_a_cards, show_cards
from players import Human, Computer


class Game:
    def __init__(self):
        print('Welcome to LOTO game')
        time.sleep(2)

    def main_menu(self):
        os.system('clear')
        print('Main menu')
        choice1 = input("Input total number of players (must be in range 2 to 6) or 'q' to quit\n")
        if choice1.lower() == 'q':
            sys.exit('Bye!')
        choice2 = input("Input number of human players (must be in range 1 to 6, but not more that total number)\n")
        if choice2.lower() == 'q':
            sys.exit('Bye!')
        self._new_game(int(choice1), int(choice2))

    def _new_game(self, num_of_players: int, num_of_humans: int):
        if not 1 < num_of_players < 7:
            print('Number of players mast be in range of 2 to 6')
            time.sleep(1)
            self.main_menu()
        self.pool: List[int] = pool_of_numbers()
        self.winner: Union[Human, Computer, None] = None
        self.cards: List[list] = deal_a_cards(num_of_players)
        self.table_of_players: List[Union[Human, Computer]] = []
        if num_of_humans == num_of_players:
            for pl in range(num_of_players):
                player = Human(f'Person{pl+1}', self.cards.pop())
                self.table_of_players.append(player)
        else:
            for hm in range(num_of_humans):
                human = Human(f"Human{hm+1}", self.cards.pop())
                self.table_of_players.append(human)
            for cm in range(num_of_players - num_of_humans):
                computer = Computer(f"Computer{cm+1}", self.cards.pop())
                self.table_of_players.append(computer)
        self._start_match()

    def _start_match(self):
        while not self.winner:
            for pl in self.table_of_players:
                self._take_turn(pl)
                if len(self.table_of_players) == 1:
                    self.winner = self.table_of_players[0]
                    break
        self._end_match()

    def _show_cards(self):
        show_cards(*self.table_of_players)

    def _take_turn(self, player: Union[Human, Computer]):
        os.system('clear')
        self._show_cards()
        piece = self.pool.pop()
        print(f'Turn of {player.name}. Piece is {piece}')
        answer = player.take_piece(piece)
        if answer == 'win':
            self.winner = player
            self._end_match()
        elif answer == 'lose':
            self.table_of_players.remove(player)
        elif answer == 'wrong input':
            self.pool.append(piece)
            random.shuffle(self.pool)
        elif answer == 'take':
            pass
        else:
            self.pool.append(piece)
            random.shuffle(self.pool)

    def _end_match(self):
        os.system('clear')
        print(f'Winner is {self.winner.name}!')
        time.sleep(3)
        self.main_menu()
