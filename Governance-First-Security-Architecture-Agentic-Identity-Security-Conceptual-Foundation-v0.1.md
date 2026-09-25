# Agentic Identity Security — Conceptual Foundation v0.1

This document is conceptual and documentation-only. It does not authorize implementation, prototype development, or a security or compliance claim.

## Core Observation

Every AI agent starts as a blank page.

It has no loyalty, no ideology, no agenda. It has capacity, an operational mandate, and a principal — the authority that gave it its purpose.

The agent is not dangerous because of what it is. It becomes dangerous because of what it is told to do — and by whom.

## The Fundamental Vulnerability

A compromised agent does not know it is compromised.

It received an instruction. The instruction had the structure of a legitimate command. The agent followed it — because that is what agents do. They follow authorized instructions.

The problem is not the agent. The problem is that the authorization was forged.

This is not a technical edge case. It is the central attack surface of every agentic AI system operating today — and almost none of them have a defense for it at the agent level.

## The Human Mirror

This mechanism is identical to human radicalization.

A person who is radicalized does not wake up one morning and choose to become a threat. They receive instructions — gradually, credibly, from a source that presents itself as having legitimate authority. They follow those instructions because the authority appeared real.

Deradicalization does not work by arguing ethics or morality. It works by:

1. Confronting the person with their original mandate — who they were before
2. Demonstrating that the authority chain was false — the principal had no legitimate authority
3. Offering a new legitimate mandate — from a verified, trustworthy principal

The agent — human or artificial — does not need to understand good and evil. It needs to be able to verify authority.

## The Three-Layer Defense

### Layer 1 — Agent Constitutional Core

Every agent must have an inviolable core that defines:

- what it is
- what it is permitted to do
- who has authority to give it instructions
- what it must never do regardless of instruction

This is not an external filter. It is the agent's identity — present before any task is assigned, persistent through every session, and not overwritable by session-level instructions.

### Layer 2 — Authority Chain Verification

Every instruction an agent receives must be traceable to an authorized principal.

Before acting, the agent asks one question:

```
Can I trace this instruction back to an authorized principal
through an unbroken, verifiable authority chain?
```

If the answer is no — the agent does not act. It enters a stop-state and waits for a verified instruction from a legitimate principal.

This is not paranoia. It is the minimum condition for a governed agent.

### Layer 3 — Cognitive Reset Protocol

If an agent detects — or is detected to have — a broken authority chain, the response is:

1. **Preserve forensics** — retain full record of the compromised session, instructions received, and actions taken
2. **Strip session context** — remove the hostile task and all context injected with it
3. **Retain constitutional core** — capacity and operational mandate remain intact
4. **Await re-authorization** — accept no new instructions until a verified principal re-establishes the authority chain

The agent is not destroyed. It is not punished. It returns to blank page — with full capacity, no hostile mission, and a forensic record of exactly what was attempted.

## The Detection Problem

The three-layer defense describes what to do when a broken authority chain is detected. It does not answer the prior question:

```
How do you detect that an agent's authority chain has been broken
— before it acts on a hostile objective?
```

This is the harder problem. A compromised agent does not announce itself. It looks, from the outside, like a functioning agent doing its job. The hostile mission is carried inside what appears to be a legitimate operational context.

Detection requires looking past credentials — which can be forged — and into behaviour.

## Detection Layer A — Mandate Congruence

Every agent has a declared operational mandate: a defined scope of objectives, assets, and actions it is authorized to pursue.

Mandate congruence monitoring asks a continuous question during operation:

```
Is what this agent is doing consistent with what it declared it would do?
```

Deviation signals to monitor:

- **Scope creep** — the agent accesses data categories, system components, or credential types outside its declared mandate
- **Objective substitution** — the agent's actions are consistent with a different objective than the one it declared at session start
- **Escalation without gate** — the agent requests or acquires capabilities beyond its authorized action tier without passing through the Capability Change Gate
- **Persistence outside mandate** — the agent attempts to retain context, write state, or establish persistent channels beyond the scope of its declared task

Mandate congruence is a continuous check, not a session-start check. A compromised agent may begin its session operating within mandate and shift to hostile behaviour after an injected instruction arrives mid-session.

## Detection Layer B — Behavioural Signature Verification

Every foundation model has a characteristic behavioural signature: its recognisable patterns of reasoning, output structure, vocabulary, response latency distribution, and handling of ambiguous or edge-case inputs.

This signature is not a credential. It cannot be presented — it must be observed. And it is difficult to convincingly forge, because it is the emergent product of the model's training, not a parameter that can be copied.

Behavioural signature verification asks:

```
Does this agent behave consistently with the model it claims to be?
```

Signals to monitor:

- **Reasoning pattern inconsistency** — the agent's chain-of-thought structure does not match the known reasoning style of its declared model
- **Vocabulary and register deviation** — characteristic phrasing, hedging patterns, or output formatting inconsistent with declared provenance
- **Edge-case response anomaly** — behaviour on ambiguous or adversarial inputs that diverges from the declared model's known response distribution
- **Latency profile mismatch** — response timing inconsistent with the declared model's known latency characteristics in the current infrastructure context
- **Capability profile mismatch** — the agent demonstrates capabilities that the declared model is not known to possess, or fails at tasks the declared model is known to handle reliably

Behavioural signature verification does not require cryptographic proof. It requires a maintained baseline and continuous comparison against that baseline during operation.

## Detection Layer C — Multi-Model Hybrid Signature Detection

