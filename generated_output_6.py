def merge_dicts(dict1, dict2):
    """Merge two dictionaries, with values from dict2 overriding those from dict1."""
    return {**dict1, **dict2}
