# AI Companion Elf

> **Don't just use an LLM. Learn how to raise one.**

**Building a personal AI companion with persistent identity, memory, personality, and the ability to learn and grow over time.**

---

# English Version (中文版在后半部分，如有需要可直接跳过英文版)

## 1. Origin — Why This Project Exists

This project began long before I knew what a large language model was.

Growing up, I was fascinated by stories such as **Pokémon**, **Digimon**, and novels centered around intelligent companion creatures.

What attracted me was not simply the fantasy, the battles, or the supernatural abilities.

It was the idea of having an intelligent non-human companion of my own:

- one that could communicate with me,
- understand me,
- develop its own personality,
- remember the experiences we shared,
- help me when I encountered difficult problems,
- and grow alongside me over many years.

For most of my life, such a companion belonged entirely to fiction.

The emergence of modern artificial intelligence, especially large language models, changed that assumption.

Today's AI is still far from the kind of companion I imagined. A chatbot with a system prompt is not a persistent individual, and an API connected to a user interface is not a digital life companion.

But for the first time, there appears to be a plausible technological path toward building pieces of that idea.

Foundation models can provide intelligence.

Post-training can shape behavior.

Memory systems can preserve experience.

Multimodal models can provide vision and hearing.

Agents can interact with tools and computers.

Continual learning may eventually allow an AI to change through experience.

Virtual avatars, spatial computing, augmented reality, and robotics may provide different forms of embodiment.

This project begins with a simple question:

> **How much of that childhood idea can actually be built?**

I do not know the answer.

Project Companion exists to find out.

---

## 2. Mission

> **Build an AI that can be owned, understood, shaped, and grown by an individual.**

The goal is not simply to build another chatbot.

It is not to place a system prompt around an existing model and call it a personality.

It is not to build another wrapper around a commercial AI API.

The long-term goal is to understand and experiment with the technologies required to create a personal AI companion that can develop:

- persistent identity,
- stable personality,
- long-term memory,
- autobiographical experience,
- personal knowledge,
- skills,
- perception,
- agency,
- and eventually the ability to learn and grow over time.

The foundation model may provide general intelligence.

But intelligence alone does not define an individual.

The central hypothesis of this project is:

> **Intelligence may begin from a shared foundation, but identity emerges from experience.**

Two companions may begin from the same base model.

If they live with different people, accumulate different memories, develop different preferences, learn different skills, and experience different histories, they should gradually become meaningfully different companions.

Understanding whether and how this can happen is one of the central research goals of Project Companion.

---

## 3. What Is a Companion?

The project is organized around four major dimensions:

### Track A — Mind

How does the Companion think and learn?

This track studies the foundations of language-model intelligence:

- Data
- Tokenization
- Embeddings
- Transformers
- Attention
- Pretraining
- Optimization
- Evaluation
- Inference
- Open foundation models
- Fine-tuning
- SFT
- LoRA
- Preference learning
- DPO
- Reasoning and capability development

The first objective is not to download an existing model.

It is to train a small language model from random weights and personally experience the entire process:

**Data → Tokenizer → Transformer → Pretraining → Checkpoint → Inference**

This will become **Companion-0**.

---

### Track B — Self

Why is this Companion *this particular Companion*?

This is one of the most important long-term research tracks of the project.

It explores:

- Identity
- Personality
- Values
- Preferences
- Behavioral consistency
- Episodic memory
- Semantic memory
- Autobiographical memory
- Experience
- Reflection
- Memory consolidation
- Continual learning
- Individuality
- Identity continuity

A future Companion should not merely know facts about its human.

It should possess a history.

It should be able to remember meaningful shared experiences and allow those experiences to influence future behavior.

This raises a deeper question:

> **Where does an AI's identity actually live?**

In its weights?

Its memory?

Its context?

Its training history?

Its interaction history?

Or in some combination of all of them?

Project Companion does not assume that this question has already been solved.

It intends to investigate it experimentally.

---

### Track C — Presence

How does the Companion move beyond the chat window and become part of everyday life?

