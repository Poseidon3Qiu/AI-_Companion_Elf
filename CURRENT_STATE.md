# Project Companion — Current State

Last updated: 2026-10-01

This is the complete replacement version, based on the available synced `sources/CURRENT_STATE.md`. The original `/mnt/data/CURRENT_STATE.md` path is unavailable in this environment. Historical learning notes and experimental decisions are retained; obsolete current-status sections are updated below. Completion metrics are carried forward from the project owner's milestone record, not independently rerun in this update.

## Current Phase

**Companion-0: COMPLETE — educational / experimental baseline retained.**

**Companion-1: BEGINNING — minimal Brain Interface and first foundation-model integration.**

## Active Experiment

Companion-1 — Minimal Brain Interface.

C0-EXP001 — Tokenizer Build 1 is retained below as a completed historical experiment.

## Current Goal

Implement the smallest useful Brain Interface, initially exposing only:

```text
generate(context)
```

Then connect the first open-weight foundation model and let Companion-1 speak. The current first candidate is **Qwen3.5-9B**; this is a project candidate, not a permanent backend commitment or a claim that deployment has already been validated.

Companion-0 has completed the end-to-end learning pipeline. From-scratch pretraining is no longer the main development route. Preserve Companion-0's code, tokenizer, checkpoint, experimental results, and learning notes as an educational / experimental baseline.

---

## Project Learning Method

Project-first + Just-in-time Learning, with research serving the Companion.

Historical formulation: Project-first + Research-first + Just-in-time Learning. The 2026-10-01 update clarifies that research is driven by concrete building needs.

Approximate principle:

- 70% Build
- 20% Just-in-time Learning
- 10% Systematic Foundation

Proceed one step at a time.

Do not dump large amounts of code or theory at once.

When a new concept becomes necessary, explain only enough to understand and continue the current engineering task.

Performance optimization should not distract from the main path, but **time-to-result is a priority**. For compute-heavy work, benchmark first and avoid wasting long periods on slower local execution when an effective faster resource is available.

Main priority:

**Keep moving along the Companion main development path; the active stage is now Companion-1.**

---

# Companion-0 Architecture — Completed Baseline

Completed pipeline:

```text
TinyStories
    ↓
Tokenizer v0
    ↓
Token IDs
    ↓
Embedding
    ↓
Transformer
    ↓
Logits
    ↓
Next-token prediction
    ↓
Training
    ↓
Checkpoint
    ↓
Inference
    ↓
First Companion-0 generated text
```

Completion status as of 2026-10-01:

```text
Tokenizer v0           ✓ COMPLETE
Token IDs              ✓ UNDERSTOOD
Embedding              ✓ BASIC COMPLETE
Positional information ✓ BASIC UNDERSTOOD
Self-Attention          ✓ BASIC UNDERSTOOD
Multi-Head Attention    ✓ BASIC UNDERSTOOD
Transformer Block       ✓ BASIC UNDERSTOOD
Logits / next-token     ✓ BASIC UNDERSTOOD
Training Loss           ✓ COMPLETE (initial implementation)
Backprop / optimization ✓ COMPLETE (initial implementation)
Training loop           ✓ COMPLETE (10-step sanity run)
Checkpoint              ✓ SAVED
Inference               ✓ COMPLETE (first autoregressive generation)
```

---

# C0-EXP001 — Tokenizer Build 1

## Dataset

Dataset:

TinyStories

Training subset:

50,000 stories

Files currently available:

```text
data/processed/tinystories_50k.jsonl
data/processed/tinystories_50k.txt
```

The plain-text file is used for tokenizer training:

```text
data/processed/tinystories_50k.txt
```

---

## Tokenizer Design

Tokenizer algorithm:

**Byte-level BPE**

Target vocabulary size:

```text
8,000
```

Model target:

```text
Companion-0
~10M–50M parameters (original planning target)
7,321,088 parameters (completed baseline)
```

