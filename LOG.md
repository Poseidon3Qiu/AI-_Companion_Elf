# Project Companion --- LOG

Created: 2026-10-02\
Conversation coverage: Companion-1 local Brain setup through first
Brain-Swap Test and transition to Persistent Experience.

## 1. Starting Point

The active C1 sequence was:

``` text
Quantized Local Brain
→ measure local constraints
→ minimal generate(context)
→ replacement test
→ persistent experience
→ observe retrieval problem
→ embeddings only if justified
```

The purpose was not to optimize one model. The purpose was to establish
a replaceable intelligence boundary while preserving the larger C1
research goal: artificial continuity.

## 2. Repository Reorganization

The completed Companion-0 baseline was moved under:

``` text
companion0/
```

and active Companion-1 work uses:

``` text
companion1/
```

The project-level `.venv`, Git repository, state files, and project
documents remain shared.

After the move, `companion0/model/generate.py` was run successfully. The
tokenizer and saved checkpoint still loaded and generation still
executed, confirming that the C0 baseline remained usable after
reorganization.

## 3. Python / MLX Environment Repair

The existing project `.venv` was retained rather than creating another
environment.

Its pip installation was broken (`No module named pip._vendor`). The
broken pip package files inside the project `.venv` were removed, pip
was restored with `ensurepip`, and then upgraded.

The project environment was verified to import MLX and MLX-VLM
successfully.

Relevant installed components included:

``` text
mlx 0.32.3
mlx-metal 0.32.3
mlx-vlm 0.7.4
mlx-audio 0.5.7
transformers 5.18.0
```

An accidental global Python package change was also cleaned up so the
Companion experiment remained isolated from unrelated Python
installations.

## 4. First Local Brain --- Qwen3.5-9B 4-bit + MLX

Selected model:

``` text
mlx-community/Qwen3.5-9B-4bit
```

Hardware:

``` text
MacBook Pro
M1 Pro
16 GB unified memory
```

The model downloaded and reconstructed successfully and produced a valid
first response.

Observed short-run measurements across several runs were approximately:

``` text
Generation speed: ~31–32 tokens/s
MLX-reported peak memory: ~6.07 GB
```

Prompt throughput varied substantially between runs, so it was not
treated as a stable benchmark.

The important conclusion was limited: this quantized 9B-class model is
practically runnable on the current machine for short inference tests.
The experiment did not establish long-context behavior, sustained-load
stability, or a final production model choice.

## 5. Minimal Brain Backend

`brain.py` was used for the MLX/Qwen backend.

The initial public concept remained:

``` python
generate(context)
```

The model was later changed to lazy loading so importing the Brain layer
would not automatically consume memory by loading Qwen when another
backend was selected.

Conceptually:

``` text
import backend
→ no model load yet
→ first MLX generate()
→ load Qwen
→ reuse loaded model on later calls
```

## 6. BrainResult

A project-owned result type was introduced:

``` text
BrainResult
```

Its purpose is to prevent the rest of Companion from depending on the
native return type of MLX, Ollama, or future providers.

It currently supports fields such as:

``` text
text
model
backend
prompt_tokens
generation_tokens
prompt_tps
generation_tps
peak_memory
finish_reason
```

Backends are not required to fabricate measurements they do not
currently expose. Unsupported values can remain `None`.

This was an important refinement: having two functions both named
`generate(context)` is not enough if they return incompatible
structures.

## 7. Second Local Brain --- Llama 3.1 8B + Ollama

Ollama was already installed, but initially had no models.

Downloaded:

``` text
llama3.1:8b
```

The model successfully responded through:

``` text
ollama run llama3.1:8b ...
```

A minimal `ollama_brain.py` adapter was then created using
`subprocess.run(...)`.

The Ollama adapter was changed to return the same `BrainResult` type as
the MLX backend.

The current subprocess implementation is intentionally minimal. A future
Ollama HTTP/API adapter could expose richer metrics and remove the CLI
subprocess layer, but this is not required for the current continuity
experiment.

## 8. Why Qwen Was Not Moved Into Ollama

Qwen currently uses an MLX-format model in the Hugging Face cache, while
Llama is managed by Ollama.

Converting/importing the MLX Qwen model into Ollama was not pursued
because it could create duplicate model storage and would weaken the
experiment by making both candidate Brains depend on the same runtime
manager.

Keeping:

``` text
Qwen → MLX
Llama → Ollama
```

makes the replacement test stronger: both the model and runtime can
change while the Companion-facing boundary remains stable.

## 9. Unified Brain Interface

A minimal `brain_interface.py` was introduced with the conceptual public
call:

``` python
generate(context, backend="mlx")
generate(context, backend="ollama")
```

The rest of Companion should not need to know about MLX, Ollama,
Qwen-specific behavior, or Llama-specific behavior.

The intended boundary is:

