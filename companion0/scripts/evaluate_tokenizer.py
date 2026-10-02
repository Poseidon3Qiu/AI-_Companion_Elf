from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("tokenizer/tokenizer_v0.json")

with open("data/processed/tinystories_50k.txt", "r", encoding="utf-8") as f:
    text = f.read()

encoding = tokenizer.encode(text)

total_tokens = len(encoding.ids)

print("Total tokens:", total_tokens)

num_stories = 50_000

average_tokens_per_story = total_tokens / num_stories

print("Average tokens/story:", average_tokens_per_story)

total_characters = len(text)

characters_per_token = total_characters / total_tokens

print("Total characters:", total_characters)
print("Characters/token:", characters_per_token)
