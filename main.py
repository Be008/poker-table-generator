import random
from collections import namedtuple

NUM_CARDS_PER_PLAYER = 2
PLAYERS = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

Card = namedtuple('Card', ['rank', 'suit'])

def generate_deck():
    deck = [Card(rank, suit) for suit in SUITS for rank in RANKS]
    return deck

def shuffle_deck(deck, players):
    random.shuffle(deck)
    hands = {player: [] for player in players}
    for _ in range(NUM_CARDS_PER_PLAYER):
        for player in players:
            hands[player].append(deck.pop())
    return hands

def shuffle_table(deck):
    random.shuffle(deck)
    table = [deck.pop() for _ in range(5)]
    return table

def evaluate_hands(cards):
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    values = [ranks[card.rank] if card.rank != 'Ace' else 1 for card in cards]
    values.sort(reverse=True)

    # Check for straight flush
    suits = {card.suit for card in cards}
    if len(suits) == 1 and values == list(range(values[0], values[0] - 5, -1)):
        return 'Straight flush', values
    
    # Check for four of a kind
    for value in values:
        if values.count(value) == 4:
            return 'Four of a kind', value
    
    # Check for full house
    if len(set(values)) == 2 and values.count(values[0]) in [2, 3]:
        return 'Full house', values
        
    # Check for flush
    if len(suits) == 1:
        return 'Flush', values
    
    # Check for straight
    if values == list(range(values[0], values[0] - 5, -1)):
        return 'Straight', values
    
    # Check for three of a kind
    for value in values:
        if values.count(value) == 3:
            return 'Three of a kind', value
        
    # Check for two pairs
    pairs = [value for value in set(values) if values.count(value) == 2]
    if len(pairs) == 2:
        return 'Two pairs', pairs
    
    # Check for one pair
    for value in values:
        if values.count(value) == 2:
            return 'One pair', value
    
    # Check for high card
    return 'High card', values

def verify_winner(hands, table):
    best_hand = max(hands.items(), key=lambda x: evaluate_hands(x[1] + table))
    return best_hand[0], evaluate_hands(best_hand[1] + table)

def main():
    deck = generate_deck()
    hands = shuffle_deck(deck, PLAYERS)
    for player, cards in hands.items():
        print(f'{player}: {[f"{card.rank} of {card.suit}" for card in cards]}')
    table = shuffle_table(deck)
    print(f'Table: {[f"{card.rank} of {card.suit}" for card in table]}')
    winner, best_hand = verify_winner(hands, table)
    print(f'{winner} wins with {best_hand[0]}')

if __name__ == '__main__':
    while True:
        main()
        if input('Play again? (y/n): ').lower() != 'y':
            break