``` text
Companion
    ↓
Brain Interface
    ↓
Backend Adapter
    ├── Qwen / MLX
    ├── Llama / Ollama
    ├── future GPT adapter
    └── future Claude adapter
```

Model-specific protocol differences belong inside the adapter layer.

## 10. First Brain-Swap Test

The same context was sent through both backends:

``` text
Explain in one short sentence what memory means for an AI companion.
```

The MLX path successfully invoked Qwen and returned:

``` text
Model: mlx-community/Qwen3.5-9B-4bit
Backend: mlx
```

The Ollama path successfully invoked Llama and returned:

``` text
Model: llama3.1:8b
Backend: ollama
```

Therefore the first minimal Brain-Swap Test succeeded.

The important result is architectural, not a judgment about which model
is better:

``` text
same Companion-facing interface
→ different model
→ different runtime
→ normalized result
```

This establishes the minimum Replaceable Intelligence boundary required
for the next C1 work.

## 11. Qwen Thinking / Chat-Template Issue

During the swap test, Qwen emitted reasoning-style content beginning
with `<think>` and used the 100-token generation budget before reaching
a concise final answer.

An attempted `enable_thinking=False` change at the generation-call level
did not solve the behavior.

Investigation indicated that Qwen's model-specific chat template /
prompt protocol needs proper backend handling rather than passing a raw
string directly.

This led to a broader architectural observation:

``` text
model/runtime differences
+
prompt protocol differences
→ should terminate inside the backend adapter
```

However, continuing to investigate Qwen-vs-Llama output behavior was
judged to have diminishing value for the current C1 objective.

Decision:

**Record the Qwen thinking/chat-template behavior as a known backend
issue and defer it.**

It does not block the central continuity experiment.

## 12. Decision: Stop Model Comparison

The session explicitly rejected spending further time comparing Qwen and
Llama differences.

The purpose of the two-Brain experiment was to prove replaceability, not
to benchmark or rank the models.

That proof is now sufficient for the current stage.

Future model/backend adaptation should happen only when a concrete
incompatibility blocks Companion behavior.

## 13. New Resume Point --- Persistent Experience

The main path now advances to:

``` text
User
→ Companion
→ Brain
→ Response
→ save Experience

later interaction
→ load prior Experience
→ provide relevant continuity context
→ Brain
→ response informed by prior experience
```

The first implementation should remain simple and inspectable.

Do not begin with:

``` text
vector database
embedding pipeline
complex memory taxonomy
large retrieval framework
```

Instead:

1.  Save a small number of real experiences.
2.  Reuse them in later interactions.
3.  Observe what fails as the experience set grows.
4.  Introduce retrieval/embeddings only when the observed problem
    requires them.

This preserves the project's project-first / just-in-time learning
principle.

## 14. Current Open Issues

-   Design the smallest Persistent Experience representation.
-   Decide when an interaction becomes durable experience.
-   Preserve provenance so later Brains can reinterpret important
    memories.
-   Keep durable state under Companion control rather than
    model-provider control.
-   Observe when naive experience loading becomes insufficient.
-   Revisit Qwen chat-template normalization only if it becomes relevant
    to the active experiment.
-   Later measure continuity across Brain swaps rather than comparing
    models in isolation.

## 15. Exact Resume Instruction

Resume with **Companion-1: First Persistent Experience**.

Do not return to Qwen/Llama comparison unless it blocks the next
experiment.

Build the simplest transparent persistence path first, then perform a
real two-interaction continuity test.

# Project Companion — Baseline Discussion Log

Created: 2026-10-02
Coverage: Project Companion inception through 2026-10-02
Timezone for date labels: America/Los_Angeles
Log type: First recovered project-wide baseline; organized research/development journal, not a verbatim transcript.

## 1. Sources, coverage, and reconstruction limits

This baseline combines the uploaded `sources/CURRENT_STATE.md` (1,479 lines), the older root STATE (602 lines), five project reference texts, the supplied conversation preview, and retrievable ChatGPT messages. The newer uploaded STATE is the primary state baseline; the older root file must not overwrite newer strategic decisions.

Read reference material: `项目概述.txt`, `最初动力源-9-28-2026晚.txt`, `学习路径0.0枯燥版.txt`, `学习路径0.0.txt`, and `AI应该有自己的高效编程语言.txt`. Synced source files are read-only and were not changed.

Recovered conversations:

