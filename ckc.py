def open_or_senior(members):
    categories = []
    for age, handicap in members:
        if age >= 55 and handicap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories

# List of members as (age, handicap) pairs
members = [(60, 10), (45, 20), (55, 5), (50, 8)]

# Call the function and print the result
print(open_or_senior(members))