The 8K vocabulary is an experimental starting point, not assumed to be optimal.

Future experiments may compare:

```text
8K vs 16K vocabulary
```

and measure effects on:

- tokenization efficiency
- sequence length
- model parameter count
- downstream model behavior

---

# Special Token Decisions

Tokenizer v0 currently uses:

```text
<EOS>    YES
<BOS>    NO
<PAD>    NO
<UNK>    NO
```

## EOS

`<EOS>` = End Of Sequence.

Chosen to mark story boundaries:

```text
Story A <EOS> Story B <EOS> Story C <EOS>
```

EOS should be inserted between stories / at the end of each story during preparation of the pretraining token stream.

It should NOT be inserted between ordinary sentences.

Sentence boundaries can already be represented by normal punctuation such as:

```text
.
?
!
```

Important:

Adding `<EOS>` to `special_tokens` only places

[Source note: this sentence was already truncated in the available baseline. The fragment is preserved; the missing original wording is unavailable. The explicit EOS insertion rule above remains valid.]

---

# Neural Network Progress — 2026-10-01

## Embedding

PyTorch is installed and `nn.Embedding` has been tested.

Current experimental settings:

```text
vocab_size = 8000
embedding_dim = 256
```

Understood:

- Token IDs are identifiers / lookup indices, not meaningful numerical magnitudes.
- `nn.Embedding` maps each Token ID to a trainable vector.
- Embedding weights begin as learned parameters and are updated during training.
- For a single sequence, `[T] -> [T, C]`.
- For batched sequences, `[B, T] -> [B, T, C]`.

Tensor dimension convention now understood:

```text
B = batch size
T = sequence length / number of tokens per sequence
C = channels / embedding dimension
```

Example:

```text
[B, T] = [3, 4]
embedding_dim = 256
→ [B, T, C] = [3, 4, 256]
```

## Positional Information

Basic concept understood:

```text
Tensor ordering exists
≠
Attention automatically receives position as a feature
```

Therefore Transformer needs positional information in addition to Token Embedding.

A deeper mathematical/code demonstration is intentionally deferred until Self-Attention, where the reason becomes directly relevant.


## Self-Attention / Transformer Concepts

Conceptually understood:

- Context = the token information currently available to the model for understanding / prediction; it is not simply a human-language text length.
- Sequence length `T` is the number of token positions in the current sequence. Context windows are measured in tokens.
- In GPT-style causal attention, each position may attend to itself and previous allowed positions, but not future positions.
- For each token representation `X`, learned projections create Query, Key, and Value vectors:

```text
Q = X W_Q
K = X W_K
V = X W_V
```

- Query/Key matching produces attention scores. Softmax converts scores into positive attention weights that sum to 1.
- The attention output for a token position is the weighted sum of the Value vectors of the positions it is allowed to see.
- Attention output is not written back into the original Embedding Table. It forms new hidden-state / token-representation tensors.
- The original Embedding Table has shape approximately `[vocab_size, d_model]`; the per-sequence hidden states have shape `[B, T, C]`. These are different objects.
- Numerical vectors are information representations. Transformer operations transform these representations into forms that are increasingly contextual and useful for next-token prediction.

## Multi-Head Attention

Basic concept understood:

```text
d_model = 256
num_heads = 8        # example design
head_dim = 32
```

Each head has its own learned Q/K/V projections and can learn different useful attention patterns. The head outputs are concatenated and passed through an output projection `W_O`, returning to the model dimension.

Typical shape flow:

```text
[B,T,256]
    ↓
8 heads × [B,T,32]
    ↓ concatenate
[B,T,256]
    ↓ W_O
[B,T,256]
```

## Residual / FFN / LayerNorm / Transformer Blocks

Understood:

