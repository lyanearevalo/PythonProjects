import art
print(art.logo)


any_other = "y"
auction_dictionary = {
}

while (any_other == "y"):
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")

    auction_dictionary[name] = int(bid)

    any_other = input("Are there any other bidders? Type 'y' or 'n'. ").lower()

    while any_other not in ("y", "n"):
        print("--- Invalid input. Try again. ---")
        any_other = input("Are there any other bidders? Type 'y' or 'n'. ")
    print("\n" * 100)

max_bid = 0
for key in auction_dictionary:
    if auction_dictionary[key] > max_bid:
        max_bid = auction_dictionary[key]
        winner = key

print(f"The winner is {key} with the highest bid of ${max_bid}.")


