from datasets import Dataset
from glob import glob
import json

DATA_FILES = glob("data/raw/tiny_stories/train-*.arrow")
NUM_STORIES = 50_000
OUTPUT_FILE = "data/processed/tinystories_50k.jsonl"

stories = []

# dataset = Dataset.from_files(DATA_FILES)

# print("Number of stories:", len(dataset))

total_stories = 0

for file in DATA_FILES:
    dataset = Dataset.from_file(file)
    # print(file, len(dataset))
    # total_stories += len(dataset)

    for story in dataset:
        stories.append(story["text"])

        if len(stories) >= NUM_STORIES:
            break

    if len(stories) >= NUM_STORIES:
        break

print("Collected stories:", len(stories))

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for story in stories:
        json.dump({"text": story}, f, ensure_ascii=False)
        f.write("\n")

# first_dataset = Dataset.from_file(DATA_FILES[0])

# total_characters = 0

# for story in first_dataset:
#     total_characters += len(story["text"])

# average_characters = total_characters / len(first_dataset)

# print("Average characters per story of 1 shard:", average_characters)