- Residual connections preserve the incoming representation while adding newly computed information: conceptually `new = old + change`.
- FFN / MLP operates independently on each token position after attention. It commonly expands the channel dimension temporarily and projects it back, e.g. `256 -> 1024 -> 256`.
- LayerNorm stabilizes / normalizes the numerical representation while preserving tensor shape. Detailed mathematics are intentionally deferred.
- Transformer Blocks are stacked serially. Block 2 consumes Block 1's output; Block 3 consumes Block 2's output, etc.
- Blocks have similar architecture but normally have independent learnable parameters.
- Across blocks, the main hidden-state shape normally remains `[B,T,C]`, while the vector values / representations change layer by layer.
- Changes in hidden-state values during a forward pass are activations / representations changing; this is distinct from updating model parameters during training.

Conceptual block skeleton currently understood:

```text
X
↓ LayerNorm
Multi-Head Self-Attention
↓
Residual Add
↓ LayerNorm
FFN / MLP
↓
Residual Add
↓
Block Output
```

## Logits / Next-Token Prediction

For Companion-0's current dimensions:

```text
d_model = 256
vocab_size = 8000
```

After the final Transformer representation:

```text
[B,T,256]
    ↓ output linear projection
[B,T,8000]
```

The 256 hidden dimensions are representation features; they are not token choices. The 8,000 output dimensions correspond to the 8,000 vocabulary token candidates. These raw scores are logits.

Softmax can convert logits into a probability distribution over vocabulary tokens for prediction / sampling.

Causal language-model training concept understood:

```text
Tokens:  The | dog | chased | the | cat
Input:   The | dog | chased | the
Target:  dog | chased | the | cat
```

The target is the token stream shifted by one position. During training, multiple sequence positions can provide next-token prediction signals in the same forward pass.

## MPS / Apple GPU

MPS support has been verified on the current Mac:

```text
MPS available: True
MPS built: True
Using device: mps
```

Companion-0 neural-network code should be device-aware from the beginning and support MPS by default when available. Model parameters and input tensors must be on the same device.

Tiny experiments may not become faster on MPS because startup / dispatch overhead can dominate. MPS becomes more relevant for Transformer matrix operations, forward/backward passes, and training.

# Compute / Time-to-Result Rule

Time sensitivity is an explicit engineering requirement.

```text
< 5 min       Local execution is fine.
5–15 min      Local is usually acceptable; easy free acceleration may still be considered.
>= 15 min     Proactively evaluate acceleration options.
>= 30 min     Do not default to letting the M1 run; benchmark and seek faster resources first.
```

Before large jobs, run a short benchmark (for example 100–500 steps when appropriate) and estimate:

- throughput / tokens per second
- expected total runtime
- memory usage
- device being used

Compare **total time-to-result**, including setup, upload, migration, and environment overhead. A remote GPU is not automatically better if moving the workload takes longer than simply completing it locally.

Acceleration preference:

```text
1. M1 Pro + MPS
2. Low-cost code / batch / precision improvements
3. Free GPU resources such as Colab when available and beneficial
4. Other existing/free compute resources
5. Low-cost cloud GPU when justified
```

# Immediate Next Step / Resume Point

**Begin Companion-1: implement the minimal Brain Interface, then connect the first open-weight foundation model so Companion-1 can speak.**

1. Define the single initial entry point: `generate(context)`.
2. Implement one backend for the first candidate brain, Qwen3.5-9B, choosing execution resources according to actual memory, latency, setup, and cost requirements.
3. Run a first real interaction through the interface and record its output and practical limitations.
4. Let observed interaction problems determine the next capability and the research needed to add it.

Keep the backend replaceable across Local / Cloud / API. Do not build a full Memory / Identity / Agent system in advance. Continue one necessary concept at a time, then return to building.

Historical resume point, now completed: Training Loss → cross-entropy → backpropagation / gradients → optimizer updates → first training loop → checkpoint → autoregressive inference.

---

# Milestone — 2026-10-01

## Companion-0 — COMPLETE

Companion-0 completed the full pipeline:

