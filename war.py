import random

class Card(object):
    """ A standard playing card. Don't make me get the Book of Hoyle!"""
    suits = ["Spades", "Clubs", "Diamonds", "Hearts", None]  # None is for Jokers
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Joker"]
    joker_rank = len(ranks) - 1

    def __init__(self, suit, rank):
        if suit is not None:
            if suit < 0 or suit > 4:
                raise Exception("Can't create a card with an unknown suit: %r!" % suit)
        if rank < 0 or rank > 13:
            raise Exception("Can't create a card with an unknown rank: %r!" % rank)
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ Human-representation of a card """
        if self.rank == len(self.ranks) - 1:
            return self.ranks[self.rank]
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    def __cmp__(self, other):
        """
        Compares this card to other by rank.

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        return cmp(self.rank, other.rank)

class Deck(object):
    """ A 54-card War deck, including two jokers. """
    def __init__(self):
        self.cards = []
        for i in xrange(len(Card.suits) - 1):
            for j in xrange(len(Card.ranks) - 1):
                self.cards.append(Card(i, j))

        # Add the two jokers
        self.cards.extend([Card(None, len(Card.ranks) - 1), Card(None, len(Card.ranks) - 1)])

        # Shuffle the cards by default
        self.shuffle()

    def shuffle(self):
        """ Shuffle the cards in this deck """
        random.shuffle(self.cards)

    def deal_card(self):
        """ Take a card from the top of the deck """
        return self.cards.pop()

class Hand(object):
    """ A players hand (collection of cards) """
    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards or []

    def add_card_to_bottom(self, card):
        """ Add a card to the bottom of the deck """
        self.cards.append(card)

    def add_card_to_top(self, card):
        """ Add a card to the top of the deck """
        self.cards.insert(0, card)

    def play_card(self):
        """ Remove a card from the top of a the hand """
        return self.cards.pop(0)

    @property
    def out_of_cards(self):
        """ Is this hand out of cards? """
        return self.num_cards == 0

    @property
    def num_cards(self):
        """ How many cards does this hand have? """
        return len(self.cards)

    @property
    def has_a_joker(self):
        return any([card.rank == Card.joker_rank for card in self.cards])

def play_round(hand1, hand2, round):
    """ Play a round of war """
    winning_hand = None
    card1, card2 = hand1.play_card(), hand2.play_card()
    if card1 < card2:
        hand2.add_card_to_bottom(card2)
        hand2.add_card_to_bottom(card1)
        winning_hand = hand2
    elif card2 < card1:
        hand1.add_card_to_bottom(card1)
        hand1.add_card_to_bottom(card2)
        winning_hand = hand1
    else:
        print "There is a tie c1 %s, c2 %s" % (card1, card2)
        winning_hand = play_tie(hand1, hand2, round)
        winning_hand.add_card_to_bottom(card1)
        winning_hand.add_card_to_bottom(card2)

    print "Round #%3d: %s [1:(%2d) %s, 2:(%2d) %s]" % (round, winning_hand.name, len(hand1.cards), card1, len(hand2.cards), card2)
    return winning_hand

def play_tie(hand1, hand2, round):
    """ Play a tie-breaking round of war """
    if hand1.out_of_cards:
        return hand2
    elif hand2.out_of_cards:
        return hand1

    # Players offer up 3 cards to put down in the kitty, which will go to the
    # winner of the tie-breaking round
    hand1_down_cards = []
    hand2_down_cards = []
    for hand, down_cards in [(hand1, hand1_down_cards), (hand2, hand2_down_cards)]:
        for _ in xrange(min(hand.num_cards - 1, 3)):
            down_cards.append(hand.play_card())

    # Play a round to determine who wins the tie
    winning_hand = play_round(hand1, hand2, 0)
    print "%s won the tie and %d cards to boot!" % (winning_hand.name, len(hand1_down_cards + hand2_down_cards))
    for spoils in hand1_down_cards + hand2_down_cards:
        winning_hand.add_card_to_bottom(spoils)

    return winning_hand

# The game
if __name__ == "__main__":
    # Get a deck of cards and two players
    d = Deck()
    hand1, hand2 = Hand("Player 1"), Hand("Player 2")

    # Deal the cards
    num_cards = len(d.cards)
    for i in xrange(num_cards):
        if i % 2 == 0:
            hand1.add_card_to_top(d.deal_card())
        else:
            hand2.add_card_to_top(d.deal_card())

    assert len(d.cards) == 0, 'Why is the dealer hiding cards?!?'
    assert len(hand1.cards) != 0, "Why didn't player 1 get any cards?"
    assert len(hand2.cards) != 0, "Why didn't player 2 get any cards?"

    # Play War!
    round = 1
    while not any([hand1.out_of_cards, hand2.out_of_cards]) and round <= 2000:
        play_round(hand1, hand2, round)
        round += 1

    if hand1.out_of_cards:
        print "Player 2 is the winner"
    elif hand2.out_of_cards:
        print "Player 1 is the winner"
    else:
        print "No clear winner"
    print "Player 1 has jokers?: ", hand1.has_a_joker
    print "Player 2 has jokers?: ", hand2.has_a_joker