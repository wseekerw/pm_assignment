from collections import Counter
import difflib
from collections import defaultdict

def filter_shorter_title_posts(posts, max_length=15):
    filtered_posts = []

    for post in posts:
        title = post.get('title', '')
        if len(title) < max_length:
            post_with_reason = post.copy()
            post_with_reason['reason'] = "Short title"
            filtered_posts.append(post_with_reason)

    return filtered_posts


def find_duplicate_titles_by_user(posts):
    seen = defaultdict(set) 
    flagged = []

    for post in posts:
        user_id = post['userId']
        title = post['title']

        if title in seen[user_id]:
            flagged.append({**post, "reason": "Duplicate title by the same user"})
        else:
            seen[user_id].add(title) 

    return flagged

def find_users_with_similar_titles(posts, threshold=5, similarity_cutoff=0.8):
    flagged = []
    user_posts = defaultdict(list)

    for post in posts:
        user_posts[post['userId']].append(post)

    for user_id, user_post_list in user_posts.items():
        titles = [post['title'] for post in user_post_list]
        similar_count = 0

        for i in range(len(titles)):
            for j in range(i + 1, len(titles)):
                if difflib.SequenceMatcher(None, titles[i], titles[j]).ratio() > similarity_cutoff:
                    similar_count += 1

        if similar_count >= threshold:
            for post in user_post_list:
                flagged.append({**post, "reason": "User has multiple similar titles"})

    return flagged