| Conversation | ID | Recoverable content |
| --- | --- | --- |
| 解释Marin模型 | 6abb5af3-9a68-83e8-b5cb-df8f376c9569 | Motivation, original learning-route objections, AI-native computing question |
| Begin | 6abb6495-a894-83e8-a80a-a6238a444ec2 | Genesis README and first commit learning |
| C0-Concept0 | 6abc4800-0144-83e8-a46a-32d53c5ba705 | Tokenizer-before-Transformer correction, actual project directory and Python |
| C0-Tokenizer build0 | 6abd5de9-2d08-83e8-9b73-1f29111416d0 | BPE merges, vocabulary hyperparameter and 8K choice |
| C0-Tokenizer build1 | 6abd8857-bbbc-83e8-865a-32c710a431e3 | Tokenization measurements, performance deferral, EOS discussion |
| C0-Embedding0 | 6abdd70f-8838-83e8-932a-54552f57e694 | B/T/C and positional-information questions |
| C0-Transformer0 | 6abeb430-1440-83e8-91d9-a3277855ce07 | Numerical representation insight, logits/token-choice distinction |
| C0-Loss/backprop/gradient/Training loop | 6abee66e-5654-83e8-a8e6-b9f932ec2718 | Git push output and full-state update requests |
| 讨论C1开始的未来方向 | 6abf259f-7850-83e8-bdc9-fe4834698671 | Cumulative preservation and final STATE/LOG separation |

The thread reader returned bounded excerpts, often only five recent turns, with no older-page cursor even when ten turns were requested. Some assistant messages are cut off; images and attached-file contents are absent from these excerpts. This is the most complete reconstruction supported by available material, not a claim that all original chat turns were retrieved. Earlier C1 arguments are often recoverable only from STATE's synthesis. Exact chronology within a day, missing direct quotations, unseen screenshots, unavailable generated text, model-install results and missing experiments are not invented. Dates are used where source records provide them; thematic ordering elsewhere is not a fabricated timestamp.

Historical third-party model, service and hardware discussions below record what was considered then. They are not fresh provider/pricing recommendations or independently verified current product claims.

## 2. Inception: from fictional companion to personal AI research

The Genesis README excerpt explicitly records childhood attraction to Pokémon, Digimon and intelligent companion creatures; the current request also identifies 御兽-style companionship. The desired relationship is richer than battles or novelty: communication, understanding, a distinct personality, shared memories, help with difficult problems and growth over years.

Marin/open-research discussion supplied another motivation: owning an AI should involve understanding how it is made, not merely downloading an artifact. The reference contrasts open weights with open training knowledge—data recipes, training code, checkpoints, loss, failures and operational know-how. Large shared models and smaller local derivatives were discussed as different scales of participation. Numbers in the Marin reference are historical discussion context, not independently verified by this log task.

The user wanted eventually to understand and contribute to such research and to manufacture an individually distinctive LLM. The assistant connected shared foundation intelligence with personal experience: base intelligence can be shared while memory, training and interaction histories diverge. That was a research direction, not proof of a digital individual or consciousness.

### Not merely a wrapper; objective critique

The initial mission rejected stopping at an API UI or a “You are…” personality prompt. The ambition is to understand and shape the mechanisms behind memory, continuity and growth. Later acceptance of existing foundation models does not erase this goal: individuality belongs to the Companion system and its learning history, rather than requiring a privately pretrained frontier model.

The current user request explicitly requires objective, non-accommodating judgments. Preserve limitations, criticize unrealistic assumptions and distinguish a working pipeline from useful intelligence. The original full conversation establishing this requirement is not recoverable; no invented quotation or attribution is supplied.

## 3. Traditional learning path and why it changed

The original “枯燥版” proposed roughly two to three years of structured preparation. It began with mathematics and ML foundations—vectors, matrices, probability, derivatives, gradients, chain rule, regression, MLP, backpropagation and optimizers—then deep learning, Transformer, pretraining, post-training, memory, agents, continual learning and multimodal work. Understanding and implementing mechanisms was favored over only calling APIs. The schedule and larger 100M–1B ambitions were proposals, not completed milestones.

The user did not reject rigor or gradual learning. The explicit objection was that waiting too long before touching the real subject would damage motivation and enjoyment. They wanted to build in a real environment immediately, encounter obstacles and learn the necessary knowledge to overcome them.

The revised method became **Project-first + Research-first + Just-in-time Learning**, approximately **70% Build / 20% JIT learning / 10% systematic foundations**. This is a guiding allocation, not a measured time sheet. Companion is the main quest; attention, cross entropy, memory limits and other topics are skill branches that return to building. The 2026-10-01 clarification was “Research serves Companion”: research should solve a concrete problem, and reproduction should deepen understanding without obliging the project to rebuild every mature component.

### Teaching failure and accepted correction

In C0-Concept0, the assistant had treated understanding token/BPE theory as completion of the tokenizer stage and moved toward Transformer. The user challenged why real tokenizer construction appeared only after their question. The assistant accepted the criticism and distinguished **Concept understood**, **Component built**, and **Component verified**.

The resulting rule was **Understand → Build → Verify → Module Complete**, followed by deciding whether to open a new conversation. The assistant should proactively stop unnecessary theory, announce genuine completion and provide a transition when a new chat is useful. This is a concrete correction to teaching behavior, not just a slogan.

## 4. Two long-term tracks and AI-native computing

