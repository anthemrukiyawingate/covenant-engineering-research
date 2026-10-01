# Data, LIMS and data governance

*As of 1 October 2026.*

## Laboratory information management (LIMS)

The study runs on a file-based laboratory information management system: a version-controlled repository in which every planning document, record and analysis is a committed file. Nothing that counts as evidence lives only in a notebook or a chat.

| Component | What it holds | Count (1 Oct 2026) |
| --- | --- | --- |
| Pre-registrations | Success conditions, predictions, analysis plan and amendments, written before each generation trains | 45 documents |
| Run records | One record per fired study, with each verdict generated from the sealed analysis output | 20 records (45 reports in all) |
| Sealed analysis scripts | Each fixed by a SHA-256 fingerprint before results are read, each with a built-in self-test | 14 scripts |
| Trial ledger | Every test that fired, with its verdict quoted verbatim from its record (Markdown and JSON) | 101 tests |
| Commit history | Each change is one commit | 294 commits |

**The trial ledger** is the denominator for every claim. Its integrity check, `ledger_check.py`, refuses to pass if a verdict is not quoted verbatim from its record. Current totals by test type:

| Test type | Tests | Licensed or held | Not licensed or refuted | Unresolved | Other |
| --- | --- | --- | --- | --- | --- |
| Primary | 26 | 10 | 5 | 10 | 1 (screen) |
| Secondary | 42 | 25 | 14 | — | 3 |
| Gate (validity checks) | 17 | 11 | 3 | — | 3 (2 flags fired) |
| Declared descriptive | 16 | 3 | 4 | — | 9 (1 flag fired) |

## Data governance

- **Fixed before seen.** Success conditions are written down and analyses are sealed by fingerprint before any data exist. A pre-registration changed after firing must be disclosed as such, and its original stays in the record.
- **Nothing withdrawn.** Failed tests, refuted predictions and discarded designs stay in the ledger and the records.
- **Provenance per run.** Each training run writes a metadata file (corpus fingerprint, model, recipe, seed, run time) and an environment snapshot (`pip-freeze.txt`).
- **Seeds controlled.** A seed registry with a hard-fail guard stops a seed from being reused across studies. Confirmatory tests use fresh seed ranges.
- **Independent reads.** Another team member checks the seals, the analysis and the verdict before a result is reported. Where a run fired before that read, the record says so.
- **Numbers traced to source.** Documents that report numbers (the abstract, Chapter 7) are checked by a script that finds every number in the source records. Figures are drawn from the sealed analyses' own data and stop if a headline number disagrees with the ledger.
- **Storage and release.**
  - Run outputs (checkpoints, readouts, metadata) sit on the lab's network storage.
  - Records and code sit in a private version-controlled repository.
  - Before any copy leaves the lab, it is checked for lab addresses and credentials.
  - Public release is curated: this review copy carries the README, figures and verified references.

## Summary of the data

| Item | Value |
| --- | --- |
| Model | Pythia-410m, one public base model |
| World | 32-position ring; 736 training pairs, with 256 held-out pairs at distances 7–10 (generation 7 on) |
| Languages | A (boundaries 0 and 16), B′ (boundaries 3 and 13), random-split control, untrained twins |
| Naming records | 128 per language (4 per position); dose shares 0, 0.25, 0.5, 1 |
| Training runs recorded | 849 run-metadata files across 1,125 result directories |
| Environment snapshots | 174 `pip-freeze.txt` files |
| Typical run | 4,000 steps; median 11.7 min per run (sample of 365 runs) on NVIDIA GB10 |
| Generations | 1–10, plus Aim 2 transfer and own-task designs |

**Not measured here:** the total size of the stored run data, and the token count of the training corpora. The run counts come from a scan of the run store to four folder levels.
