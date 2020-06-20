import time


class Player:
    def __init__(self, name: str, card: list, ai: bool = False):
        self.name = name
        self.check_set = set(card)
        self.card = card
        self.ai = ai

    def take_piece(self, piece: int):
        if self.ai:
            time.sleep(1)
            if piece in self.check_set:
                self.check_set.remove(piece)
                position = self.card.index(piece)
                self.card[position] = '--'
                say = 'take'
            else:
                say = 'pass'
            if not self.check_set:
                return 'win'
            else:
                return say
        choice = input('Take? y/n\n')
        if choice.lower() == 'y':
            if piece in self.check_set:
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
        else:
            print('wrong input')
            say = 'wrong input'
        if not self.check_set:
            say = 'win'
        return say
