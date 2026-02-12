# A tiny placeholder recommendation engine
from collections import Counter
import heapq


def simple_mutual_rec(user_id: str, data, limit: int = 10):  # API consumer can request how many recommendations they want
    if not isinstance(data, dict) or "users" not in data:
        raise ValueError("Invalid data format: expected {'users': [...]}")
    # TODO: fetch follow relations from Supabase and compute mutual counts
    user_friends = {}  # Lookup Dictionary
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])

    if user_id not in user_friends:
        raise KeyError("User not found")

    direct_friends = user_friends[user_id]
    suggestions = Counter()
    for friend in direct_friends:

        if friend not in user_friends:
            continue
        
        for mutual in user_friends[friend]:  # Friends Of Friend
            
            if mutual not in user_friends:
                continue

            if mutual == user_id or mutual in direct_friends:
                continue
            
            suggestions[mutual] += 1
    # Take all suggested users, sort them by number of mutual friends, highest first
    top_pairs = heapq.nlargest(limit, suggestions.items(), key=lambda x: x[1])
    return [user_id for user_id, mutual_count in top_pairs]
