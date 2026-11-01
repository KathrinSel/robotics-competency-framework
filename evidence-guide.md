# Evidence Guide — How to Score Each Level

This guide answers a practical question: **how do you tell a level 1 from a level 2 at CV screening stage, and what does each level sound like in an interview?**

Compiled in response to [Issue #1](https://github.com/KathrinSel/robotics-competency-framework/issues/1). Based on real interview feedback across 9 role types.

---

## Scoring levels — operational definitions

| Score | Level | CV evidence | Interview signal |
|-------|-------|-------------|-----------------|
| 0–2 | Not present / Aware | Concept mentioned in education or course context only | Can define the term; no personal example |
| 3–4 | Aware+ | Listed as a skill with no described project | Describes what it is but not what went wrong or why choices were made |
| 5–6 | Practitioner | Named in a project with described outcomes and context | Has a concrete story; can explain tradeoffs; acknowledges failure modes |
| 7–8 | Advanced | Multiple projects; measurable results; system-level ownership | Reasons from first principles; explains what breaks and why; made design decisions |
| 9–10 | Expert | Paper, open-source contribution, or widely recognised system | Defines the problem space; knows where the field is wrong; has strong opinions backed by evidence |

**Key insight from interviews:** the gap between level 2 and level 3 is almost never about vocabulary. Candidates who failed interviews often knew all the right terms. The filter is whether they can explain *what goes wrong* and *why* — not just *what it is*.

---

## Top competencies — screening and interview guide

### Real Hardware Deployment (legged/dynamic systems)
*Primary filter for RL Locomanipulation role*

**CV — level 2 signals:**
- "Deployed trained policy on Unitree B2 / Spot / ANYmal"
- "Real-robot experiments" with described outcomes (not just "simulation experiments")
- Internship or role at a company with physical robots

**CV — level 3 signals:**
- Described the full bring-up cycle: sim training → hardware validation → iteration
- Mentions actuator characterisation, latency measurement, or mass correction
- Failure analysis documented (paper, blog post, or project description)

**Interview — level 2 answer:**
> "We trained in Isaac Lab and deployed on Spot. The policy worked but was jerky — we had to tune the PD gains and add a low-pass filter."

**Interview — level 3 answer:**
> "We measured 120ms latency from policy output to actuator response — about 2–3 policy steps. We trained on the latency distribution in sim rather than assuming zero delay. We also weighed the robot and retrained with corrected mass after the policy kept falling on one side."

**Red flag:** "We ran hardware experiments" with no description of what failed or what was changed.

---

### Action Chunking & Async Inference
*Primary filter for Manipulation Capability Engineer*

**CV — level 2 signals:**
- "Deployed ACT / Diffusion Policy with action chunking"
- Work on real manipulation systems with inference latency constraints

**CV — level 3 signals:**
- Described handling async execution explicitly
- Work on systems with variable inference time or multi-rate observation

**Interview — level 2 answer:**
> "Action chunking means the model predicts multiple future actions at once instead of one at a time. It helps because the model runs slower than the control loop."

**Interview — level 3 answer:**
> "The problem with async chunking is that by the time you execute action step 4, your observation was captured at step 1. If the scene changed — object moved, someone intervened — you're executing stale actions. Under distribution shift this compounds quickly. We handled it by detecting OOD states via uncertainty estimation and falling back to a reactive policy when confidence dropped below threshold. We also used a rolling window rather than fixed chunks to reduce the staleness gap."

**Red flag:** Candidate explains what action chunking is but cannot describe a scenario where it fails.

---

### Sim-to-Real Transfer
*Must-have for RL Locomanipulation and Simulation Engineer roles*

**CV — level 2 signals:**
- "Sim-to-real transfer" mentioned with a described physical deployment
- Domain randomization used in a project with real-robot outcome

**CV — level 3 signals:**
- Describes specific sim-to-real gaps they diagnosed and fixed
- Adaptive or automated domain randomization
- Paper or technical post on sim-to-real methodology

**Interview — level 2 answer:**
> "We used domain randomization — randomised mass, friction, and motor gains. The policy transferred but needed some fine-tuning on the real robot."

**Interview — level 3 answer:**
> "The main gap was contact dynamics — specifically foot-ground interaction. Sim assumed perfect contact while the real floor had compliance. We added contact force randomisation and trained with a distribution of surface stiffness values. We also found that randomising motor delay was more important than randomising mass — the policy was much more sensitive to timing than to inertia."

**Red flag:** Domain randomization described only as "randomise parameters" with no understanding of which parameters matter and why.

---

### Transformer Implementation Depth
*Primary filter for VLA Pre-Training and Senior RL (VLA) roles*

**CV — level 2 signals:**
- PyTorch / JAX work on transformer-based models
- Research or industry role involving model training (not just fine-tuning via APIs)

**CV — level 3 signals:**
- Custom attention implementation or architecture modification
- Work on training stability, numerical issues, or distributed training at scale
- Open-source transformer code or paper contribution

**Interview — level 2 answer:**
> "Attention is softmax(QK^T / sqrt(d)) × V. The sqrt(d) prevents the dot products from getting too large and pushing softmax into the saturating region."

**Interview — level 3 answer:**
> "For numerically stable softmax you subtract the row maximum before exponentiation — that's the LSE trick. Without it you get overflow for large dot products, especially at low precision. In multi-head attention, Q and K must share the same last dimension for the dot product to be defined, but V can have a different dimension — you project it separately. For GQA you have fewer K/V heads than Q heads, which reduces the KV cache size at inference while keeping most of the expressivity."

**Red flag:** Can recite the attention formula but cannot explain shapes, why the scaling factor works, or what goes wrong without numerical stabilisation.

---

### GPU Memory & Training Efficiency
*Second primary filter for VLA roles*

**CV — level 2 signals:**
- Multi-GPU training experience described
- Work involving large model training (1B+ parameters)

**CV — level 3 signals:**
- Described memory optimisation techniques applied (activation checkpointing, quantisation, FSDP)
- Profiling or benchmarking of training throughput
- Resolved OOM errors through architectural or infrastructure changes

**Interview — level 2 answer:**
> "GPU memory holds the model weights, the activations from the forward pass, and the gradients. Optimizer states like Adam's first and second moments take another 2× the weight memory."

**Interview — level 3 answer:**
> "For a model that doesn't fit on one GPU: FSDP shards weights, gradients, and optimizer states across devices — you only hold your shard locally and all-gather when needed. Activation checkpointing trades compute for memory by recomputing activations during backward instead of storing them. For inference on the robot, we quantised to fp8 which halved memory and improved throughput — the tricky part was maintaining numerical stability in the attention layers which are sensitive to low precision."

**Red flag:** Describes distributed training at a conceptual level but cannot explain what is stored in GPU memory during a forward pass.

---

### Retargeting Strategies
*Hidden filter for Teleoperation roles — most common failure point*

**CV — level 2 signals:**
- Teleoperation system development with motion capture input
- Work on human-to-robot motion mapping

**CV — level 3 signals:**
- Multiple retargeting strategies implemented and compared
- User calibration or workspace scaling described
- Finger / hand retargeting beyond simple open/close

**Interview — level 2 answer:**
> "Retargeting maps the human operator's tracked pose to robot joint commands. We used an absolute approach — the robot's end-effector mirrors the operator's hand position in Cartesian space."

**Interview — level 3 answer:**
> "Absolute retargeting is intuitive but breaks when the operator's workspace doesn't match the robot's — a tall operator and a short one reach the same shelf differently. Relative retargeting tracks deltas from a calibration pose, which scales better across users and robot morphologies. The tradeoff is that operators lose the intuitive 'what you see is where the robot goes' mapping, so you need better feedback. We added a ghost hand visualisation in VR so operators could see their intended target before committing."

**Red flag:** Only aware of absolute retargeting; cannot describe user calibration or the tradeoffs between mapping strategies.

---

### Production Systems Mindset
*Primary differentiator for Staff Control SW Engineer*

**CV — level 2 signals:**
- "Production deployment" mentioned with scale described (number of units, duration)
- CI/CD, testing frameworks, or reliability engineering in job description

**CV — level 3 signals:**
- Fleet-scale deployment with described reliability or latency metrics
- Ownership of release process or safety validation pipeline
- Incident response or post-mortem experience described

**Interview — level 2 answer:**
> "We had CI/CD set up with automated tests. Before releasing a new controller version we ran regression tests in simulation and then validated on hardware."

**Interview — level 3 answer:**
> "We ran interleaved A/B tests on the road — half the fleet on the current controller, half on the candidate — with a statistical stopping rule so we didn't need to wait for a fixed sample size. We also had requirements traceability from the control spec down to test cases, which was essential when we needed to justify a safety argument. The hardest part was maintaining determinism — we fixed memory allocation in the hot path and added warm-up periods so the first control cycle wasn't slower than the rest."

**Red flag:** Production experience described only in terms of "it worked in deployment" with no mention of testing methodology, reliability metrics, or what happened when things went wrong.

---

## Using this guide

**At CV screening:** look for the level 2 signals in the project descriptions — not just skill lists. A candidate who lists "sim-to-real" as a skill but describes only simulation experiments in their projects is likely a level 1.

**At interview:** use the level 3 answer as your calibration target. You do not need to evaluate the technical content yourself — listen for whether the candidate volunteers failure modes, tradeoffs, and design decisions without being prompted. That pattern is a stronger signal than any specific fact.

**Calibration note:** for roles where both a 3/4 and a 2/4 interviewer scored the same candidate (which happened for several roles in our data), the disagreement was almost always about whether production experience or theory depth was the primary filter. Align your panel on this before starting the process.

---

*Part of the [Robotics Competency Framework](https://github.com/KathrinSel/robotics-competency-framework)*  
*Contributions and corrections welcome — open an issue or PR.*