**Track A — Personal / Open LLM** includes Transformer, pretraining, post-training, SFT/LoRA/DPO/RL, Identity, Personality, long-term Memory, continual learning and multimodal/agent work.

**Track B — AI-native Computing** includes computer architecture, OS, compilers, LLVM/MLIR, CUDA/GPU, distributed systems, program synthesis, learned systems and AI-native runtime. The intention is eventual convergence, not simultaneous implementation of both complete stacks at C1.

The user asked why AI must express computation using languages designed around human readability such as Java/Python, and whether it could invent a more direct, efficient and precise interface to hardware/resources. Discussion explored AI-generated IR, execution graphs, learned representations and runtimes that translate goals and constraints into computation; language syntax itself may not be the essential intermediate layer.

Existing ecosystems explain the practical use of conventional code: operating systems, compilers, libraries and accelerator runtimes already exist. Bypassing source-language syntax is a research possibility, not evidence that an unreadable representation is automatically faster or correct. The source's hypothetical efficiency figures are illustrations, not measured results.

Verification remained a central constraint: human specifications, formal checks, auditing, permissions and reliable execution may become more important as generated computation becomes less readable. No new AI language, compiler, operating system or runtime has been built in the recorded baseline. Track B stays a long-term research direction rather than a prerequisite to the first Companion interaction.

## 5. Genesis, tooling and the meaning of history

The recovered Begin conversation records **DOC-001 — Project Genesis / README v1.0** in English first, Chinese second. The README explains origin, mission, tracks, learning philosophy, roadmap, privacy and research questions. The assistant initially assumed a web edit might already be committed; the user clarified it was not. The subsequent first-commit lesson treated a commit as a meaningful permanent project-history point.

The recovered assistant records Genesis and first-commit completion on 2026-09-29. The milestone title was `DOC-001: create Project Genesis README v1.0`. Images are unavailable to this retrieval, so screenshot-based confirmation is a historical assistant report, not a newly inspected image.

Tool learning should occur when needed: do not continue into branches/PRs/clone merely to finish a Git syllabus. Preserve meaningful failures and versions as research data. Repository history is more than a cloud folder.

C0-Concept0 provides the actual user-reported development location `/Users/Poseidon/desktop/Keep Studying/AI_Companion_Elf`, with `data/` and `tokenizer/`, and Python **3.10.8**. A separate venv was proposed to isolate dependencies. This document mirror is not that implementation repository; no implementation code was rerun here.

## 6. Companion-0: first model from random weights

The first build aimed at a small model, originally about **10M–50M parameters**, to experience the whole route from text to trained parameters and generation. Capability was secondary to understanding. Early version ideas included dataset/tokenizer improvements, instruction tuning, personality and memory; they were illustrative roadmap versions, not proof those versions were built. Later C1–C5 framing supersedes treating that list as a rigid schedule.

### Corpus and tokenizer

TinyStories supplied a controllable **50,000-story** subset. Recorded prepared paths are `data/processed/tinystories_50k.jsonl` and `.txt`; the text file trains the tokenizer. The project used **byte-level BPE**, **8,000 vocabulary entries**, and a version-controlled `tokenizer/tokenizer_v0.json`.

The BPE lesson used `low`, `lower`, `lowest`: count adjacent pairs, merge a frequent pair, recount, and continue. Ties show that a merge path can require a deterministic convention. BPE frequency compression does not imply understanding the word's meaning. The illustrative `</w>` marker was part of the teaching example, not evidence that the final byte-level tokenizer uses that marker.

The user correctly identified vocabulary size as a human-chosen hyperparameter. Smaller vocabulary tends to fragment text and increase sequence length; larger vocabulary grows embedding/output layers. **8K** was accepted as an initial experiment, not declared optimal. **8K vs 16K** remains an optional comparison of sequence length, efficiency, parameter count and downstream behavior.

User-reported measurement:

| Metric | Value |
| --- | ---: |
| Total tokens | 10,956,351 |
| Average tokens/story | 219.12702 |
| Total characters | 44,478,696 |
| Characters/token | 4.059626786326944 |

The user asked what controls a slow run and how to accelerate it, then chose to continue the main learning path and defer optimization. This does not mean runtime is irrelevant; later explicit time-to-result rules require benchmarks for substantial jobs. The exact handling of special tokens in this measurement is not available.

### Special tokens and a boundary disagreement

Tokenizer v0 records **EOS yes; BOS/PAD/UNK no**. EOS marks story boundaries/endings, not every normal sentence; punctuation already represents sentence boundaries. The user questioned whether placement mattered enough to delay the main path. The retained decision keeps the important story-boundary distinction while avoiding a detached deep dive.

Registering a special token and inserting it into a training stream are distinct operations. The uploaded STATE contains a truncated sentence about registration; its missing original words are not reconstructed as a quotation. The explicit insertion rule survives.

### Embedding and positional information

