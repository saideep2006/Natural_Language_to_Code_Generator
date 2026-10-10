def group_by_first_letter(words):
    result = {}
    for word in words:
        if not word:
            continue
        key = word[0]
        result.setdefault(key, []).append(word)
    return result