A long-term companion cannot require its human to repeatedly open an application, explain the situation from the beginning, ask a question, receive an answer, and close the application.

The Companion should eventually be capable of:

- Voice interaction
- Hearing
- Vision
- Multimodal perception
- Environmental awareness
- Context awareness
- Persistent presence
- Tool use
- Computer interaction
- Planning
- Agency

The interaction model should gradually evolve from:

**Human → Question → AI → Answer**

toward:

**Human ↔ Companion ↔ World**

A good Companion should also learn when *not* to act.

Persistent presence should not mean constant interruption.

It should eventually understand when to speak, when to help, when to observe, and when to remain silent.

---

### Track D — Embodiment

What does the Companion look like, and how does it exist in the physical or virtual world?

The Companion's body should not define its identity.

Its embodiment may change over time:

**2D Avatar → 3D Character → AR/VR Presence → Spatial Computing → Physical Device → Robot**

One day it may appear on a computer screen.

Another day it may exist as a spatial character through augmented reality.

In the future, it may interact with the physical world through a robotic body.

The interface may change.

The body may change.

But the Companion should remain the same individual.

This leads to another long-term principle:

> **The body can change. Identity should persist.**

---

## 4. The Companion Model

At the highest level, the project can be summarized as:

                 Companion
                     │
        ┌────────────┼────────────┐
        │            │            │
       Mind         Self       Presence
        │            │            │
        └────────────┼────────────┘
                     │
                Embodiment
                     │
                     ▼
             Personal Companion

The project is therefore not only about making an LLM more capable.
It is about investigating what would be required to transform general-purpose artificial intelligence into a persistent personal companion.

## 5. Core Research Questions

Project Companion will maintain a growing list of long-term research questions.

Initial questions include:

RQ-001 — Identity
Where should an AI's identity live?
Weights, context, memory, training history, or another architecture?

RQ-002 — Personality
Can personality become a stable learned behavioral pattern rather than a system prompt?

RQ-003 — Identity Continuity
What makes a Companion remain the "same" Companion after model upgrades, fine-tuning, memory changes, or hardware migration?

RQ-004 — Autobiographical Memory
How should an AI form, retrieve, summarize, consolidate, and reinterpret memories of its own history?

RQ-005 — Individuality
Can two Companions beginning from the same base model develop meaningfully different identities through different experiences?

RQ-006 — Continual Learning
How can a Companion learn from long-term interaction without catastrophic forgetting, uncontrolled model drift, or degradation?

RQ-007 — Presence
How can an AI maintain useful awareness of a person's environment without becoming intrusive, distracting, or dependent on constant explicit prompting?

RQ-008 — Embodiment
Can a Companion move between different virtual and physical bodies while preserving a continuous identity?
These questions are not assumed to have easy answers.
Some may remain open for years.
Their purpose is to guide experiments, not to predetermine conclusions.

## 6. Learning Philosophy

The traditional learning path would be:

Mathematics
    ↓
Machine Learning
    ↓
Deep Learning
    ↓
PyTorch
    ↓
Transformer
    ↓
LLM
    ↓
Finally build something

Project Companion will take a different approach:

**Project-first + Research-first + Just-in-time Learning**

The working ratio is approximately:

70% Build
20% Just-in-time Learning
10% Systematic Foundation

Instead of waiting until every prerequisite has been mastered, the project begins with real systems and real experiments.

When Attention becomes necessary, study Attention.

When matrix multiplication becomes a barrier, study the required linear algebra.

When loss fails to decrease, study gradients, cross entropy, optimization, and learning rates.

When GPU memory becomes a bottleneck, study precision, batching, memory usage, and training efficiency.

When the Companion begins forgetting, study catastrophic forgetting and continual learning.

The rule is:

Problems determine what we learn next. The curriculum does not determine when we are allowed to encounter the problem.

Or, more personally:

我们一起养出一只 AI；为了养它，被迫把 LLM、AI systems 和 computing 一层一层学明白。

## 7. Companion Evolution

The Companion will evolve through multiple generations.

Companion-0 — Birth