Token IDs are lookup indices, not meaningful numerical magnitudes. With vocabulary 8,000 and embedding dimension 256, a trainable table maps `[T]` to `[T,C]`, or `[B,T]` to `[B,T,C]`. The user asked what a batch and sequence mean and then confirmed understanding B/T/C: batch size, token-sequence length and representation channels.

The user challenged why position information is needed if tokens already appear in order. The retained distinction is that tensor storage order does not by itself provide position as a feature to ordinary attention. A deeper demonstration was deferred until needed. This illustrates JIT depth rather than skipping the concept.

### Attention, contextual representations and Transformer

The learned projections are `Q = X W_Q`, `K = X W_K`, `V = X W_V`. Query/key scores become normalized attention weights; outputs combine allowed value vectors. Causal positions cannot attend to future tokens. These outputs are new hidden states, not overwrites of the embedding table.

The 256-channel, eight-head example gives head dimension **32**. Head outputs concatenate and project back to 256. Residual additions preserve incoming representations while adding changes. Feed-forward layers transform each token independently, conceptually 256 → 1024 → 256. LayerNorm stabilizes representations, and serial blocks have independent learned parameters while preserving the principal `[B,T,C]` shape.

The user articulated a key insight: numbers can encode information about the world, and computation can transform them into more useful representations. This learning moment connects numerical operations to language modeling. It does not claim that any arbitrary number inherently contains human meaning. Forward activations changing and training weights changing are distinct processes.

### Logits, targets, loss and optimization

The final projection transforms `[B,T,256]` into `[B,T,8000]`. The user explained that the model chooses a vocabulary token rather than one of the 256 representation coordinates. Raw scores are logits; softmax can provide sampling probabilities. Training targets are the token stream shifted by one position, enabling next-token supervision at multiple positions.

The completed workflow includes cross-entropy, backward gradients and **AdamW** updates. The record preserves basic learning/implementation completion, not mastery of every underlying derivation. Detailed intermediate lesson wording and every run/error are unavailable.

### Recorded completed model and first sanity run — 2026-10-01

```text
embedding_dim = 256
num_heads = 8
num_layers = 4
max_seq_len = 256
parameters = 7,321,088
Architecture: causal attention, Pre-LN blocks, GELU FFN
Device: PyTorch MPS on M1 Pro
batch_size = 8
seq_len = 256
learning_rate = 3e-4
optimizer = AdamW
steps = 10
loss: 9.1568 (step 1) → 7.7127 (step 10)
```

MPS availability/build were reported true. The actual model is below the original planning range; preserve target and result rather than silently altering history. Ten steps validate initial forward/loss/backward/update plumbing. They do not establish convergence, generalization, coherent language or held-out performance. The corpus token total is not the number processed in the run.

The checkpoint is recorded as **`companion_0_checkpoint.pt`**. Exact serialized fields and current location are unavailable. Autoregressive inference began with **“Once upon a time”** and produced incoherent but English-like token sequences. Exact generated text is not recoverable. The successful end-to-end pipeline is the milestone; useful Companion dialogue is not demonstrated.

C0 remains an educational/experimental baseline. Future from-scratch work may answer focused questions; continuing pretraining is no longer the primary route toward Companion.

## 7. Git/GitHub baseline — 2026-10-01

The uploaded STATE preserves the local repository `AI_Companion_Elf`, GitHub repository `Poseidon3Qiu/AI-_Companion_Elf`, remote `origin`, and merged `main` tracking `origin/main`.

Recorded history:

- `5a219f4 Initial commit`
- `ad8332e DOC-001: create Project Genesis README v1.0`
- `7d709c3 Complete Companion-0 baseline`
- `eedab1a Merge existing GitHub history with Companion-0`

Local and remote histories were unrelated. A merge preserved both rather than force-pushing over the remote. The `.gitignore` add/add conflict was resolved with current local exclusions; remote README was preserved. The recovered user terminal output directly reports push **ad8332e → eedab1a** and tracking configuration.

Source/tokenizer/state are versioned; datasets, environments, caches and checkpoints are ignored. Ignoring a file does not delete it. Git source history alone does not back up the checkpoint. No fresh GitHub inspection, push or repository modification occurred during this documentation task.

## 8. From a commercial Personal AI goal to artificial-individual research

Early direction imagined a usable Personal AI with identity, personality, memory and growth. The C1 synthesis reframed the main task away from racing mature commercial products toward long-term **artificial continuity / artificial individual formation**.

The durable question became: **What makes an artificial intelligence persist as an individual across time, experience and replacement of its foundation model?** This changes what counts as progress: controlled experiments and understandable continuity mechanisms matter more than rapidly assembling every product feature.

The original project questions remain:

- Identity: weights, context, memory, or a distinct persistent structure?
- Personality: stable learned behavior beyond one prompt?
- Memory: episodic, semantic and autobiographical organization?
- Growth: experience-driven change without catastrophic forgetting?
- Individuality: divergent histories under the same starting foundation?
- Ownership: personal control, backup, migration and offline survival?

