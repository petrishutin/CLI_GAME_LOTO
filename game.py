import os
import sys
import time
import random

from cards import pool_of_numbers, make_pair_of_cards
from player import Player

class Game:

    def __init__(self):
        print('Welcome to LOTO game')
        time.sleep(2)

    def main_menu(self):
        os.system('clear')
        print('Main menu')
        choice = input('Input 1 to play PvE, 2 to play PvP, 3 to watch MEGA-ULTRA-BATTLE of AIs, q to quit\n')
        self._new_game(choice)

    def _new_game(self, mode):
        self.pool = pool_of_numbers()
        self.winner = None
        self.card1, self.card2 = make_pair_of_cards()
        if mode == 'q':
            sys.exit('Bye!')
        elif mode == '1':
            self.player1 = Player('Player1', self.card1)
            self.player2 = Player('Computer', self.card2, ai=True)
        elif mode == '2':
            self.player1 = Player('Player1', self.card1)
            self.player2 = Player('Player2', self.card2)
        elif mode == '3':
            self.player1 = Player('Computer1', self.card1, ai=True)
            self.player2 = Player('Computer2', self.card2, ai=True)
        else:
            print('Wrong input. try again')
            time.sleep(1)
            self.main_menu()
        self._start_match()

    def _start_match(self):
        while not self.winner:
            self._take_turn(1)
            self._take_turn(2)

    def _show_cards(self):
        def join_cells(nums):
            return f"|{'|'.join((str(x) if len(str(x)) == 2 else ' ' + str(x) for x in nums))}|"

        print(f"Player1 card: {' ' * 17}Player2 card:")
        print(f"{'_' * 28}    {'_' * 28}")
        print(f"{join_cells(self.player1.card[:9])}    {join_cells(self.player2.card[:9])}")
        print(f"{join_cells(self.player1.card[9:18])}    {join_cells(self.player2.card[9:18])}")
        print(f"{join_cells(self.player1.card[18:])}    {join_cells(self.player2.card[18:])}")
        print(f"{'-' * 28}    {'-' * 28}")

    def _take_turn(self, player: int):
        os.system('clear')
        self._show_cards()
        if player == 1:
            player = self.player1
            opponent = self.player2
        else:
            player = self.player2
            opponent = self.player1
        piece = self.pool.pop()
        print(f'Turn of {player.name}. Piece is {piece}')
        answer = player.take_piece(piece)
        if answer == 'win':
            self.winner = player
            self._end_match()
        elif answer == 'lose':
            self.winner = opponent
            self._end_match()
        elif answer == 'wrong input':
            self.pool.insert(-1, piece)
        elif answer == 'take':
            pass
        else:
            self.pool.append(piece)
            random.shuffle(self.pool)

    def _end_match(self):
        print(f'Winner is {self.winner.name}')
        time.sleep(3)
        self.main_menu()
