# Robotics Competency Framework

**An open competency standard for hiring engineers in humanoid and mobile robotics.**

Built by a talent practitioner who conducted 200+ technical interviews across UK, US, and Canada — and calibrated against real interview feedback, hiring decisions, and hiring manager input.

---

## Why this exists

Robotics sits at the intersection of mechanical engineering, embedded software, AI, and safety-critical systems. A qualified robotics engineer is not a software engineer with a broader stack — they are a genuinely multidisciplinary profile that standard hiring tools cannot evaluate.

Existing HR infrastructure was built for two scenarios: high-volume hiring (retail, logistics) or generic software engineering. Robotics fits neither. The result: companies either hire the wrong people slowly, or fail to hire at all.

This framework was created to fill that gap — providing a shared language for evaluating robotics talent across specialisations, seniority levels, and geographies.

**What makes this different from other frameworks:**
This is not theoretical job architecture. Every competency level and must-have threshold was calibrated against real interview feedback — including both successful and rejected candidates, and direct input from hiring managers.

---

## What's inside

### 9 Role Profiles

| Role | Focus |
|------|-------|
| RL Engineer — Locomanipulation | Learning-based policies for legged robots with real hardware deployment |
| VLA Pre-Training Engineer | Foundation model pre-training — primarily a deep learning role |
| Senior RL Engineer (VLA) | RL + multimodal transformers + distributed training |
| Robotics Sim & Control Engineer | Sim-driven hardware design + RL + control theory |
| Simulation Engineer — Manipulation | Production-grade physics simulation for dexterous tasks |
| Staff Control SW Engineer | Production-grade real-time control systems ownership |
| Teleoperation SW Engineer (VR) | Low-latency VR teleoperation systems |
| Teleoperation Engineer (Controls & Haptics) | Bilateral control, haptics, real-time operator systems |
| Manipulation Capability Engineer | Post-training, fine-tuning, and deployment for end-user tasks |

### 11 Competency Domains · 70 Competencies

| Domain | Coverage |
|--------|----------|
| D1 · RL Core | Policy optimization, reward design, curriculum, imitation learning, distributed training |
| D2 · Simulation | Isaac Lab, MuJoCo, physics solvers, GPU-parallel sim, domain randomization, timing |
| D3 · Locomotion | Legged/humanoid robots, dynamic balance, kinematics, WBC, real hardware deployment |
| D4 · Manipulation | Dexterous grasping, in-hand manipulation, deformable objects |
| D5 · Locomanipulation | Combined loco+manip policies, multi-behavior learning |
| D6 · Perception & VLA | VLA models, transformer depth, GPU training efficiency, action representations |
| D7 · Control Systems | MPC, impedance/force control, real-time architecture, bilateral teleoperation, haptics |
| D8 · Software & HW | ROS2, C++, Python/PyTorch, real-time Linux, CI/CD, production systems |
| D9 · Teleoperation | System architecture, retargeting, motion capture, VR, haptics, latency |
| D10 · Robot Learning | Action chunking, data quality, policy evaluation, deployment |
| D11 · Research & Collab | Publications, experiment design, HW↔SW collaboration, technical leadership |

### Scoring System

| Score | Level | Meaning |
|-------|-------|---------|
| 0 | Not required | Not relevant for this role |
| 1 | Aware | Understands the concept, no hands-on experience |
| 2 | Practitioner | Has applied in at least one real project |
| 3 | Expert | Leads, defines, and advances the field |

**★ Must-have** — competencies marked with ★ are stop-factors: a score below 2 is a disqualifying gap regardless of overall profile strength.

---

## Key insights from 200+ interviews

**1. Academic profile is not a predictor of success**
A PhD candidate with ICRA/IROS/RAL publications received a Weak Hire for the RL Locomanipulation role. Two hired candidates had gaps in RL theory (GAE, surrogate loss derivation) but were hired for their real hardware deployment experience. Standard recruiting filters by academic credentials — and gets it wrong.

**2. Production ownership matters more than theory depth**
For Staff Control SW Engineer, both hired candidates had notable gaps in robotics-specific controls knowledge (IK, WBC, inverse dynamics). Both were hired for their production systems mindset, fleet-scale deployment experience, and hardware ownership. The candidate with the deepest control theory but weakest production experience was rejected.

**3. VLA Engineer is primarily a deep learning role**
The hired VLA Pre-Training engineer came from a recommendation systems background — not robotics. Robotics domain knowledge is nice-to-have; transformer implementation depth and GPU training efficiency are the real filters. Standard robotics job boards will miss these candidates entirely.