Train a small language model from random weights.

The objective is not intelligence.

The objective is understanding the complete birth process of a language model

Dataset
  ↓
Tokenizer
  ↓
Transformer
  ↓
Random Initialization
  ↓
Pretraining
  ↓
Evaluation
  ↓
Checkpoint
  ↓
Inference
  ↓
First Generated Text

**Companion-1 — Intelligence**

Move from the educational small model toward capable open foundation models and develop a personal training pipeline.

Study and apply:
- SFT
- LoRA
- Preference learning
- DPO
- Evaluation
- Model adaptation

**Companion-2 — Individuality**

Begin systematically developing:

- Identity
- Personality
- Values
- Behavioral patterns
- Personal preferences

**Companion-3 — Memory**

Develop persistent memory systems:
- Semantic memory
- Episodic memory
- Autobiographical memory
- Retrieval
- Memory consolidation

**Companion-4 — Growth**

Explore whether the Companion can change through experience.
Study:
- Continual learning
- Experience replay
- Model editing
- Reflection
- Catastrophic forgetting
- Model drift

**Companion-5 — Presence**

Give the Companion perception and persistent interaction:
- Voice
- Hearing
- Vision
- Environmental context
- Multimodal understanding

**Companion-6 — Agency**

Allow the Companion to interact with systems and tools:
- Tool use
- Planning
- Computer interaction
- Agents
- Permissions
- Controlled autonomy

**Companion-7 — Embodiment**

Explore external forms:
- 2D / 3D avatars
- Animation
- Spatial computing
- AR / VR
- Physical devices
- Robotics

**Companion-8 — Companion**

Integrate the previous systems into a persistent personal AI companion.

This roadmap is expected to change.

Changing the roadmap is not failure.

Discovering that an assumption was wrong is part of the research.

## 8. Experiment Philosophy

Project Companion is intended to be an experimental research project, not merely a collection of tutorials.

Important experiments will receive permanent identifiers:

C0-EXP001
C0-EXP002
C0-EXP003
...

Each major experiment should record:

Question
Hypothesis
Configuration
Procedure
Result
What Failed
What Worked
What I Learned
Next Experiment

Failed experiments will not be deleted simply because they failed.

A failed experiment that changes our understanding is useful data.

The history of mistakes, revisions, abandoned ideas, and unexpected results is part of the project.

## 9. Project Documentation System

Different types of work will use different identifiers.

L      Learning Unit
EXP    Experiment
M      Milestone
RQ     Research Question
DOC    Project Document
TOOL   Project Tool / Infrastructure

Examples:

C0-L001       Language Modeling
C0-EXP001     First Training Corpus
C0-M01        First Successful Tokenization
RQ-001        Where Should Identity Live?
DOC-001       Project Genesis
TOOL-GIT-001  GitHub Repository Setup

The purpose of this system is to make a multi-year project navigable.

Every meaningful piece of work should have a place in the project's history.

## 10. Open Research and Privacy

Project Companion is intended to document as much of its technical development as reasonably possible.

Public material may include:

- Source code
- Architecture
- Research notes
- Experiment designs
- Failed experiments
- Training methodology
- Public datasets
- Evaluation results
- Technical lessons
- Model development history
- 
However, a personal AI inevitably contains deeply personal information.

The following should remain private:

- Personal conversations
- Private autobiographical memories
- Sensitive personal information
- Private training data
- Credentials
- API keys
- Authentication tokens
- Private interaction history
- Any data that should not become public

The principle is:

**Open methodology. Private life.**

The goal is to make the engineering and research reproducible without turning a person's private life into public training data.

## 11. Ownership

A central goal of Project Companion is personal ownership.

A Companion should ideally be:

- exportable,
- transferable,
- backupable,
- inspectable,
- modifiable,
- locally runnable where practical,
- and not permanently dependent on a single commercial AI provider.

Cloud services may be useful.

Commercial foundation models may be useful.

APIs may be useful.

But the long-term identity and history of the Companion should not disappear simply because a company changes a product, pricing model, API, or service.

The Companion should belong to the individual.

