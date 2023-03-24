import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """
    >>> beer_card = Card('7', 'diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')

    >>> deck = FrenchDeck()
    >>> len(deck)
    52

    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[-1]
    Card(rank='A', suit='hearts')

    >>> from random import choice

    #>>> choice(deck)
    #Card(rank='3', suit='hearts')

    >>> for card in deck:  # doctest: +ELLIPSIS
    ...     print(card)
    Card(rank='2', suit='spades')
    ...
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
import doctest
doctest.testmod(verbose=True)