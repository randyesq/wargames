A Python implementation of the War card game, Kleinman house style. Wikipedia says that
War is like https://en.wikipedia.org/wiki/War_(card_game), but this doesn't involve
any Jokers, which is the real way to play war.

This really is just an implementation to help teach my kids how to write code to
play card games that they already know how to play.

## Going to war

To play war, simple run:

```
$ python war.py
```

## Configuration

None, it's pretty simple. Two players, battling it out.

## Sample output of game play
```
$ python war.py
Player 1 has jokers to start?: True
Player 2 has jokers to start?: False
Round #  1: Player 1 [1:(28) King of Clubs, 2:(26) 4 of Hearts]
Round #  2: Player 1 [1:(29) 7 of Spades, 2:(25) 4 of Clubs]
Round #  3: Player 1 [1:(30) 6 of Hearts, 2:(24) 3 of Hearts]
Round #  4: Player 2 [1:(29) 3 of Clubs, 2:(25) King of Hearts]
Round #  5: Player 1 [1:(30) 9 of Clubs, 2:(24) 8 of Clubs]
Round #  6: Player 2 [1:(29) 5 of Spades, 2:(25) Joker]
Round #  7: Player 1 [1:(30) 5 of Diamonds, 2:(24) 4 of Spades]

[... snip ...]

Round #170: Player 2 [1:(45) 6 of Clubs, 2:( 9) Jack of Spades]
Round #171: Player 1 [1:(46) King of Diamonds, 2:( 8) 10 of Hearts]
There is a tie c1 2 of Diamonds, c2 2 of Spades
Round #  0: Player 1 [1:(43) 10 of Spades, 2:( 3) 6 of Hearts]
Player 1 won the tie and 6 cards to boot!
Round #172: Player 1 [1:(51) 2 of Diamonds, 2:( 3) 2 of Spades]
Round #173: Player 1 [1:(52) 10 of Diamonds, 2:( 2) Ace of Clubs]
Round #174: Player 1 [1:(53) King of Spades, 2:( 1) Jack of Spades]
Round #175: Player 1 [1:(54) Jack of Diamonds, 2:( 0) 6 of Clubs]
Player 1 has jokers to finish?: True
Player 2 has jokers to finish?: False
Player 1 is the winner!
$ 
```