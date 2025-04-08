# Functional Programming in Python
from functools import reduce

# List of users with their scores
users = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 67},
    {"name": "Charlie", "score": 95},
    {"name": "Diana", "score": 74},
]

# 1. map: Increase all scores by 5 points
def add_bonus(user):
    return {"name": user["name"], "score": user["score"] + 5}

updated_users = list(map(add_bonus, users))
print("Scores after bonus:")
print(updated_users)

# 2. filter: Get users with scores above 80
def is_high_scorer(user):
    return user["score"] > 80

high_scorers = list(filter(is_high_scorer, updated_users))
print("\nHigh scorers:")
print(high_scorers)

# 3. reduce: Total score of all users
total_score = reduce(lambda acc, user: acc + user["score"], updated_users, 0)
print("\nTotal score:", total_score)

# 4. lambda: Sorting users by score (descending)
sorted_users = sorted(updated_users, key=lambda user: user["score"], reverse=True)
print("\nUsers sorted by score:")
print(sorted_users)

# 5. all & any: Check for conditions
print("\nAll users scored above 60:", all(user["score"] > 60 for user in updated_users))
print("Any user scored 100:", any(user["score"] == 100 for user in updated_users))
