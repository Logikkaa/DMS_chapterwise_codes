from itertools import combinations

def is_straight(hand_values):
    return all(hand_values[i] == hand_values[i + 1] - 1 for i in range(4))

def poker_probabilities():
    ranks = "23456789TJQKA"
    suits = "CDHS"
    deck = [rank + suit for rank in ranks for suit in suits]
    poker_hands = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight", "Flush",
                   "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
    hand_counts = {hand: 0 for hand in poker_hands}
    total_hands = 0

    for hand in combinations(deck, 5):
        hand_values = [ranks.index(card[0]) for card in hand]
        hand_suits = [card[1] for card in hand]
        sorted_hand_values = sorted(hand_values)

        if is_straight(sorted_hand_values):
            hand_counts["Straight"] += 1

        if len(set(hand_suits)) == 1:
            hand_counts["Flush"] += 1

        for value in sorted_hand_values:
            occurrences = hand_values.count(value)
            if occurrences == 2:
                hand_counts["One Pair"] += 1
                break
            elif occurrences == 3:
                hand_counts["Three of a Kind"] += 1
                break
            elif occurrences == 4:
                hand_counts["Four of a Kind"] += 1
                break

        if sorted_hand_values[0] == 0 and is_straight(sorted_hand_values[1:] + [13]):
            hand_counts["Royal Flush"] += 1
        elif is_straight(sorted_hand_values):
            hand_counts["Straight Flush"] += 1

        total_hands += 1

    for hand in poker_hands:
        probability = hand_counts[hand] / total_hands
        print(f"Probability of {hand}: {probability:.6f}")

poker_probabilities()
