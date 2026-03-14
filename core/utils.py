def build_url(target):

    if target.startswith("http://") or target.startswith("https://"):
        return target

    # default to https first
    return "https://" + target
