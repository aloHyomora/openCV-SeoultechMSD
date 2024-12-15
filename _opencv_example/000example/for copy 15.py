# 카드 52장에서 무작위로 7장씩 뽑아 5명에게 나누어지도록 한다. 
import random as rnd
shapes = ['♠','◇','♡','♣']
nums = ['A'] + [str(n) for n in range(2,11)] + ['J', 'Q', 'K']
total_deck = [s+n for s in shapes for n in nums]

for i in range(5):
    selectedCards = rnd.sample(total_deck, 7)
    for ch in selectedCards:
        total_deck.remove(ch)
        
    print(f'Player{i+1} cards')
    print(selectedCards)
    print()
