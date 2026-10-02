from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("tokenizer/tokenizer_v0.json")

text = "Once upon a time, there was a little dragon."

encoding = tokenizer.encode(text)

print("Text:")
print(text)

print("\nTokens:")
print(encoding.tokens)

print("\nToken IDs:")
print(encoding.ids)

print("\nNumber of tokens:")
print(len(encoding.ids))

decoded = tokenizer.decode(encoding.ids)

print("\nDecoded:")
print(decoded)

print("\nMatches original:")
print(decoded == text)

print("\nVocabulary size:")
print(tokenizer.get_vocab_size())
