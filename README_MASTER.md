# SDN-PQC MASTER EXPERIMENTAL ARCHIVE — 2026-10-29

**Locked research title:** Controller-Orchestrated Crypto-Agile Post-Quantum Migration for Scalable Software-Defined Networks

## Start here

- `00_MASTER_INDEX/MASTER_COMPARISON_INDEX.xlsx` — styled dashboard, study registry, per-stage metrics, file index and evidence restrictions.
- `00_MASTER_INDEX/STUDY_REGISTRY.csv` — research-wide stage provenance and primary row counts.
- `00_MASTER_INDEX/MASTER_POLICY_RUN_LEVEL_52970.csv` — 52,970 normalized run-level records, with different metric names labeled explicitly.
- `00_MASTER_INDEX/MASTER_COMPARISON_LONG.csv` — 348 source-backed per-policy results in long form; never average unlike metrics across studies.
- `00_MASTER_INDEX/COMPARISON_HIGHLIGHTS.csv` — B4, P1 and P1-v1.1 selected contrasts, labeled by stage.
- `00_MASTER_INDEX/FILE_MANIFEST_SHA256.csv` — SHA-256 and path for every original source file embedded in this archive.
- `00_MASTER_INDEX/ALL_RAW_CSV_CATALOG.csv` — location, row count and checksum of source CSV files.
- `00_MASTER_INDEX/EVIDENCE_BOUNDARIES.md` — scientific claim limitations.
- `00_MASTER_INDEX/MASTER_AUDIT_SUMMARY.json` — machine-readable counts, pending work and caveats.

## Content folders

`01_LOCKED_PROTOCOLS_AND_REFERENCES` contains research protocol and version-locked hardware/software descriptions. The 900dpi figure is conceptual artwork and **not a photograph proving lab installation**.

`02_EXTERNAL_SOURCE_ORIGINAL` contains the pinned public GitHub benchmark ZIP. External observed TLS data belongs to its original authors and is not our independent measurement.

`03_EXECUTED_*` preserve local TLS pilot, seven-role reconnect experiments and the external-means-informed TLS proof-of-concept.

`04_EXTERNAL_TRACE_REPLAY_MODELED` and `05_EXP07_FAIR_CONCURRENCY_MODELED` preserve models, raw external inputs, offline job schedules, results, report and graphs. Their migration timings are **modeled**.

`06_EXP08_LIVE_TLS_APPLICATION`, `07_EXP09A_MBB_BMB_ORIGINAL_AND_RERUN`, and `08_EXP09B_DEADLINE_HELDOUT` preserve live single-host application/TLS measurements. These are real socket/TLS operations but not genuine isolated SDN networks.

`09_EXP10U_USERSPACE_OPENFLOW_EXECUTED` contains custom TCP-forwarding switches using an OpenFlow 1.3 subset (flow-mod/barrier), actual routed TLS operations and controller logs. Not ONOS, not OVS, not physical Ethernet forwarding.

`10_NOT_EXECUTED_*` contains deployment source and mock/local security test code only; no genuine ONOS/OVS performance results.

`11_H1_PHYSICAL_DEPLOYMENT_NOT_EXECUTED` contains physical-lab preparation only.

`12_PRIOR_DELIVERY_PACKAGES_DUPLICATE_CONTENT` contains original ZIP deliveries for convenience and archival provenance; **do not sum their data as independent experiments**.

## Primary evidence conclusion

- GitHub source: 18,000 third-party TLS observations extracted and used for external performance profiling.
- Live single-host experiments establish authenticated TLS operation, endpoint mechanism behavior and short response gaps; the prototype is CPU-scheduled localhost routing, not controlled network congestion.
- Make-before-break (MBB) generally reduced observed response gaps versus break-before-make (BMB) on identical testbeds. This effect is **not unique to P1**.
- Locked P1 and exploratory P1-v1.1 did not demonstrate statistically supported superiority over the strong B4 load-aware policy on primary observed endpoint gap metrics in the held-out single-host tests.
- Actual ONOS 2.7.0, Open vSwitch 3.3.9, congestion-conditioned OpenFlow experiments, and seven physical H1.0 PC results are **pending**.

## Integrity audit

The SHA-256 file manifest covers all source files, and the archive ZIP is tested after creation. Original past deliveries are preserved separately where available. All data were collected in earlier experiments; **this consolidation does not invent or rerun data**.