No evidence here establishes consciousness or solves these questions. The commercial-to-research turn is recorded in STATE; its complete original turn-by-turn debate is unavailable.

## 9. Brain independence and continuity

**“Replacing the Brain must not mean killing the Companion.”** The Brain is a replaceable intelligence substrate; Companion is broader than the foundation model. The conceptual formulation is **Persistent State + Learning Dynamics + Replaceable Intelligence**.

Persistent state includes memory, identity, experience/history, preferences, relationship patterns and reflection/learning history. Memory is foundational but not sufficient by itself: mechanisms must interpret, consolidate, forget and let experience influence future behavior. Ownership requires portability, auditability and practical recoverability even if a provider disappears.

C1's three coupled axes are **Brain Independence**, **Persistent State**, and **Learning & Reflection**. C1 first investigates continuity without editing base-model weights. Controlled adaptation, adapters/model editing and continual weight learning belong primarily to **C2 Growth**, after external continuity can be measured.

### Memory candidates, controlled writes and provenance

The Brain can interpret experience and propose a memory candidate. It should not possess uncontrolled final authority to write durable state. Source evidence and model inference must remain distinguishable so one model's mistaken summary does not become untraceable identity history.

Desired provenance includes source interaction, timestamp, fact/user-statement/inference classification, producing Brain/process, confidence where meaningful, and revision/consolidation history. These are requirements/directions, not an already implemented schema or confirmed policy engine. Important unresolved questions include acceptance rules, contradictions, forgetting, correction and how much reflection should influence identity.

### Brain-Swap research

Hold persistent Memory + Identity + Experience constant; change Qwen/Llama/GPT/Claude/future Brain; compare memory recall, identity/preference consistency, relationship continuity, behavior drift and reasoning quality. This probes what belongs to the base model versus project-controlled state. It is a proposed controlled experiment, not a reported result or proof that every swap preserves individuality.

## 10. Development rhythm: progress now, long experiments in parallel

The accepted rhythm is **short-cycle continuous progress + spiral revisiting + longitudinal experiments in parallel**. A long-term identity question should not make elapsed time the project's main daily task.

Sessions should produce a working capability, necessary understanding, measurement, reproduced mechanism, discovered failure or improved research question. Revisit Memory, Identity, Reflection, Learning and architecture at deeper levels as real needs appear. Months-long observations can accumulate alongside this work.

Control variables for individual experiments; do not freeze the entire roadmap or prohibit all Brain changes while awaiting a longitudinal result. The source records this principle, but not a complete original debate or a running longitudinal dataset.

## 11. Local Companion Core, replaceable Brain and Context Firewall

The preferred direction is **Local Companion Core / Replaceable Cloud Brain**, with a local Brain also required. “Cloud provides compute; Local owns continuity” and “Rent compute, not the Companion” summarize the ownership boundary.

Local Core should retain authoritative persistent state, provenance, history and eventually context building/memory management. Remote compute primarily supplies replaceable inference. The same boundary can support local models, cloud-hosted open-weight models or commercial APIs. Open weights may support fixed-version experiments and later controlled training; API models remain useful for comparison or difficult tasks.

Local persistence does not imply no disclosure to a remote Brain. A remote Brain receives selected working context. The future Context Firewall should filter by relevance, sensitivity, permissions, provenance and minimum necessary disclosure rather than uploading complete persistent history by default. This is an architectural direction; no implemented privacy filter or measured leakage guarantee is claimed.

## 12. API tokens and API's limited role

An API credential/token grants service access; language-model tokens are text-processing units. Neither possessing a credential nor paying for inference establishes ownership of a Brain's weights or a Companion's identity.

The recorded compute policy uses API for prototyping, evaluation, comparison and auxiliary assistance, with replaceability tests also possible. A commercial API must not become the permanent sole dependency or authoritative continuity store. The full original discussion specifically explaining API tokens is not available in source text/recovered excerpts; this section states the retained role and terminology boundary without pretending to reproduce missing exchanges. No secrets are included.

## 13. Cloud GPU, student/free resources and scope critique — 2026-10-02

The embedded STATE discussion starts from whether cloud models always require rented GPUs and whether student/free resources can help. Considered categories include student/research credits, Colab, Oracle Cloud, Runpod/commercial GPU rental and local inference; the wider compute policy also mentions Kaggle, Azure and GCP as possible resources.

The useful part accepted was compute independence and experiment-specific choice. Claude criticized operating Mac + Runpod + Oracle + Colab as parallel environments at this early stage. That scope critique was substantially accepted: the Companion boundary needs replaceability, not a multi-cloud engineering project.

Result: use local experimental Brain plus **at most one primary Cloud GPU environment when actually needed**. Oracle infrastructure learning may be valuable separately; Colab may be a temporary notebook; neither is a mandatory main-path dependency. Do not equate a provider's free/student tier with guaranteed suitable GPU access. No recovered credit amounts, eligibility approval, GPU allocations or precise price quotation can be reproduced reliably.

