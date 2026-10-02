from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.trainers import BpeTrainer
from tokenizers.decoders import ByteLevel as ByteLevelDecoder

trainer = BpeTrainer(
    vocab_size=8000,
    special_tokens=["<EOS>"],
    initial_alphabet=ByteLevel.alphabet(),
)

tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = ByteLevel(add_prefix_space=False)
tokenizer.decoder = ByteLevelDecoder()

tokenizer.train(
    files=["data/processed/tinystories_50k.txt"],
    trainer=trainer,
)

tokenizer.save("tokenizer/tokenizer_v0.json")
