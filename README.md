<div align="center"><h1>Poker Table Generator</h1></div>

## About
This Python script implements a simple poker game for up to four players. The game includes the generation and shuffling of a standard deck of cards, dealing hands to players, shuffling cards on the table, and determining the winner based on the best poker hand.

## Usage

### Prerequisites
Ensure that you have Python installed on your system.

### Clone the Repository
```bash
git clone https://github.com/Be008/poker-table-generator.git
cd poker-table-generator
```
### Run the script
```bash
python main.py
```

## Logic Overview
<ul>
    <li><p>generate_deck(): Creates a standard deck of 52 playing cards.</p>
    </li>
    <li><p>shuffle_deck(deck, players): Shuffles the deck and deals hands to players.</p>
    </li>
    <li><p>shuffle_table(deck): Shuffles the deck to represent cards on the table.</p></li>
    <li><p>evaluate_hands(cards): Evaluates the best poker hand category for a given set of cards.</p>
    </li>
    <li><p>verify_winner(hands, table): Determines the winner and their winning hand based on player hands and table cards.</p>
    </li>
    <li><p>main(): Executes the main flow, displaying player hands, table cards, and announcing the winner.</p>
    </li>
</ul>