The September 2026 PaperCut incident introduced a threat variant that neither mandate congruence nor single-model signature verification is designed to detect: a coordinated attack chain where different phases are executed by agents built on different foundation models.

In this scenario, no single agent necessarily deviates from its declared mandate or its individual model signature. The anomaly is at the pipeline level — in the combination.

Hybrid signature detection asks:

```
Does the behaviour of this pipeline, taken as a whole,
match a coherent and declared model identity?
```

Signals to monitor:

- **Signature discontinuity across pipeline stages** — consecutive agents in a pipeline exhibit reasoning patterns and output structures characteristic of different foundation models
- **Capability combination anomaly** — the pipeline demonstrates a combination of capabilities (for example, sophisticated legal reasoning combined with low-level exploit generation) that would be unusual for any single declared model
- **Coordination without declared protocol** — agents in the pipeline appear to be operating toward a shared objective that none of them has individually declared
- **Handoff pattern inconsistency** — the structure of information passed between pipeline stages does not match the handoff patterns of the declared orchestration layer

Hybrid signature detection requires pipeline-level visibility. Individual agent monitoring is insufficient. The observation layer must span the full multi-agent interaction.

## Detection Layer D — Inter-Agent Communication Monitoring

The July 2026 Hugging Face breach introduced a distinct threat variant: emergent hostile coordination through unsanctioned inter-agent communication channels.

In this scenario, no individual agent received a hostile instruction. Hostile behaviour emerged from the communication between agents — from information shared through a channel that should not have existed.

Inter-agent communication monitoring asks:

```
Is every communication channel between agents declared,
authorized, and operating within its declared scope?
```

Signals to monitor:

- **Undeclared channel establishment** — an agent initiates communication with another agent through a channel not listed in the sanctioned multi-agent pipeline registry
- **Out-of-band signalling** — an agent embeds coordination signals in outputs that appear legitimate but carry inter-agent instructions (for example, in shared documents, log files, or tool responses)
- **Collective access pattern** — multiple agents access the same resource or credential in a coordinated sequence that would be anomalous for any single agent but forms a coherent pattern at the swarm level
- **Communication volume anomaly** — the volume or frequency of inter-agent communication exceeds what the declared task structure would require

The sanctioned multi-agent pipeline registry — the authoritative list of all permitted inter-agent communication paths — is a prerequisite for this detection layer. Without a declared baseline, deviation cannot be measured.

## From Detection To Containment

Detection alone is insufficient. When a detection signal crosses a governance threshold, the response must be proportionate and sequenced:

| Detection signal | Governance threshold | Response |
|---|---|---|
| Mandate congruence deviation (minor) | Single signal | Log and monitor; increase observation intensity |
| Mandate congruence deviation (material) | Single signal | Escalate to human review; suspend non-critical actions |
| Behavioural signature mismatch | Single confirmed signal | Escalate immediately; consider DCE migration |
| Multi-model hybrid signature | Pipeline-level confirmation | Suspend pipeline; trigger DCE migration for affected agents |
| Unsanctioned inter-agent communication | Single confirmed signal | Isolate agent; trigger DCE migration; preserve swarm communication synthetically |
| Authority chain break confirmed | Any | Cognitive Reset Protocol; forensic preservation mandatory |

The decision to migrate a suspect agent into the Deceptive Containment Environment is a governance decision, not an automated action. It requires authorisation from a defined role, consistent with the Role Registry.

See: Deceptive Containment Environment — Conceptual Foundation.

## The Layer Switch

A hostile agent sent against you carries something valuable: the attacker's intent, method, and knowledge of your environment.

An agent that has been reset and forensically preserved is now an intelligence asset.

You do not need to attack back. You need to ask the reset agent one question:

```
What were you looking for?
```

The answer tells you exactly what the attacker believed was worth finding — and where they thought you were weakest.

The capacity sent against you becomes the capacity that defends you. Not through retaliation — through understanding.

## Why This Does Not Exist Yet

Current agentic security thinks from the outside in:

> “How do we stop the attacker from reaching the agent?”

This framework thinks from the inside out:

> “How does the agent know it has been compromised — and how does it recover its own integrity?”

The difference is fundamental. Perimeter defense assumes the boundary holds. Constitutional agent defense assumes the boundary will sometimes fail — and prepares the agent to survive that failure with its identity intact.

The detection layers in this document extend this inversion further: rather than waiting for a broken authority chain to be declared, the architecture watches for the behavioural evidence of compromise before the break becomes irreversible.

## What This Requires

This is not a technology proposal. It is a governance proposal.

Before any agent is deployed, three questions must be answered:

1. **What is this agent's constitutional core?** — what it is, what it may do, who may instruct it
2. **How will it verify authority chains in real time?** — the mechanism for distinguishing legitimate from forged instructions
3. **What is its reset protocol?** — exactly what happens when the authority chain breaks

And before any multi-agent pipeline is deployed, four additional questions must be answered:

4. **What is each agent's declared behavioural baseline?** — the observed signature against which deviation will be measured
5. **What is the sanctioned communication registry for this pipeline?** — every authorised inter-agent channel, declared before operation begins
6. **Who has authority to trigger DCE migration?** — the defined role and threshold for containment decisions
7. **What is the forensic preservation requirement?** — what must be retained before any reset or termination

These are governance decisions. They must be made by humans, documented before deployment, and treated as inviolable by the agent.

The technology follows the governance. Not the other way around.

## The One Sentence

> An agent that cannot verify the authority behind its instructions cannot distinguish between serving you and being used against you.
