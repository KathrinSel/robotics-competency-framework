# Robotics Competency Framework

**An open competency standard for hiring engineers in humanoid and mobile robotics.**

Built by a talent practitioner who has conducted 1000+ interviews across UK, US, and Canada — and calibrated against real interview feedback, hiring decisions, and hiring manager input.

---

## Why this exists

Robotics sits at the intersection of mechanical engineering, embedded software, AI, and safety-critical systems. A qualified robotics engineer is not a software engineer with a broader stack — they are a genuinely multidisciplinary profile that standard hiring tools cannot evaluate.

Existing HR infrastructure was built for two scenarios: high-volume hiring (retail, logistics) or generic software engineering. Robotics fits neither. The result: companies either hire the wrong people slowly, or fail to hire at all.

This framework was created to fill that gap — providing a shared language for evaluating robotics talent across specialisations, seniority levels, and geographies.

**What makes this different from other frameworks:** This is not theoretical job architecture. Competency levels and must-have thresholds were calibrated against real interview feedback — including both successful and rejected candidates — and direct input from hiring managers. Every role states how it was calibrated, so you know how much to trust it.

---

## What's inside

### 9 Role Profiles

| Role | Focus | Calibration |
|------|-------|-------------|
| RL Engineer — Locomanipulation | Learning-based policies for legged robots with real hardware deployment | Interview-calibrated |
| VLA Pre-Training Engineer | Large-scale model pre-training — primarily a deep learning role | Interview-calibrated |
| Senior RL Engineer (VLA) | RL + transformer architectures + distributed training | JD + hiring manager input |
| Robotics Sim & Control Engineer | Sim-driven hardware design + RL + control theory | JD only |
| Simulation Engineer — Manipulation | Production-grade physics simulation for dexterous tasks | Rejections only (search closed) |
| Staff Control SW Engineer | Production-grade real-time control systems ownership | Interview-calibrated |
| Teleoperation SW Engineer (VR) | Teleoperation systems, retargeting, VR and low-latency streaming | Interview-calibrated |
| Teleoperation Engineer (Controls & Haptics) | Bilateral control, haptics, real-time operator systems | Partially calibrated |
| Robot Learning Engineer | Imitation learning, post-training, and deployment of manipulation policies on real robots | Interview-calibrated |

### 12 Domains · 74 Competencies

| Domain | Coverage |
|--------|----------|
| D1 · RL Core | Policy optimization, reward design, curriculum, imitation learning, distributed training |
| D2 · Simulation | Isaac Lab, MuJoCo, physics solvers, GPU-parallel sim, domain randomization, timing |
| D3 · Locomotion | Legged/humanoid robots, dynamic balance, kinematics, whole-body control |
| D4 · Manipulation | Dexterous grasping, in-hand manipulation, deformable objects |
| D5 · Locomanipulation | Combined loco+manip policies, multi-behavior learning |
| D6 · Perception & VLA | VLA models, transformer depth, large-scale training, GPU training efficiency, action representations |
| D7 · Control Systems | MPC, impedance/force control, real-time architecture, bilateral teleoperation, passivity |
| D8 · Software & HW | ROS2, C++, Python/PyTorch, real-time Linux, CI/CD, production systems, real hardware deployment |
| D9 · Teleoperation | System architecture, retargeting, motion capture, VR, haptics, latency |
| D10 · Robot Learning | Action chunking, data quality, policy evaluation, deployment |
| D11 · Research & Collab | Publications, experiment design, HW↔SW collaboration, technical leadership |
| G · Interview gates | Algorithmic coding, system design & technical execution — apply to every role |

### Scoring levels

| Score | Level | Meaning |
|-------|-------|---------|
| 0 | Not required | Not relevant for this role |
| 1 | Aware | Understands the concept, no hands-on experience |
| 2 | Practitioner | Has applied it in at least one real project |
| 3 | Expert | Leads, defines, and advances the field |

### Requirement tiers

