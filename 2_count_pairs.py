def count_pairs(pairs):
    pairs_counter = {}

    for id, version in pairs:
        key = (id, version)

        if key in pairs_counter:
            pairs_counter[key] += 1
        else:
            pairs_counter[key] = 1

    result = [
        [id, version, count] for (id, version), count in pairs_counter.items()
    ]
    return result