GPU/provider selection is **just in time**, based on actual model, VRAM, precision, context length, inference/training mode, runtime, setup, available credits and then-current pricing. Historical price discussion does not justify choosing a provider months ahead.

Time-to-result includes setup/upload/migration, not just GPU throughput. Retained heuristic: under 5 minutes local is fine; 5–15 minutes usually acceptable; at least 15 minutes evaluate acceleration; at least 30 minutes benchmark and seek effective faster resources before defaulting to slow local execution. A short appropriate benchmark should estimate throughput, duration, memory and device. This rule complements the user's earlier deferral of premature tokenizer optimization.

## 14. M1 Pro 16 GB correction and quantization

The earlier shorthand “M1 Pro + 7B/9B → Local Brain” omitted precision. Claude identified that approximate FP16 weights alone require **14 GB for 7B** and **18 GB for 9B**, before macOS, runtime, KV cache and other allocations. The critique was accepted.

The project did not abandon the local Brain or assume all 7B/9B candidates are impossible. It corrected the plan to quantized inference, beginning with the recorded candidate **Qwen3.5-9B MLX 4-bit**, with smaller models such as 4B as fallback. Four-bit weight size does not equal complete runtime memory; speed, quality, memory pressure and stability need measurement.

The first local experiment should record exact artifact/version, quantization, size, load time, memory pressure, generation speed and stability. No successful installation or local Qwen benchmark is reported in the material. Candidate naming reflects the historical decision and is not a newly verified availability claim.

## 15. Embedding disagreement and final immediate order

Claude proposed Embedding as the immediate next topic. That sequencing was rejected, while the expected future importance of embeddings was retained. Starting retrieval machinery now would prematurely assume a memory architecture before the minimal replaceable Brain works.

The agreed sequence is:

1. Run quantized Local Brain.
2. Measure real constraints.
3. Wrap it behind **`generate(context)`**.
4. Test replacement without changing Companion-level calling code.
5. Record first persistent experiences under controlled ownership.
6. Observe real retrieval problems.
7. Compare retrieval options and introduce embeddings when justified.

C0 token embedding and C1 retrieval embedding are distinct uses. Learning `nn.Embedding` in the training baseline does not mandate a vector database as the next step. Conversely, delaying retrieval embeddings does not reject them forever.

The uploaded STATE still contained an older interface-first resume paragraph alongside this later local-first sequence. This documentation update reconciles the front-page resume point to the later agreed sequence. No full Memory/Identity/Agent system should be designed before the first Brain interaction.

## 16. Roadmap and unresolved research

Current stage direction: **C1 Continuity → C2 Growth / Continual Learning → C3 Agency → C4 Embodiment → C5 AI-native Computing**. It is a research direction, not a rigid waterfall or a set of completed features.

Open questions remain:

- What local candidate offers acceptable quality, memory, speed and stability on this machine?
- What is the smallest useful replaceable Brain contract?
- What survives model swaps, and how should continuity/individuality be measured?
- How should memories be accepted, revised, consolidated and forgotten without erasing provenance?
- How can experiences alter behavior while preserving an auditable identity history?
- When does simple storage stop meeting retrieval needs, and which mechanism should then be added?
- How should Context Firewall decisions be enforced and measured?
- When is controlled weight adaptation justified beyond external memory/reflection?
- Which remote compute and credits fit the next actual experiment?
- How can Track B experiments improve computation while remaining correct and verifiable?

Optional C0 questions—8K/16K vocabulary, data/tokenizer changes and longer training—remain historical research opportunities, not C1 prerequisites.

## 17. State-recording制度的三阶段演变

### A. Cumulative STATE, full replacement delivery

The user repeatedly requested the complete CURRENT_STATE and confirmed cumulative preservation. The rule was to use the previous full file, retain milestones/experiments/learning/architecture history, append new records and change only obsolete current descriptions. Full replacement refers to delivering the entire file, not overwriting history with a short summary. The user should not have to manually combine fragments unless explicitly requesting append-only content.

### B. Same-day cumulative STATE + Detailed Discussion Log

On 2026-10-02 the user requested recording reasoning as well as conclusions. The assistant added a Detailed Discussion Log Policy and reported a baseline of 1,354 lines becoming 1,479. It captured assumptions, critique, accepted/rejected arguments, decisions and questions. The Cloud/quantization/multi-cloud/Embedding log in the uploaded source is the concrete first example.

This intermediate rule was real and remains in historical Change Log. It is not erased or retroactively described as never adopted.

### C. Final STATE / LOG separation

The user then explicitly proposed two Markdown files when saying **“更新 state and log”**. STATE remains cumulative and authoritative for new-chat recovery. LOG becomes the detailed organized journal of the current conversation, with creation date and coverage at its start for direct appending to a local master log.