```text
TinyStories
→ byte-level BPE tokenizer
→ token IDs
→ token + positional embeddings
→ causal Transformer
→ logits
→ next-token prediction
→ cross-entropy loss
→ backpropagation / gradients
→ AdamW parameter updates
→ training loop
→ checkpoint
→ autoregressive inference
→ first generated text
```

### Dataset / Token Stream

- Dataset: TinyStories, 50,000-story subset.
- Tokenizer: byte-level BPE, vocabulary size 8,000.
- Total tokenized training stream: **10,956,351 tokens**.
- The token-stream size is not the number of tokens processed in the 10-step sanity run.

### Completed Model

```text
embedding_dim = 256
num_heads = 8
num_layers = 4
max_seq_len = 256
parameters = 7,321,088
```

Architecture: causal self-attention, Pre-LN Transformer blocks, and GELU feed-forward networks. The completed model is smaller than the original approximate 10M–50M planning target; retain both the historical target and actual result.

### First Training Run

```text
Hardware: MacBook Pro M1 Pro
Device: PyTorch MPS
batch_size = 8
seq_len = 256
learning_rate = 3e-4
optimizer = AdamW
training_steps = 10

Step 1 loss  = 9.1568
Step 10 loss = 7.7127
```

The loss decreased during the initial run. This validated the initial forward → loss → backward → optimizer update workflow on MPS. Ten steps are a pipeline sanity test, not evidence of convergence, generalization, or useful language ability; no held-out evaluation result is recorded here.

### Checkpoint

```text
companion_0_checkpoint.pt
```

The checkpoint was saved as part of the completed training workflow. Its exact filesystem location and serialized fields are not present in the available state-file record; do not infer them.

### First Autoregressive Inference

Prompt:

```text
Once upon a time
```

First generation result: incoherent but English-like token sequences after the 10-step training run. The exact generated text is not available in the supplied baseline or retrieved milestone preview and is therefore not reconstructed here.

Conclusion: the first autoregressive generation completed, validating the end-to-end route from data to model training, checkpoint, and generated text. Very limited training explains why this initial output does not demonstrate coherent storytelling or Companion-level interaction.

### Learning Outcome / Baseline Role

Companion-0 provided firsthand experience with tokenization, embeddings, contextual representations, logits, shifted next-token targets, loss, gradients, parameter updates, checkpointing, and autoregressive generation.

Retain it as an educational / experimental baseline. Future from-scratch experiments may be run to answer specific learning or research questions, but continued from-scratch pretraining is **not the main route toward Companion**.

---

# Strategic Transition — Research Serves Companion

```text
Companion = Foundation Model
          + Identity
          + Memory
          + Experience
          + Personality
          + Context
          + Tools
          + Learning mechanisms
```

**Companion != Foundation Model.** The foundation model supplies the initial language / reasoning backend; the larger Companion direction concerns continuity, identity, accumulated experience, interaction, and capabilities around that backend. These components describe the direction, not an already implemented system or a requirement to build every component immediately.

**Research serves Companion.** Use research when a concrete development problem or interaction exposes a need. Reproduction is a way to understand relevant mechanisms; it does not require independently rebuilding every mature component before making progress.

## Development Principles

- **Build first.** Produce the smallest working interaction, then iterate.
- **Research just in time.** Investigate the specific obstacle or capability that is currently needed.
- **Reproduce to understand.** Use focused reproductions when firsthand implementation improves understanding.
- **Don't reinvent unknowingly.** Check existing approaches before committing to a custom solution, and make the choice consciously.
- **Research serves Companion.** Keep research connected to the project's practical direction.

Preserve the existing approximately 70% Build / 20% Just-in-time Learning / 10% Systematic Foundation balance and the one-step-at-a-time method.

# Compute Strategy — Experiment-Driven Choice

Choose resources for each experiment:

