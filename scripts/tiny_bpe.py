text = "low low low lower lower newest widest"

words = text.split()

print(words)

word_symbols = [list(word) for word in words]

print(word_symbols)


# count
def count_pairs(word_symbols):
    pair_counts = {}

    for symbols in word_symbols:
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])

            if pair not in pair_counts:
                pair_counts[pair] = 0

            pair_counts[pair] += 1

    return pair_counts


# merge
def merge_pair(word_symbols, best_pair):
    new_word_symbols = []

    for symbols in word_symbols:
        new_symbols = []
        i = 0

        while i < len(symbols):
            if i < len(symbols) - 1 and (symbols[i], symbols[i + 1]) == best_pair:
                new_symbols.append(symbols[i] + symbols[i + 1])
                i += 2
            else:
                new_symbols.append(symbols[i])
                i += 1

        new_word_symbols.append(new_symbols)

    return new_word_symbols


# pair_counts = count_pairs(word_symbols)

# best_pair = max(pair_counts, key=pair_counts.get)

# new_word_symbols = merge_pair(word_symbols, best_pair)

# word_symbols = new_word_symbols

num_merges = 5

for step in range(num_merges):
    pair_counts = count_pairs(word_symbols)

    best_pair = max(pair_counts, key=pair_counts.get)

    print("Step:", step + 1)
    print("Best pair:", best_pair)
    print("Count:", pair_counts[best_pair])

    word_symbols = merge_pair(word_symbols, best_pair)

    print("After merge:", word_symbols)
    print()