This first LOG has a deliberate exception: recover project-wide history from inception through 2026-10-02. Future logs do not copy all older logs by default. STATE preserves historical milestones, measurements, architectural evolution, learning outcomes and Change Log, but stops accumulating detailed chat narratives. The previous embedded discussion is migrated here; the intermediate policy's historical record remains in STATE.

## 18. This update's concrete outcome and resume boundary

Generated complete CURRENT_STATE.md from the newer uploaded baseline, preserved its substantive records and all Change Log entries, restored source-backed tracks/motivation and recovered tokenizer measurements, replaced active discussion-in-STATE policy, and placed recovery fields/resume order at the beginning.

Generated this first baseline LOG from all retrievable material listed above. No implementation experiment, new model deployment, cloud account setup, Git push, claim of useful C0 intelligence or successful Brain-Swap occurred in this document task. Missing history remains explicitly missing.

Resume actual development with the first quantized Local Brain attempt and measurements, then the minimal `generate(context)` boundary. Continue short build/research cycles while retaining source evidence and recording actual outcomes.

---

## Appendix — Migrated original embedded discussion record

The following section is preserved from the uploaded STATE so the reasoning log is relocated rather than discarded. Its closing instruction to keep detailed discussion in STATE is historical and superseded by Section 17C above.


## 2026-10-02 — Cloud Cost, Local Brain Constraints, Scope Control, and Learning Order

### Starting Question
The discussion began with whether cloud-deployed models always require paid rented GPUs and whether student/free alternatives exist.

### Initial Direction
Student credits, Colab, Oracle Cloud, commercial GPU rental, and local inference were considered. The useful architectural principle was that remote compute must remain replaceable and must not own Companion continuity. However, planning many environments at once risked unnecessary scope creep.

### Local 7B/9B Constraint
Claude challenged the earlier shorthand `Mac M1 Pro + 7B/9B → Local Brain`. The critique correctly identified the 16 GB unified-memory constraint: FP16 weight memory alone is roughly 14 GB for 7B and 18 GB for 9B, before macOS, runtime overhead, KV cache, and other memory use.

This critique was accepted. The corrected direction is a quantized Local Brain, initially exploring approximately 7B–9B-class models only when measurements show they are practical. This also creates a JIT-learning topic around quantization, memory representation, quality tradeoffs, and Apple Silicon inference.

### First Local Brain Candidate
`Qwen3.5-9B MLX 4-bit` was selected as the first candidate, not a permanent commitment. A smaller quantized model remains a fallback if real measurements show unacceptable memory pressure, speed, or stability.

The experiment must measure model/version, quantization, size, memory pressure, load time, generation speed, and stability.

### Multi-Cloud Scope Critique
Claude argued that Mac + Runpod + Oracle + Colab as parallel operational environments was excessive for the current stage. This was substantially accepted.

Project Companion's main line is distinct from general Cloud Engineering learning. Oracle may be useful for separate infrastructure learning; Colab may be useful as a disposable notebook; a commercial GPU provider should be selected only when a concrete remote-compute experiment requires one.

Resulting principle:

> Cloud infrastructure itself is replaceable infrastructure.

### GPU Pricing
Specific prices were discussed, but the durable conclusion is not to optimize volatile GPU pricing months in advance. Provider/GPU selection should occur just in time using the actual model, VRAM, training/inference mode, precision, context length, expected runtime, available student/research credits, and then-current pricing.

### Disagreement: Embedding as Immediate Next Step
Claude proposed Embedding as the immediate next step. That sequencing was not accepted.

Embedding is expected to become important, but beginning there would prematurely assume a memory/retrieval architecture before the minimal replaceable Brain boundary exists.

The preferred project-first sequence is:

```text
Local Brain
→ measure it
→ Brain Interface: generate(context)
→ replaceability test
→ first persistent experiences
→ real retrieval problem emerges
→ evaluate retrieval mechanisms
→ Embedding when justified
```

This preserves the project's JIT-learning rule: build first, encounter a real problem, learn the required mechanism, experiment, then improve Companion.

### State-Recording Process Change
The discussion also identified that preserving only final decisions is insufficient for a long-running research project. Future `CURRENT_STATE.md` updates must therefore preserve both current conclusions and the important reasoning path beneath them.

The Detailed Discussion Log should capture:
`question/assumption → critique/evidence → accepted/rejected points → decision → open questions`.

This becomes the default rule for all future state updates.

### Open Questions
- How well will Qwen3.5-9B 4-bit actually run on the M1 Pro 16 GB machine?
- What are the measured quality/speed/memory differences between smaller and larger local candidates?
- What is the smallest useful Brain Interface before overengineering begins?
- At what point does simple episodic storage create a real retrieval problem?
- Which retrieval mechanism should be introduced first when that happens?
- When remote GPU compute is actually required, which provider/credits are best at that time?


