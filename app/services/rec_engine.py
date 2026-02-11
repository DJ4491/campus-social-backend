# A tiny placeholder recommendation engine
def simple_mutual_rec(user_id: str, data):
    
    user_friends = {}  # Lookup Dictionary
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])

    if user_id not in user_friends:
        return {}

    direct_friends = user_friends[user_id]
    suggestions = {}
    for friends in direct_friends:
        for mutual in user_friends[friends]:  # Friends Of Friends
            if mutual != user_id and mutual not in direct_friends:
                # Count mutual friends
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
    # Take all suggested users, sort them by number of mutual friends, highest first
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [user_id for user_id, mutual_count in sorted_suggestions]

    # TODO: fetch follow relations from Supabase and compute mutual counts
    return []