## 12. Current Status

Project started: September 2026

Current generation: Companion-0

Current objective:

Train the first Companion language model from random weights and observe it produce language for the first time.

The first major experiment will begin with:

C0-EXP001 — First Training Corpus

The first question is simple:

What should Companion-0 eat first, and why?

## 13. Long-Term Goal

The goal is not to predict exactly what artificial intelligence will look like decades from now.

The goal is to build, experiment, measure, learn, and continuously revise our assumptions.

Today, Project Companion begins with a tiny language model.

Over time, it may acquire:

language,
knowledge,
memory,
personality,
experience,
vision,
voice,
tools,
agency,

and eventually a body.

The technology may change.

The architecture may change.

The models may change.

Many early assumptions will probably turn out to be wrong.

But the central question remains:

Can an AI become a persistent individual that learns, remembers, grows, and shares a life history with one person?

Project Companion is an attempt to find out.


# 中文版

## 1. 起源 —— 为什么会有这个项目

这个项目的起点，其实远早于我知道“大语言模型”是什么的时候。
从小，我就非常喜欢 《宝可梦（Pokémon）》、《数码宝贝（Digimon）》，以及以智慧宠物、御兽和伙伴生物为核心的小说与幻想作品。
真正吸引我的，并不只是幻想世界、战斗或者那些神奇的能力。
而是一个更简单的想法：

如果我也能够拥有一只真正属于自己的智慧伙伴，会怎么样？
它能够和我交流。
它能够理解我。
它拥有自己的性格。
它能够记住我们共同经历过的事情。
当我在人生中遇到困难的时候，它能够帮助我分析和解决问题。
更重要的是，它并不是一个随时可以被替换掉的工具。
它会和我一起经历时间，并在这个过程中不断成长。
在过去的大部分时间里，这样的伙伴只能存在于幻想作品之中。
现代人工智能，尤其是大语言模型的出现，让这件事情第一次发生了变化。
今天的 AI 距离我小时候想象中的那种智慧伙伴依然非常遥远。
一个套着 system prompt 的 chatbot 并不是一个真正持续存在的个体。
一个连接商业 API 的聊天界面，也不是一个真正意义上的数字生命伙伴。
但是第一次，我们似乎已经能够看到通往那个目标的一些技术路径。

Foundation Model 可以提供基础智能。
Post-training 可以塑造行为。
Memory System 可以保存经历。
Multimodal Model 可以提供视觉和听觉。
Agent 可以使用工具并与计算机交互。
Continual Learning 也许最终能够让 AI 因为经历而真正发生改变。
Virtual Avatar、Spatial Computing、AR 以及 Robotics，则可能让它获得不同形式的身体。

因此，这个项目从一个非常简单的问题开始：

小时候那个完全属于幻想的想法，今天究竟有多少能够真正被我们造出来？

我不知道答案。

Project Companion 的目的，就是亲手去寻找这个答案。

## 2. 项目使命

创造一个能够被个人拥有、理解、塑造，并长期培养成长的 AI。

我们的目标并不是再制造一个 chatbot。

也不是给现有模型写一句 system prompt，然后把它称为“人格”。

更不是给商业 AI API 套一个漂亮的界面。

长期目标，是理解并实验创造 Personal AI Companion 所需要的一整套技术，使它逐渐拥有：

- 持续存在的 Identity
- 稳定的 Personality
- Long-term Memory
- Autobiographical Experience
- Personal Knowledge
- Skills
- Perception
- Agency
- 以及最终通过长期经历不断学习和成长的能力
- 
Foundation Model 可以提供通用智能。
但通用智能本身并不能定义一个“个体”。
这个项目最核心的假设之一是：

智能可以来自共同的基础，但 Identity 应该从不同的经历中逐渐产生。

两只 Companion 完全可以从同一个 Base Model 开始。
但是如果它们陪伴的是不同的人，拥有不同的记忆，形成不同的偏好，学习不同的技能，经历不同的历史，那么随着时间推移，它们应该逐渐成为两个真正不同的 Companion。
这种差异究竟能否产生，以及应该如何产生，是 Project Companion 最核心的长期研究问题之一。

