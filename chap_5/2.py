def pick_6_lottery_expected_value(pot_size, ticket_price, num_tickets):
    winnings = pot_size / num_tickets  # Winnings
    winnings = pot_size / num_tickets  # Winnings per ticket
    probability_of_winning = 1 / math.comb(49, 6)  # Probability of winning with one ticket
    expected_value = probability_of_winning * winnings - ticket_price
    return expected_value

pot_size = 1000000  # Total size of the pot
ticket_price = 1  # Ticket price
num_tickets = 500000  # Number of tickets bought

expected_value = pick_6_lottery_expected_value(pot_size, ticket_price, num_tickets)
print(f"Expected value of buying a $1 lottery ticket: ${expected_value:.2f}")