| Mark | Tier | Meaning |
|------|------|---------|
| ★ | Must-have | Stop-factor: below level 2 is a disqualifying gap, regardless of overall profile strength. In the interview data, these separated hire from no-hire. 3–4 per role. |
| ◆ | Ideal profile | Marks an ideal candidate. Absence does not disqualify — the candidate stays in the process — but presence makes the case stronger. In the interview data, these separated Strong Yes from Yes. |
| — | Level only | Expected depth without special status. |

**Interview gates** — algorithmic coding and system design apply to every role and can only be assessed in an interview, never from a CV.

See [`evidence-guide.md`](evidence-guide.md) for what each level looks like at CV screening and in interviews.

---

## Key insights from interview data

**1. Academic profile is not a predictor of success**
A PhD candidate with ICRA/IROS/RAL publications received a Weak Hire for the RL Locomanipulation role. Two candidates who received offers had gaps in RL theory (GAE, surrogate loss derivation) but were chosen for their real hardware deployment experience. Standard recruiting filters by academic credentials — and gets it wrong.

**2. Production ownership matters more than theory depth**
For Staff Control SW Engineer, the candidate who received the offer had notable gaps in robotics-specific controls knowledge (IK, WBC, inverse dynamics), but owned fleet-scale production controls end to end. The candidate with the strongest control theory and the least production ownership was judged a better fit for an R&D whole-body control role than for this production one.

**3. VLA pre-training is primarily a deep learning role**
The hired VLA Pre-Training engineer came from a recommendation systems background — not robotics. The real filter is having actually trained large models from scratch, plus transformer implementation depth and GPU training efficiency. Robotics and hands-on VLA experience define the ideal candidate, but strong ML engineers without them are still considered. Agentic development or a few hours of fine-tuning do not count as model training.

**4. Retargeting is the hidden filter in Teleoperation**
Most candidates with robotics or AV background arrive without understanding the retargeting layer (converting human motion to robot commands, absolute vs relative strategies, user calibration). This was the most common failure point across Teleoperation interviews — yet it appears in almost no standard robotics job descriptions.

**5. Keyword matching fails completely for Robot Learning Engineer**
Candidates who knew all the terms (DAgger, action chunking, diffusion policy, async inference) still failed interviews. The role filters on understanding failure modes and system-level reasoning — not vocabulary. A candidate who can explain what action chunking is will not necessarily pass; one who can explain what goes wrong with async action chunking under distribution shift will.

**6. Sim Engineer and RL Engineer are fundamentally different profiles**
Despite both working with simulators, these roles require different thinking. Sim Engineer requires depth in physics solver internals, timing concepts, and production simulation infrastructure. RL Engineer requires policy training depth. Candidates strong in RL locomotion were flagged as better fits for the robot learning team, not simulation.

**7. Teleoperation has two distinct halves that rarely coexist**
No single candidate fully covered both the VR/streaming half (Unity, WebRTC, wireless, immersive telepresence) and the controls/haptics half (bilateral control, passivity, force feedback, haptic devices). One interviewer explicitly suggested opening two separate positions. Companies expecting one person to cover both will be disappointed.

**8. The locomanipulation title is misleading**
Despite the role being called "RL Locomanipulation Engineer", interviews focused entirely on locomotion depth. Manipulation was not tested as a separate competency in any interview reviewed. Combined loco+manip policy experience is a differentiator but not a filter.

**9. Most rejections happen outside the specialization interview**
Hiring managers report that most candidates fail the algorithmic coding round, and that among those who pass, the most common rejection comes at system design — usually for passive engagement rather than weak design. The specialization interview, which this framework's role calibration is based on, is rarely the stage that decides the outcome.

---

## Important caveats

**Interview stage coverage:** Role calibration is based on specialization-interview feedback. The coding and system design stages, where most rejections happen, are captured only as interview gates. See insight #9.

