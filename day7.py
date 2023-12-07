from utilities import get_lines
from enum import Enum
from collections import Counter

class CamelHand:
    class Types(Enum):
        High, Pair, TwoPair, Three, FullHouse, Four, Five = range(7)

    def __init__(self, hand: str) -> None:
        conversion = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

        self.hand = []
        for char in hand:
            if char in conversion:
                self.hand.append(conversion[char])
            else:
                self.hand.append(int(char))

        self.__determine_type__()

    def __determine_type__(self):
        counts = Counter(self.hand)
        if counts.most_common(1)[0][1] == 5:
            self.type = CamelHand.Types.Five
        elif counts.most_common(1)[0][1] == 4:
            self.type = CamelHand.Types.Four
        elif counts.most_common(2)[0][1] == 3 and counts.most_common(2)[1][1] == 2:
            self.type = CamelHand.Types.FullHouse
        elif counts.most_common(1)[0][1] == 3:
            self.type = CamelHand.Types.Three
        elif counts.most_common(2)[0][1] == 2 and counts.most_common(2)[1][1] == 2:
            self.type = CamelHand.Types.TwoPair
        elif counts.most_common(1)[0][1] == 2:
            self.type = CamelHand.Types.Pair
        else:
            self.type = CamelHand.Types.High

    def __lt__(self, other):
        if self.type == other.type:
            return self.hand < other.hand
        else:
            return self.type.value < other.type.value

    def __eq__(self, other):
        return self.type == other.type and self.hand == other.hand
    
    def __str__(self) -> str:
        return f"{','.join(self.hand)}: {self.type.name}"

    def __repr__(self) -> str:
        return self.__str__()


def part1(is_test: bool = True):
    all_lines = get_lines(7, is_test)
    hands = []

    for line in all_lines:
        hand, bid = line.split()
        hands.append((CamelHand(hand), int(bid)))

    hands.sort()

    total = 0
    for rank, hand in enumerate(hands):
        _, bid = hand
        total += bid * (rank + 1)

    return total
    


print(part1(False))
