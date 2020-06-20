import random

from typing import List

from players import Computer


def pool_of_numbers() -> list:
    return random.shuffle([i for i in range(1, 91)])


def deal_a_cards(num: int) -> List[list]:
    pool = pool_of_numbers()
    cards = []
    for _ in range(num):
        card = []
        for _ in range(3):
            line = []
            for _ in range(5):
                number = pool.pop()
                line.append(number)
            for _ in range(4):
                line.append('  ')
            random.shuffle(line)
            card.extend(line)
        cards.append(card)
    return cards


def show_cards(*player_table) -> None:
    def join_card_cells(nums):
        return f"|{'|'.join((str(x) if len(str(x)) == 2 else ' ' + str(x) for x in nums))}|"

    name_string = card_top_edge = card_line1 = card_line2 = card_line3 = bottom_edge = ''
    for player in player_table:
        name_string += player.name + ' card:' + ' ' * (22 - len(player.name)) + '    '
        card_top_edge += f"{'_' * 28}    "
        card_line1 += f"{join_card_cells(player.card[:9])}    "
        card_line2 += f"{join_card_cells(player.card[9:18])}    "
        card_line3 += f"{join_card_cells(player.card[18:])}    "
        bottom_edge += f"{'-' * 28}    "
    print(name_string, card_top_edge, card_line1, card_line2, card_line3, bottom_edge, sep="\n")


if __name__ == '__main__':
    pt: List[Computer] = []
    name_list = ('Player1', '2fd', '3', '4')
    crds = deal_a_cards(4)
    print(crds)
    for name in name_list:
        user = Computer(name, crds.pop())
        pt.append(user)
        print(user.check_set)
    show_cards(*pt)