**Calibration differs by role:** Each role in `framework.yaml` carries a calibration status — `interview_calibrated`, `partially_calibrated`, `rejections_only`, `jd_and_hm_input`, or `jd_only` — and the data basis behind it. Treat `jd_only` and `jd_and_hm_input` roles as starting points, not calibrated profiles.

**Simulation Engineer:** The search for this role was closed without a hire. Its matrix is based only on rejected candidates: it shows what is insufficient, not what is sufficient. Treat it as directional, not definitive.

**Interviewer variance:** For several roles, two interviewers on the same candidate gave opposite recommendations (3/4 vs 2/4). This reflects genuine disagreement about role priorities — not candidate inconsistency. Teams should align internally on which competencies are true stop-factors before using this framework.

---

## How to use this framework

### For hiring teams
- Align your interview panel on must-have thresholds before starting the process
- Use the competency matrix to build structured scorecards
- When briefing recruiters or agencies, give them the must-haves (★) as the deciding criteria and the ideal-profile signals (◆) as tie-breakers
- Treat borderline candidates as a likely no — candidates who only just meet the bar are usually rejected later
- Do not treat academic publications as a proxy for engineering depth
- For Teleoperation and Staff Control roles: production experience outweighs theoretical depth

### For candidates
- Understand what is actually tested — not just what appears in the JD
- Prepare for algorithmic coding and system design: most candidates are rejected at these stages, not on domain knowledge
- For VLA pre-training: show that you have trained large models from scratch — say what scale and what went wrong
- For RL Locomanipulation: real hardware deployment experience is non-negotiable
- For Robot Learning Engineer: prepare to explain failure modes, not just concepts

### For educators and researchers
- The gap between academic robotics and industry hiring is significant
- Publications at top venues do not guarantee strong performance in production engineering roles
- The most valued competencies — production ownership, hardware deployment, sim-to-real on real systems — are rarely developed in academic settings

---

## Files in this repository

| File | Description |
|------|-------------|
| `framework.yaml` | Single source of truth — edit this file |
| `framework.json` | Generated from framework.yaml, for tools and integrations |
| `competency_matrix.csv` | Generated table view — 9 roles × 74 competencies |
| `evidence-guide.md` | What each scoring level looks like at CV screening and in interviews |
| `tools/build.py` | Validates framework.yaml and regenerates the CSV and JSON |
| `CHANGELOG.md` | Version history |
| `CITATION.cff` | Citation metadata |
| `LICENSE` | CC BY 4.0 |

---

## Data sources

This framework is based on:
- 1000+ candidate interviews conducted by the author across UK, US, and Canada
- Written feedback from around 30 specialization interviews across 7 role profiles, including candidates who received offers and candidates who were rejected — the basis for role calibration
- Direct hiring manager input on role expectations and ideal candidate profiles
- Job descriptions for all 9 roles

---

## Contributing

Contributions welcome:
- Additional role profiles (field robotics, agricultural robotics, surgical robotics)
- Interview feedback data to calibrate existing profiles further — especially for roles marked `jd_only` or `rejections_only`
- Regional hiring norm differences (US vs EU vs Asia-Pacific)

To change the matrix, edit `framework.yaml` and run `python tools/build.py` — it validates your change and regenerates the CSV and JSON. Open an issue or submit a pull request.

---

## About

Created by **Kathrin (Ekaterina) Selezneva**, Lead of Talent Acquisition at a humanoid robotics company (London, UK).

Built during the process of scaling a robotics team from 0 to 200 engineers across UK, US, and Canada — after discovering that every existing tool failed to evaluate the profiles we needed.

[LinkedIn](https://www.linkedin.com/in/ekaterinaselezneva-hr/) · [Contact](mailto:seleznevaem@gmail.com)

---

## License

This framework is licensed under [CC BY 4.0](LICENSE) — free to use, adapt, and share, including commercially, with attribution. To cite it, use the **Cite this repository** button on the right side of the repository page.

*This framework is released as open source. Use it, adapt it, improve it.*
*If it helps your team hire better — that is the point.*
