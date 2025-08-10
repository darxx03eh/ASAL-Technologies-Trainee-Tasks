import random, itertools
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
random.shuffle(deck)
print(f"one choice: {random.choice(deck)}")
# u can choice more than one using
# this will choice 5 cards
print(f"five choices: {random.choices(deck, k=5)}")