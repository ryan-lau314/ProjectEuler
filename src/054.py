from urllib.request import urlopen

VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
SUITS = ["C", "S", "H", "D"]


class PokerHand:
    def __init__(self, hand):
        assert len(hand) == 5
        for card in hand:
            assert isinstance(card, str)
            assert len(card) == 2
            assert card[0] in VALUES
            assert card[1] in SUITS

        self.hand = hand
        self.values = self.__values()
        self.suits = self.__suits()
        self.rank = self.__rank()

    def __values(self):
        values = [0] * len(VALUES)
        for card in self.hand:
            value = card[0]
            values[VALUES.index(value)] += 1
        return values

    def __suits(self):
        suits = [0] * len(SUITS)
        for card in self.hand:
            suit = card[1]
            suits[SUITS.index(suit)] += 1
        return suits

    def __rank(self):
        if self.__is_straight_flush():
            return "8 STRAIGHT FLUSH", self.__get_straight_flush_value()

        if self.__is_four_of_a_kind():
            return "7 FOUR OF A KIND", self.__get_four_of_a_kind_value()

        if self.__is_full_house():
            return "6 FULL HOUSE", self.__get_full_house_value()

        if self.__is_flush():
            return "5 FLUSH", self.__get_flush_value()

        if self.__is_straight():
            return "4 STRAIGHT", self.__get_straight_value()

        if self.__is_three_of_a_kind():
            return "3 THREE OF A KIND", self.__get_three_of_a_kind_value()

        if self.__is_two_pairs():
            return "2 TWO PAIRS", self.__get_two_pairs_value()

        if self.__is_pair():
            return "1 PAIR", self.__get_pair_value()

        return "0 HIGH CARD", self.__get_high_card_value()

    def __is_straight_flush(self):
        return self.__is_flush() and self.__is_straight()

    def __get_straight_flush_value(self):
        return self.__get_high_card_value()

    def __is_four_of_a_kind(self):
        return any(value == 4 for value in self.values)

    def __get_four_of_a_kind_value(self):
        return [self.values.index(4), self.values.index(1)]

    def __is_full_house(self):
        return self.__is_three_of_a_kind() and self.__is_pair()

    def __get_full_house_value(self):
        return [self.values.index(3), self.values.index(2)]

    def __is_flush(self):
        return any(suit == 5 for suit in self.suits)

    def __get_flush_value(self):
        return self.__get_high_card_value()

    def __is_straight(self):
        return "11111" in "".join([str(value) for value in self.values])

    def __get_straight_value(self):
        return self.__get_value_frequencies()[:1]

    def __is_three_of_a_kind(self):
        return any(value == 3 for value in self.values)

    def __get_three_of_a_kind_value(self):
        return [self.values.index(3)] + [
            value
            for value, frequency in self.__get_value_frequencies()
            if frequency == 1
        ]

    def __is_two_pairs(self):
        return len([value for value in self.values if value == 2]) == 2

    def __get_two_pairs_value(self):
        return [
            value
            for value, frequency in self.__get_value_frequencies()
            if frequency == 2
        ] + [self.values.index(1)]

    def __is_pair(self):
        return any(value == 2 for value in self.values)

    def __get_pair_value(self):
        return [self.values.index(2)] + [
            value
            for value, frequency in self.__get_value_frequencies()
            if frequency == 1
        ]

    def __get_high_card_value(self):
        return [value for value, _ in self.__get_value_frequencies()]

    def __get_value_frequencies(self):
        return [
            (value, frequency)
            for value, frequency in enumerate(self.values)
            if frequency > 0
        ][::-1]

    def __str__(self):
        rank_name, rank_values = self.rank
        return rank_name + ": " + ",".join([VALUES[value] for value in rank_values])

    def __gt__(self, other):
        self_rank_name, self_rank_values = self.rank
        other_rank_name, other_rank_values = other.rank

        return self_rank_name > other_rank_name or (
            self_rank_name == other_rank_name and self_rank_values > other_rank_values
        )


def p054():
    count = 0

    lines = urlopen("https://projecteuler.net/project/resources/p054_poker.txt")
    for line in lines:
        cards = line.decode("utf-8").strip().split(" ")
        first_hand = PokerHand(cards[:5])
        second_hand = PokerHand(cards[5:])
        if first_hand > second_hand:
            count += 1

    print(count)


if __name__ == "__main__":
    p054()
