# Robotics Competency Framework

**An open competency standard for hiring engineers in humanoid and mobile robotics.**

Built by a talent practitioner who conducted 200+ technical interviews across UK, US, and Canada — because no existing HR tool, ATS, or skills taxonomy was designed for this domain.

---

## Why this exists

Robotics sits at the intersection of mechanical engineering, embedded software, AI, and safety-critical systems. A qualified robotics engineer is not a software engineer with a broader stack — they are a genuinely multidisciplinary profile that standard hiring tools cannot evaluate.

Existing HR infrastructure was built for two scenarios: high-volume hiring (retail, logistics) or generic software engineering. Robotics fits neither. The result: companies either hire the wrong people slowly, or fail to hire at all.

This framework was created to fill that gap — providing a shared language for evaluating robotics talent across specialisations, seniority levels, and geographies.

---

## What's inside

### 9 Role Profiles
Each with a dedicated competency map and must-have thresholds:

| Role | Focus |
|------|-------|
| RL Engineer — Locomanipulation | Learning-based policies for combined loco+manip |
| VLA Pre-Training Engineer | Foundation model pre-training for robotics |
| Senior RL Engineer (VLA) | RL + multimodal transformers + distributed training |
| Simulation Engineer — Manipulation | Physics simulation environments for dexterous tasks |
| Simulation & Control Engineer | Sim-driven hardware design + RL + control theory |
| Staff Control Software Engineer | Production-grade real-time control systems |
| Teleoperation SW Engineer (VR) | Low-latency VR teleoperation systems |
| Teleoperation Engineer (UX/Mappings) | Operator experience, control mappings, cognitive load |
| Manipulation Capability Engineer | Post-training and fine-tuning for end-user tasks |

### 10 Competency Domains · 48 Competencies

| Domain | Coverage |
|--------|----------|
| D1 · RL Core | Policy optimization, reward design, curriculum, imitation learning, distributed training |
| D2 · Simulation | Isaac Lab, MuJoCo, URDF, GPU-parallel sim, domain randomization, physics setup |
| D3 · Locomotion | Legged/humanoid robots, dynamic balance, kinematics & dynamics, whole-body control |
| D4 · Manipulation | Dexterous grasping, in-hand manipulation, deformable objects |
| D5 · Locomanipulation | Combined loco+manip policies, multi-behavior learning |
| D6 · Perception & VLA | VLA models, multimodal transformers, LLM/VLM pre-training, eval design |
| D7 · Control Systems | MPC, impedance/force control, real-time architecture, safety-critical systems |
| D8 · Software & HW | ROS2, C++, Python/PyTorch, real-time Linux, CI/CD |
| D9 · Teleoperation | VR development, low-latency streaming, operator UX, HCI, data pipelines |
| D10 · Research & Collab | Publications, experiment design, HW↔SW collaboration, technical leadership |

### Scoring System

Each competency is rated 0–3:

| Score | Level | Meaning |
|-------|-------|---------|
| 0 | Not required | Not relevant for this role |
| 1 | Aware | Understands the concept, no hands-on experience |
| 2 | Practitioner | Has applied in at least one real project |
| 3 | Expert | Leads, defines, and advances the field |

**★ Must-have** — competencies marked with ★ are stop-factors: a score below 2 is a disqualifying gap regardless of overall profile strength.

---

## How to use this framework

### For hiring teams
- Use the competency matrix to build structured interview scorecards
- Replace subjective gut-feel with role-specific must-have thresholds
- Compare candidates on the same dimensions across geographies and interviewers

### For candidates
- Understand what robotics companies actually look for beyond keywords
- Identify genuine gaps vs. surface-level skill mismatches
- Prepare for technical interviews with domain-specific depth

### For educators and researchers
- Map curricula against industry expectations
- Identify where academia and industry expectations diverge
- Understand the multidisciplinary nature of modern robotics roles

---

## Key insights from 200+ interviews

**1. Robotics ≠ software engineering**
Standard skills taxonomies treat robotics as a subset of software. It isn't. The critical differentiator is integration ability — can this person make mechanical, electrical, and software systems work together reliably in the real world?

**2. The rarest profiles**
RL Loco-manipulation engineers (simultaneous locomotion + manipulation policy) represent fewer than 300 people globally with genuine hands-on experience. Standard ATS platforms cannot identify them.

**3. Sim-to-real is the real filter**
Candidates who have only trained in simulation and never deployed on hardware consistently underperform expectations. This framework treats real-hardware deployment experience as must-have for all hardware-facing roles.

**4. VLA roles are splitting**
Two distinct profiles are emerging: engineers who pre-train foundation models (deep learning background, robotics optional) and engineers who fine-tune and deploy them (robotics-first, learning-aware). These require different hiring pipelines.

**5. Teleoperation UX is an invisible gap**
The intersection of robotics and human-computer interaction is where most companies struggle most. Cognitive load, control mappings, and operator fatigue are engineering problems — but no standard robotics taxonomy covers them.

---

## Files in this repository

| File | Description |
|------|-------------|
| `README.md` | This document |
| `competency_matrix_v4.csv` | Full competency matrix — 9 roles × 48 competencies |

---

## Contributing

This framework reflects one company's experience (humanoid robotics, London-based, 2023–2025). It is intentionally opinionated and based on real hiring data — not theoretical job architecture.

Contributions welcome:
- Additional role profiles (field robotics, agricultural robotics, surgical robotics)
- Regional calibration (US vs. EU vs. Asia-Pacific hiring norms)
- Corrections to competency levels based on your hiring experience

Open an issue or submit a pull request.

---

## About

Created by **Ekaterina Selezneva**, Head of Talent Acquisition at a humanoid robotics company (London, UK).

Built during the process of scaling a robotics team from 0 to 200 engineers across UK, US, and Canada — after discovering that every existing tool failed to evaluate the profiles we needed.

[LinkedIn](https://linkedin.com/in/your-profile) · [Contact](mailto:your@email.com)

---

*This framework is released as open source. Use it, adapt it, improve it.*
*If it helps your team hire better — that's the point.*