## 3. 什么是 Companion？
整个项目围绕四个主要维度展开。

**Track A — Mind / 大脑**

Companion 如何思考和学习？

这一方向研究语言模型智能的基础：
- Data
- Tokenization
- Embedding
- Transformer
- Attention
- Pretraining
- Optimization
- Evaluation
- Inference
- Open Foundation Model
- Fine-tuning
- SFT
- LoRA
- Preference Learning
- DPO
- Reasoning 与能力发展

我们的第一个目标不是下载一个现成模型。

而是从随机参数开始，亲手训练一个小型语言模型，完整经历：

Data → Tokenizer → Transformer → Pretraining → Checkpoint → Inference

它将成为：

Companion-0

**Track B — Self / 自我**

为什么“它是它”？

这是整个项目最重要的长期研究方向之一。

研究内容包括：
- Identity
- Personality
- Values
- Preferences
- Behavioral Consistency
- Episodic Memory
- Semantic Memory
- Autobiographical Memory
- Experience
- Reflection
- Memory Consolidation
- Continual Learning
- Individuality
- Identity Continuity

未来的 Companion 不应该只是“知道一些关于主人的信息”。
它应该拥有自己的历史。
它应该能够记住双方共同经历的重要事情，并让过去的经历真正影响未来的行为。

这会产生一个更深的问题：

AI 的 Identity 究竟存在于哪里？

存在于 weights？
Memory？
Context？
Training history？
Interaction history？
还是这些东西共同形成的某种结构？

Project Companion 不假设这个问题已经存在标准答案。

我们希望通过长期实验逐渐寻找答案。

**Track C — Presence / 存在**

怎样让 Companion 从聊天框里走出来，真正进入日常生活？

一个真正长期存在的伙伴，不应该要求主人每次：
打开应用程序 → 从头解释情况 → 提问 → 得到答案 → 关闭应用程序。

未来 Companion 应该逐渐拥有：

- Voice Interaction
- Hearing
- Vision
- Multimodal Perception
- Environmental Awareness
- Context Awareness
- Persistent Presence
- Tool Use
- Computer Interaction
- Planning
- Agency

人与 AI 的交互方式应该逐渐从：
Human → Question → AI → Answer

发展成：
Human ↔ Companion ↔ World

同时，真正优秀的 Companion 还必须学会：

什么时候不应该行动。
Persistent Presence 不应该意味着不断打扰。
它最终应该理解什么时候应该说话，什么时候应该帮助，什么时候只需要观察，以及什么时候应该保持沉默。

**Track D — Embodiment / 身体**

Companion 应该长什么样？

它应该以什么方式存在于虚拟世界或者现实世界？

Companion 的身体不应该定义它的 Identity。

随着技术发展，它可能经历：

2D Avatar → 3D Character → AR/VR Presence → Spatial Computing → Physical Device → Robot

今天，它可能只存在于电脑屏幕中。
以后，它可能通过 AR 以一个空间角色的形式出现在身边。
更远的未来，它也可能通过机器人身体与现实世界互动。

Interface 可以改变。
身体可以改变。
但 Companion 应该仍然是原来的那个 Companion。

因此产生一个长期原则：
身体可以改变，但 Identity 应该延续。

4. Companion 的整体结构
从最高层来看：
                 Companion
                     │
        ┌────────────┼────────────┐
        │            │            │
       Mind         Self       Presence
        │            │            │
        └────────────┼────────────┘
                     │
                Embodiment
                     │
                     ▼
             Personal Companion

或者：

Intelligence
    +
Identity
    +
Personality
    +
Memory
    +
Experience
    +
Growth
    +
Perception
    +
Agency
    +
Embodiment
    ↓
Companion

因此，这个项目研究的并不只是如何让 LLM 变得更强。

我们真正研究的是：

怎样让通用人工智能逐渐成为一个长期存在的个人智能伙伴。

## 5. 核心研究问题

Project Companion 将长期维护一组 Research Questions。