| Resource | Intended role |
| --- | --- |
| Local Mac / MPS | Small experiments, local interaction, debugging, and workloads that fit available resources |
| Colab / Kaggle | Free or accessible accelerated experiments when availability and setup make them useful |
| Rented Cloud GPU | Workloads whose memory or throughput requirements justify rental cost and migration |
| API | Prototyping, evaluation, comparison, and auxiliary assistance |

The earlier benchmark and total time-to-result rules remain in force. The historical acceleration preference is a starting heuristic, not a fixed resource requirement. Select according to the experiment's memory needs, throughput, latency, cost, availability, and setup overhead.

Commercial APIs may support prototypes, evaluation, or auxiliary tasks. They must not become Companion's permanent sole dependency. Keep the Brain Interface replaceable so Local, Cloud, and API backends can be swapped without redefining Companion itself.

# Companion-1 — Minimal Brain Interface

Initial public interface:

```text
generate(context)
```

Start with this single operation. Determine additional interface requirements from real interaction rather than designing an extensive abstraction in advance.

- First candidate Brain: **Qwen3.5-9B**.
- Candidate status: selected for the first integration attempt; not permanently bound.
- Execution options: Local / Cloud / API, selected per experiment.
- Immediate outcome: Companion-1 produces its first response through the Brain Interface using an open-weight foundation model.
- Implementation status: beginning; no completed integration or successful run is claimed in this state update.

Do not prebuild the full Memory / Identity / Agent system. Let actual conversations reveal issues, then research and add the smallest necessary capability just in time.

# Research Questions / Record Boundaries

Retain the tokenizer questions already recorded above: 8K vs 16K vocabulary, tokenization efficiency, sequence length, parameter count, and downstream behavior. These remain optional baseline experiments rather than immediate Companion-1 prerequisites.

Identity / Self, memory, experience, personality, context, tools, and learning mechanisms remain future research directions to be grounded in actual Companion interaction. The available baseline does not contain a separate Track B / Identity / Self history; no missing historical entries are invented in this update. Previously overwritten material cannot be recovered from this file alone and should be merged if an older source is later recovered.

# State File Update Policy

**“Update CURRENT_STATE.md” means deliver the complete full-text replacement by default.**

Use the existing file as the baseline, retain valid history, experimental data, learning notes, research questions, and methodology, append dated milestones, and make targeted edits to obsolete current-status sections. Do not replace the accumulated record with a current-stage summary.

Only an explicitly labeled “append-only content” / “仅追加内容” is a fragment rather than a full replacement. Record strategic changes in the Change Log so earlier decisions remain traceable.

# Change Log

## 2026-10-01 — Companion-0 Completion / Companion-1 Begins

- Marked Companion-0 **COMPLETE** after the full TinyStories → tokenizer → Transformer → training → checkpoint → autoregressive inference pipeline.
- Recorded 10,956,351 tokens, 7,321,088 parameters, MPS execution, the 10-step training sanity run, and loss 9.1568 → 7.7127.
- Recorded `companion_0_checkpoint.pt`, first generation prompt, observed output character, and the limits of the training / inference conclusions.
- Preserved tokenizer design decisions, special-token rules, neural-network learning notes, architecture, compute timing rules, and prior learning methodology.
- Retained Companion-0 as an educational / experimental baseline; shifted the main route away from continued from-scratch pretraining toward open-weight foundation models.
- Defined the broader Companion composition and clarified **Research serves Companion**.
- Added Build first / Research just in time / Reproduce to understand / Don't reinvent unknowingly principles.
- Expanded compute choice to Local Mac, Colab / Kaggle, rented Cloud GPU, and API; commercial APIs remain prototype / evaluation / auxiliary resources rather than a permanent sole dependency.
- Began Companion-1 with only `generate(context)` and replaceable Local / Cloud / API backends; named Qwen3.5-9B as the first candidate.
- Updated Current Phase and Immediate Next Step to implement the minimal Brain Interface and let Companion-1 speak through its first open-weight foundation model.
- Established complete-replacement state-file updates with historical preservation and a dated Change Log.
