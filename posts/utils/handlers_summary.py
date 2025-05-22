from collections import defaultdict, Counter
import re

def generate_summary(posts, users):
    user_id_to_name = {user['id']: user['name'] for user in users}
    user_unique_words = defaultdict(set)
    overall_word_counter = Counter()
    word_user_counts = defaultdict(lambda: defaultdict(int))  # word -> userId -> count

    for post in posts:
        user_id = post['userId']
        title = post.get('title', '')
        words = re.findall(r'\b\w+\b', title.lower())

        user_unique_words[user_id].update(words)
        overall_word_counter.update(words)
        for word in words:
            word_user_counts[word][user_id] += 1

    sorted_users = sorted(user_unique_words.items(), key=lambda item: len(item[1]), reverse=True)
    top_users_result = [
        {
            "userId": user_id,
            "username": user_id_to_name.get(user_id, "Unknown"),
            "unique_word_count": len(words)
        }
        for user_id, words in sorted_users[:3]
    ]

    common_words_result = []
    for word, count in overall_word_counter.most_common(10):
        user_counts = word_user_counts[word]
        top_user_id = max(user_counts, key=user_counts.get)
        common_words_result.append({
            "word": word,
            "count": count,
            "topUserId": top_user_id,
            "topUsername": user_id_to_name.get(top_user_id, "Unknown"),
            "userCount": user_counts[top_user_id],
        })

    return {
        "top_users": top_users_result,
        "common_words": common_words_result
    }