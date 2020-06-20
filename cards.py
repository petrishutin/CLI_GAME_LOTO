import random

def pool_of_numbers():
    pool = [i for i in range(1, 91)]
    random.shuffle(pool)
    return pool


def make_pair_of_cards():
    pool = pool_of_numbers()
    card1 = []
    card2 = []
    for _ in range(15):
        number = pool.pop()
        card1.append(number)
    for _ in range(12):
        card1.append('  ')
    for _ in range(15):
        number = pool.pop()
        card2.append(number)
    for _ in range(12):
        card2.append('  ')
    random.shuffle(card1)
    random.shuffle(card2)
    return card1, card2,


def show_cards(card1, card2):
    def join_cells(nums):
        return f"|{'|'.join((str(x) if len(str(x)) == 2 else ' ' + str(x) for x in nums))}|"

    print(f"{'_' * 28}    {'_' * 28}")
    print(join_cells(card1[:9]) + '    ' + join_cells(card2[:9]))
    print(join_cells(card1[9:18]) + '    ' + join_cells(card2[9:18]))
    print(join_cells(card1[18:]) + '    ' + join_cells(card2[18:]))
    print(f"{'-' * 28}    {'-' * 28}")

show_cards(*make_pair_of_cards())