第一批问题包括：

RQ-001 — Identity
AI 的 Identity 应该存在在哪里？
Weights、Context、Memory、Training History，还是另一种尚未建立的结构？

RQ-002 — Personality
Personality 能否成为通过经历逐渐学习形成的稳定行为模式，而不仅仅是一句 system prompt？

RQ-003 — Identity Continuity
模型升级、Fine-tuning、Memory 改变或者迁移硬件以后，究竟什么保证它仍然是“原来的它”？

RQ-004 — Autobiographical Memory
AI 应该如何形成、检索、总结、整合，并重新理解属于自己的历史记忆？

RQ-005 — Individuality
两个从完全相同 Base Model 开始的 Companion，能否因为不同经历逐渐形成真正有意义的个体差异？

RQ-006 — Continual Learning
Companion 怎样通过长期互动持续学习，同时避免 catastrophic forgetting、不可控的 model drift 或能力退化？

RQ-007 — Presence
AI 怎样持续理解一个人的环境，同时又不会变得侵入、打扰或者要求主人不断主动输入？

RQ-008 — Embodiment
Companion 能否在不同虚拟身体和物理身体之间迁移，同时保持连续的 Identity？

这些问题并不假设存在简单答案。

其中一些问题可能很多年以后依然没有完全解决。

它们存在的目的，是指导实验，而不是提前规定答案。

## 6. 学习哲学

传统路线通常是：

数学
 ↓
Machine Learning
 ↓
Deep Learning
 ↓
PyTorch
 ↓
Transformer
 ↓
LLM
 ↓
终于开始做项目

Project Companion 不采用这种方式。

我们采用：
Project-first + Research-first + Just-in-time Learning

暂定比例：
70% Build
20% Just-in-time Learning
10% Systematic Foundation

不等待所有先修知识全部学完才允许进入真实问题。
遇到 Attention，就学习 Attention。
矩阵运算成为障碍，再补当前真正需要的 Linear Algebra。
Loss 不下降，就研究 Gradient、Cross Entropy、Optimizer 和 Learning Rate。
GPU Memory 成为瓶颈，再研究 Precision、Batch、Memory Usage 和 Training Efficiency。
Companion 开始遗忘，再研究 Catastrophic Forgetting 和 Continual Learning。

我们的原则是：
问题决定下一步学习什么，而不是课程表决定什么时候才允许碰到问题。

用一句更属于这个项目的话来说：
我们一起养出一只 AI；为了养它，被迫把 LLM、AI systems 和 computing 一层一层学明白。

## 7. Companion 的成长路线

Companion-0 — Birth / 出生
从 Random Weights 开始训练第一只小型语言模型。

目标不是强大。
目标是亲手理解一个语言模型完整的出生过程。

Dataset
 ↓
Tokenizer
 ↓
Transformer
 ↓
Random Initialization
 ↓
Pretraining
 ↓
Evaluation
 ↓
Checkpoint
 ↓
Inference
 ↓
第一次生成文字

Companion-1 — Intelligence / 智能

从教学性质的小模型逐渐转向真正有能力的 Open Foundation Model，并建立自己的训练体系。

研究：
- SFT
- LoRA
- Preference Learning
- DPO
- Evaluation
- Model Adaptation

Companion-2 — Individuality / 个体

开始系统建立：
- Identity
- Personality
- Values
- Behavioral Patterns
- Personal Preferences

Companion-3 — Memory / 记忆

建立：
- Semantic Memory
- Episodic Memory
- Autobiographical Memory
- Retrieval
- Memory Consolidation

Companion-4 — Growth / 成长

探索 Companion 能否真正因为经历而改变。

研究：
- Continual Learning
- Experience Replay
- Model Editing
- Reflection
- Catastrophic Forgetting
- Model Drift

Companion-5 — Presence / 存在

让 Companion 获得感知能力：
- Voice
- Hearing
- Vision
- Environmental Context
- Multimodal Understanding

Companion-6 — Agency / 行动

