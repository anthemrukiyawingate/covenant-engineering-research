# Data, LIMS and data governance

*As of 2 October 2026.*

## Laboratory information management (LIMS)

The study runs on a file-based laboratory information management system: a version-controlled repository in which every planning document, record and analysis is a committed file.

| Component | What it holds | Count (2 Oct 2026) |
| --- | --- | --- |
| Pre-registrations | Success conditions, predictions, analysis plan and amendments, written before each generation trains | 45 documents (42 pre-registrations and 3 independent reads filed beside them) |
| Run records | One record per fired study, with each verdict generated from the sealed analysis output | 20 records (48 reports in all) |
| Sealed analysis scripts | Each fixed by a SHA-256 fingerprint before results are read, each with a built-in self-test | 17 scripts |
| Trial ledger | Every test that fired, with its verdict quoted verbatim from its record (Markdown and JSON) | 108 tests |
| Commit history | Each change is one commit | 322 commits |

**The trial ledger** is the denominator for every claim. Its integrity check, `ledger_check.py`, refuses to pass if a verdict is not quoted verbatim from its record. Current totals by test type:

| Test type | Tests | Licensed or held | Not licensed or refuted | Unresolved | Other |
| --- | --- | --- | --- | --- | --- |
| Primary | 29 | 13 | 5 | 10 | 1 (screen) |
| Secondary | 43 | 26 | 14 | — | 3 |
| Gate (validity checks) | 19 | 12 | 4 | — | 3 (2 flags fired) |
| Declared descriptive | 17 | 4 | 4 | — | 9 (1 flag fired) |

## Data governance

- **Fixed before seen.** Success conditions are written down and analyses are sealed by fingerprint before any data exist. A pre-registration changed after firing must be disclosed as such, and its original stays in the record.
- **Nothing withdrawn.** Failed tests, refuted predictions and discarded designs stay in the ledger and the records.
- **Provenance per run.** Each training run writes a metadata file (corpus fingerprint, model, recipe, seed, run time) and an environment snapshot (`pip-freeze.txt`).
- **Seeds controlled.** A seed registry with a hard-fail guard stops a seed from being reused across studies. Confirmatory tests use fresh seed ranges.
- **Independent reads.** Another team member checks the seals, the analysis and the verdict before a result is reported. Where a run fired before that read, the record says so.
- **Numbers traced to source.** Documents that report numbers (the abstract, Chapter 7) are checked by a script that finds every number in the source records. Figures are drawn from the sealed analyses' own data and stop if a headline number disagrees with the ledger.
- **Methods corrections are disclosed, not buried.** On 1 October 2026 two weight-decay settings produced bit-identical models. The trainer runs AdamW on bfloat16 weights without a full-precision copy, so the nominal weight decay never took effect, in any run. Every arm shares the same recipe, so no comparison changes. The finding is recorded in `lims/METHODS-NOTE-bf16-optimizer-precision.md` and in the pre-registration where it was found; earlier pre-registrations are left as written.
- **Storage and release.**
  - Run outputs (checkpoints, readouts, metadata) sit on the lab's network storage.
  - Records and code sit in a private version-controlled repository.
  - Before any copy leaves the lab, it is checked for lab addresses and credentials.
  - Public release: the repository carries the README, figures and verified references. Each tagged release adds two archives: the code and every LIMS record at the tagged commit, and the run outputs (readouts, run metadata, logs and environment snapshots; no model checkpoints).
  - Before release, lab network addresses are replaced, and every changed file is listed with its original and redacted SHA-256 in `REDACTION-MANIFEST.json`. A release builds only if every analysis self-test and the ledger check pass on the redacted copy. Model weights follow in a later release.

## Summary of the data

| Item | Value |
| --- | --- |
| Model | Pythia-410m (generations 1–10 and the Aim 2 designs); generation 11 adds nine independent Pythia-410m pretraining runs (PolyPythias) and Qwen2.5-0.5B |
| World | 32-position ring; 736 training pairs, with 256 held-out pairs at distances 7–10 (generation 7 on) |
| Languages | A (boundaries 0 and 16), B′ (boundaries 3 and 13), random-split control, untrained twins |
| Naming records | 128 per language (4 per position); dose shares 0, 0.25, 0.5, 1 |
| Training runs recorded | 1,165 run-metadata files across 1,337 result directories (generation 11 runs keep two copies of their metadata file, so files exceed runs) |
| Environment snapshots | 174 `pip-freeze.txt` files |
| Typical run | 4,000 steps; median 11.7 min per run (sample of 365 runs) on NVIDIA GB10 |
| Generations | 1–11, plus Aim 2 transfer and own-task designs (including the own-task harm test) |

**Not measured here:** the total size of the stored run data, and the token count of the training corpora. The run counts come from a scan of the run store to four folder levels.
