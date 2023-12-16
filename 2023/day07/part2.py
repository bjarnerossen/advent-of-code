def determine_hand_type(hand: str) -> int:
    hand_ranks = [
        [5],             # Five of a kind
        [4, 1],          # Four of a kind
        [3, 2],          # Full house
        [3, 1, 1],       # Three of a kind
        [2, 2, 1],       # Two pair
        [2, 1, 1, 1],    # One pair
        [1, 1, 1, 1, 1]  # High card
    ]
    card_counts = [hand.count(card) for card in set(hand) if card != 'J'] \
        or [0] 
    card_counts.sort(reverse=True)
    card_counts[0] += hand.count('J')
    return hand_ranks.index(card_counts)


def map_cards_to_integers(hand: str) -> tuple:
    ordered_card_labels = 'AKQT98765432J'
    return tuple(ordered_card_labels.index(card) for card in hand)


def read_input(filename: str) -> list:
    with open(filename) as file:
        return file.read().splitlines()


def calculate_winnings(hands: list) -> int:
    hands_info = []
    
    for line in hands:
        hand, bid = line.split(' ')
        encoded_hand = (
            determine_hand_type(hand),
            *map_cards_to_integers(hand),
            int(bid)
        )
        hands_info.append(encoded_hand)
    
    hands_info.sort(reverse=True)
    winnings = sum(rank * hand[-1] for rank, hand in enumerate(hands_info, start=1))  # rank * bid
    return winnings


def main():
    input_filename = 'input.txt'
    data = read_input(input_filename)
    total_winnings = calculate_winnings(data)
    print(total_winnings)


if __name__ == "__main__":
    main()
