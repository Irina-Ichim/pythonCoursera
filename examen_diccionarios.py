# Update the wardrobe with new items
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

# Function to calculate the total price in a basket
def add_prices(basket):
    total = 0
    for item, price in basket.items():
        total += price
    return round(total, 2)  

# Example usage of add_prices function
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
    "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
print(add_prices(groceries))  # Should print 28.44

# Function to group users by their roles
def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]
    return user_groups

# Example usage of groups_per_user function
print(groups_per_user({"local": ["admin", "userA"],
                      "public":  ["admin", "userB"],
                      "administrator": ["admin"] }))

# Function to generate a list of emails from a domain-user mapping
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return emails

# Example usage of email_list function
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
                  "yahoo.com": ["barbara.gordon", "jean.grey"],
                  "hotmail.com": ["bruce.wayne"]}))










