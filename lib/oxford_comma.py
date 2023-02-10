def oxford_comma(items):
    pass
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        items[-1] = "and " + items[-1]
        return ", ".join(items)