**4. Retargeting is the hidden filter in Teleoperation**
Most candidates with robotics or AV background arrive without understanding the retargeting layer (converting human motion to robot commands, absolute vs relative strategies, user calibration). This was the most common failure point across Teleoperation interviews — yet it appears in almost no standard robotics job descriptions.

**5. Keyword matching fails completely for Manipulation Capability Engineer**
Candidates who knew all the terms (DAgger, action chunking, diffusion policy, async inference) still failed interviews. The role filters on understanding failure modes and system-level reasoning — not vocabulary. A candidate who can explain what action chunking is will not necessarily pass; one who can explain what goes wrong with async action chunking under distribution shift will.

**6. Sim Engineer and RL Engineer are fundamentally different profiles**
Despite both working with simulators, these roles require different thinking. Sim Engineer requires depth in physics solver internals, timing concepts, and production simulation infrastructure. RL Engineer requires policy training depth. Candidates strong in RL locomotion were flagged as better fits for the robot learning team, not simulation.

**7. Teleoperation has two distinct halves that rarely coexist**
No single candidate fully covered both the VR/streaming half (Unity, WebRTC, wireless, immersive telepresence) and the controls/haptics half (bilateral control, passivity, force feedback, haptic devices). One hiring manager explicitly suggested opening two separate positions. Companies expecting one person to cover both will be disappointed.

**8. The locomanipulation title is misleading**
Despite the role being called "RL Locomanipulation Engineer", interviews focused entirely on locomotion depth. Manipulation was not tested as a separate competency in any interview reviewed. Combined loco+manip policy experience is a differentiator but not a filter.

---

## Important caveats

**Simulation Engineer:** The matrix for this role is based exclusively on rejected candidates — no hired candidate data was available. We know what is insufficient, but cannot confirm what is sufficient. This should be treated as directional, not definitive.

**Interview calibration variance:** For several roles, two interviewers on the same candidate gave opposite recommendations (3/4 vs 2/4). This reflects genuine disagreement about role priorities — not candidate inconsistency. Teams should align internally on which competencies are true stop-factors before using this framework.

---

## How to use this framework

### For hiring teams
- Align your interview panel on must-have thresholds before starting the process
- Use the competency matrix to build structured scorecards
- Do not treat academic publications as a proxy for engineering depth
- For Teleoperation and Staff Control roles: production experience outweighs theoretical depth

### For candidates
- Understand what is actually tested — not just what appears in the JD
- For VLA roles: demonstrate ML systems depth, not robotics vocabulary
- For RL Locomanipulation: real hardware deployment experience is non-negotiable
- For Manipulation Capability: prepare to explain failure modes, not just concepts

### For educators and researchers
- The gap between academic robotics and industry hiring is significant
- Publications at top venues do not guarantee strong performance in production engineering roles
- The most valued competencies — production ownership, hardware deployment, sim-to-real on real systems — are rarely developed in academic settings

---

## Files in this repository

| File | Description |
|------|-------------|
| `README.md` | This document |
| `competency_matrix_final_v2.csv` | Full matrix — 9 roles × 70 competencies, calibrated against real interview data |

---

## Data sources

This framework is based on:
- 200+ technical interviews conducted across UK, US, and Canada (2023–2025)
- Real interview feedback from hiring managers and technical interviewers
- Hiring decisions (accepted and rejected candidates) across 9 role types
- Direct hiring manager input on role expectations and ideal candidate profiles
- Job descriptions for all 9 roles

---

## Contributing

Contributions welcome:
- Additional role profiles (field robotics, agricultural robotics, surgical robotics)
- Interview feedback data to calibrate existing profiles further
- Regional hiring norm differences (US vs EU vs Asia-Pacific)

Open an issue or submit a pull request.

---

## About

Created by **Kathrin Selezneva**, Lead of Talent Acquisition at a humanoid robotics company (London, UK).

Built during the process of scaling a robotics team from 0 to 200 engineers across UK, US, and Canada — after discovering that every existing tool failed to evaluate the profiles we needed.

[LinkedIn](https://www.linkedin.com/in/ekaterinaselezneva-hr/) · [Contact](mailto:seleznevaem@gmail.com)

---

*This framework is released as open source. Use it, adapt it, improve it.*
*If it helps your team hire better — that is the point.*