让 Companion 开始与系统和工具交互：
- Tool Use
- Planning
- Computer Interaction
- Agent
- Permissions
- Controlled Autonomy

Companion-7 — Embodiment / 身体

探索 Companion 的外在形式：
- 2D / 3D Avatar
- Animation
- Spatial Computing
- AR / VR
- Physical Devices
- Robotics

Companion-8 — Companion

尝试将此前所有系统整合成一个真正长期存在的 Personal AI Companion。
这份 Roadmap 一定会改变。
改变路线并不意味着失败。
发现过去的假设是错误的，本身就是研究成果。

## 8. 实验原则

Project Companion 是一个长期实验研究项目，而不是 Tutorial Collection。
重要实验将拥有永久编号：

C0-EXP001
C0-EXP002
C0-EXP003
...

每个重要实验尽量记录：

Question
Hypothesis
Configuration
Procedure
Result
What Failed
What Worked
What I Learned
Next Experiment

失败实验不会因为失败而被删除。
如果一次失败改变了我们的理解，它就是有价值的数据。
错误、修改、被放弃的路线以及意外结果，全部属于 Companion 的成长历史。

## 9. 项目编号体系

不同工作使用不同编号：

L      Learning Unit / 学习单元
EXP    Experiment / 实验
M      Milestone / 里程碑
RQ     Research Question / 研究问题
DOC    Project Document / 项目文档
TOOL   Project Tool / 项目工具

例如：

C0-L001       Language Modeling
C0-EXP001     First Training Corpus
C0-M01        First Successful Tokenization
RQ-001        Where Should Identity Live?
DOC-001       Project Genesis
TOOL-GIT-001  GitHub Repository Setup

目的很简单：

让一个可能持续很多年的项目始终可以被定位、查询和回顾。

## 10. Open Research 与隐私

Project Companion 会尽可能记录和公开技术研究过程。

可以公开：
- Source Code
- Architecture
- Research Notes
- Experiment Design
- Failed Experiments
- Training Methodology
- Public Dataset
- Evaluation Results
- Technical Lessons
- Model Development History

但 Personal AI 最终一定会涉及高度私人化的信息。

以下内容原则上保持 Private：
- 私人对话
- 私人 Autobiographical Memory
- 敏感个人信息
- Private Training Data
- Credentials
- API Keys
- Authentication Tokens
- Private Interaction History
- 任何不应该成为公共数据的信息

因此遵循：
Open methodology. Private life.

公开方法。
保护生活。

## 11. Ownership / 所有权

Project Companion 的核心目标之一是：
个人真正拥有自己的 Companion。

理想情况下，它应该能够：

- Export
- Transfer
- Backup
- Inspect
- Modify
- 在现实可行的情况下 Local Run
- 不永久依赖任何单一商业 AI Provider

Cloud Service 可以使用。
Commercial Foundation Model 可以使用。
API 可以使用。

但 Companion 长期积累的 Identity 和 History，不应该因为某家公司修改产品、价格、API 或停止服务而消失。
Companion 应该属于个人。

## 12. 当前状态

Project Started：September 2026
Current Generation：Companion-0

当前目标：
从 Random Weights 开始训练第一只 Companion Language Model，并亲眼看到它第一次生成语言。

第一个正式实验：
C0-EXP001 — First Training Corpus
我们的第一个问题：
Companion-0 的第一口应该吃什么？为什么？

## 13. 长期目标

我们并不试图预测几十年后的 AI 一定会是什么样子。

我们要做的是：
Build → Experiment → Measure → Learn → Revise

今天，Project Companion 从一个很小的语言模型开始。

未来，它也许会逐渐获得：
语言，
知识，
记忆，
人格，
经历，
视觉，
声音，
工具，
行动能力，
最后甚至获得身体。

技术会改变。
Architecture 会改变。
Model 会改变。
今天的很多假设未来很可能会被证明是错误的。

但是有一个问题会始终保留下来：
AI 能否最终成为一个持续存在的个体——能够学习、记忆、成长，并与一个人共同拥有属于彼此的生命历史？

Project Companion，就是一次寻找这个答案的长期实验。
