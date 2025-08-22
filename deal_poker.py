#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from typing import List, Tuple

# -------- Configure card decks --------
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"] 
RANKS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "J", "Q", "K"] 
JOKERS = ["Joker", "Joker"]  # 문양 없음, 2장

def build_deck() -> List[str]:
    """
    4 types of shape (1-9, A,J, Q, K) + 2 of Joker = 54 cards in total
    Shows suite-rank or Joker. e,g. Spade-8, Hearts-K, Joker
    """
    deck = [f"{suit}-{rank}" for suit in SUITS for rank in RANKS]
    deck.extend(JOKERS)
    return deck

# -------- Input player count --------
def get_player_count(min_players: int = 1, max_players: int = 4) -> int:
    """
    Input how many players play. It's up to 4 and at least 2.
    """
    while True:
        raw = input(f"How many people play the game? ({min_players}~{max_players}): ").strip()
        if not raw.isdigit():
            print("Please enter a number.")
            continue
        n = int(raw)
        if n < min_players or n > max_players:
            print(f"Please input a number between {min_players} and {max_players}.")
            continue
        return n

# -------- Suffle --------
def shuffle_deck(deck: List[str]) -> None:
    """
    Shuffle cards in the deck.
    """
    random.shuffle(deck)

# -------- Distribute cards --------
def deal_cards(deck: List[str], num_players: int, hand_size: int = 5) -> Tuple[List[List[str]], List[str]]:
    """
    Distribute cards (hand_size) by num_players
    """
    total_needed = num_players * hand_size
    if total_needed > len(deck):
        raise ValueError("Lack of card in the deck.")

    players_hands = []
    for _ in range(num_players):
        hand = deck[:hand_size]
        del deck[:hand_size]
        players_hands.append(hand)

    remaining_deck = deck[:]  # Copy remaining cards
    return players_hands, remaining_deck

# -------- Main --------
def main():
    print("=== Play Poker game ===")
    num_players = get_player_count()

    deck = build_deck()
    shuffle_deck(deck)

    players_hands, remaining = deal_cards(deck, num_players, hand_size=5)

    # Display the results as an array type
    print("\n--- Owned cards by player ---")
    for idx, hand in enumerate(players_hands, start=1):
        print(f"Player {idx}: {hand}")

    print("\n--- Remaining cards ---")
    print(remaining)
    print(f"\nNumber of cards remaining: {len(remaining)}장")

if __name__ == "__main__":
    main()
