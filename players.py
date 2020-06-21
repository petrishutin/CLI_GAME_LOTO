import time
import sys


class Player:
    def __init__(self, name: str, card: list):
        self.name = name
        self.check_set = set(card)
        if '  ' in self.check_set:
            self.check_set.remove('  ')
        self.card = card

    def __repr__(self):
        return f"Name: {self.name}\nHand: {self.card}"


class Human(Player):

    def take_piece(self, piece: int):
        choice = input('Take? y/n\n')
        if choice.lower() == 'y':
            if self.check_set and piece in self.check_set:
                self.check_set.remove(piece)
                position = self.card.index(piece)
                self.card[position] = '--'
                say = 'take'
            else:
                say = 'lose'
        elif choice.lower() == 'n':
            if piece in self.check_set:
                say = 'lose'
            else:
                say = 'pass'
        elif choice.lower() == 'q':
            sys.exit('Bye')
        else:
            print('wrong input. Losing turn')
            time.sleep(0.5)
            say = 'wrong input'
        if not self.check_set:
            say = 'win'
        return say


class Computer(Player):

    def take_piece(self, piece):
        time.sleep(.8)
        if self.check_set and piece in self.check_set:
            self.check_set.remove(piece)
            position = self.card.index(piece)
            self.card[position] = '--'
            say = 'take'
        else:
            say = 'pass'
        if not self.check_set:
            say = 'win'
            return say
        return say
