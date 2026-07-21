import re
post = 'Today is gonna be a good day, believe, Idiots'

def replace_by_start (bad_words):
    word = bad_words.group()
    return "*" * len(word)




bad_words = ['be', 'good', 'idiot?s']
badwords_str = '|'.join (bad_words)
p = rf'(\b{badwords_str})\b'

pattern = re.compile (p, flags = re.IGNORECASE)

cencored_post = re.sub(pattern, replace_by_start, post)

if __name__ == "__main__":
    print(cencored_post)