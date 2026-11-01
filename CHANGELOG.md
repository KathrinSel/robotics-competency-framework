# Changelog

All notable changes to the Robotics Competency Framework are documented here.

## [1.3.0] — 2026-11-01

Requirement tiers and interview gates, recalibrated with hiring manager input.

### Added
- Ideal-profile tier (◆): competencies that mark an ideal candidate without disqualifying those who lack them. In the interview data, these separated Strong Yes from Yes
- Interview gates for every role: algorithmic coding, and system design & technical execution — assessed in interviews, never from CVs
- New calibration status `jd_and_hm_input`, and a `search_status` field for roles no longer being hired
- Two new sections in `evidence-guide.md`: large-scale model training from scratch, and system design & technical execution
- Insight #9 and a caveat on interview stage coverage: role calibration is based on specialization interviews, while most rejections happen at coding and system design

### Changed
- Must-haves reduced from 102 to 32 across 9 roles (3–4 per role), keeping only the competencies that separated hire from no-hire
- VLA Pre-Training: must-haves are transformer depth, GPU training efficiency, distributed training, and large-scale training from scratch; robotics understanding and hands-on VLA moved to the ideal profile
- `llm_vlm_pretraining` renamed to `large_scale_training` (LLM / VLM / vision / world models — scale of the run, not model type)
- `real_hardware_deployment` generalised to any physical robot and moved to Software & HW; now a must-have for Robot Learning Engineer and Staff Control
- Manipulation Capability Engineer renamed to Robot Learning Engineer, matching the public job title (`robot_learning_engineer`)
- Senior RL Engineer (VLA): robotics experience moved to the ideal profile per hiring manager input
- Simulation Engineer: search closed without a hire; remains a rejections-only profile

### Fixed
- Removed simulation competencies wrongly required for VLA Pre-Training (`gpu_parallel_simulation`, `simulation_ci`); `eval_design` lowered to 1
- Simulation Engineer requires at least one simulator, not both Isaac Lab and MuJoCo; dexterous grasping and reward design lowered to ideal profile, per the JD
- Teleoperation Controls & Haptics: `user_testing` lowered to 1
- Robotics Sim & Control: `policy_optimization` raised to 2, per the JD
- Academic publications capped at level 1 for all roles

## [1.2.0] — 2026-11-01

Machine-readable release: the framework is now a single source of truth that tools can consume directly.

### Added
- `framework.yaml` — the single source of truth for domains, competencies, roles, required levels and must-haves
- `framework.json` — generated from `framework.yaml`, for tools and integrations
- `tools/build.py` — validates `framework.yaml` and regenerates the CSV and JSON
- Stable competency ids (e.g. `retargeting`, `action_chunking`) so other tools can reference competencies reliably
- Calibration status for every role: `interview_calibrated`, `partially_calibrated`, `rejections_only`, or `jd_only`, with the data basis behind it

### Changed
- `competency_matrix.csv` is now generated from `framework.yaml` and replaces `competency_matrix_final_v2.csv` (same values)
- Corrected the Staff Control SW Engineer insight: data covers two candidates, one of whom received an offer

## [1.1.0] — 2026-11-01

Recalibrated against real interview feedback, hiring decisions, and hiring manager input.

### Added
- `evidence-guide.md` — CV-stage signals and interview examples for each scoring level, for the most-tested competencies (response to [Issue #1](https://github.com/KathrinSel/robotics-competency-framework/issues/1))
- New competencies surfaced by interview data, including: real hardware deployment, transformer implementation depth, GPU memory & training efficiency, action chunking & async inference, retargeting strategies, physics solver understanding, timing concepts, bilateral teleoperation, passivity theory, production systems mindset
- Teleoperation split into two profiles: SW (VR) and Controls & Haptics
- "Key insights" section — 8 findings from interview data
- "Important caveats" section, including data limitations
- LICENSE (CC BY 4.0) and CITATION.cff

### Changed
- Competency levels recalibrated against interview feedback for 7 of 9 roles. Senior RL Engineer (VLA) and Robotics Sim & Control Engineer are still based on job descriptions only
- RL theory depth, academic publications, and combined loco+manip lowered for RL Locomanipulation — not predictive of hiring outcomes in the data
- VLA Pre-Training Engineer requirements raised per hiring manager input
- Matrix expanded from 48 to 72 competencies across 11 domains

## [1.0.0]

Initial public release.

- Competency matrix for 9 robotics role profiles, 10 domains, 48 competencies
- Based on job descriptions for each role
- 0–3 scoring system with must-have markers
