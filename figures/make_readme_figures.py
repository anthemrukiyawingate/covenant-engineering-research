#!/usr/bin/env python3
"""Figures for the public README (ELRD, 2026-10-01).
fig-world.svg/png  : the 32-position ring with language A (boundaries 0 and 16) and language B' (boundaries 3 and 13),
                     read from the study's own definitions (A: lims/PREREGISTRATION-gen1-wheel-v2.md; B': lims/PREREG-gen7-
                     second-lexicon-Bprime-DRAFT0.md line 11, "bounds (3, 13), unequal categories").
fig-ledger.svg/png : the trial ledger's primary-test verdicts, taken from the output of scripts/ledger_check.py at draw time
                     (pass --ledger-line "primary: ..." copied from that output; nothing typed by hand).
Usage: python3 make_readme_figures.py --ledger-line "$(python3 scripts/ledger_check.py | grep '^primary:')"
"""
import argparse, math, re
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

ap = argparse.ArgumentParser(); ap.add_argument("--ledger-line", required=True); a = ap.parse_args()
N = 32
def ring(ax, r_in, r_out, cat, colors, label):
    for p in range(N):
        t0 = 90 - (p + 0.5) * 360 / N; t1 = 90 - (p - 0.5) * 360 / N
        ax.add_patch(Wedge((0, 0), r_out, t0, t1, width=r_out - r_in, facecolor=colors[cat(p)], edgecolor="white", lw=1))
    ax.text(0, r_out + 0.06, "", ha="center")
    return label
def boundary(ax, pos, r_in, r_out, color):
    th = math.radians(90 - (pos - 0.5) * 360 / N)
    ax.plot([r_in * math.cos(th), r_out * math.cos(th)], [r_in * math.sin(th), r_out * math.sin(th)], color=color, lw=3)
fig, ax = plt.subplots(figsize=(6.4, 6.4)); ax.set_aspect("equal"); ax.axis("off")
A = lambda p: 0 if p < 16 else 1
Bp = lambda p: 0 if 3 <= p <= 12 else 1
ring(ax, 0.78, 1.0, A, ["#2b6cb0", "#90cdf4"], "A"); ring(ax, 0.52, 0.74, Bp, ["#c05621", "#fbd38d"], "B'")
for b in (0, 16): boundary(ax, b, 0.78, 1.0, "black")
for b in (3, 13): boundary(ax, b, 0.52, 0.74, "black")
for p in range(0, N, 4):
    th = math.radians(90 - p * 360 / N); ax.text(1.1 * math.cos(th), 1.1 * math.sin(th), str(p), ha="center", va="center", fontsize=9)
ax.text(0, 0.08, "32 positions", ha="center", fontsize=11)
ax.text(0, -0.08, "near = within 8 steps", ha="center", fontsize=9, color="#444")
ax.text(0, -1.27, "Outer ring: language A (boundaries 0 | 16).  Inner ring: language B′ (boundaries 3 | 13).", ha="center", fontsize=9)
ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.35, 1.25)
for ext in ("svg", "png"): fig.savefig(f"fig-world.{ext}", dpi=160, bbox_inches="tight")
plt.close(fig)

m = re.match(r"primary: (\d+) tests; LICENSED/HELD (\d+); NOT LICENSED/REFUTED (\d+); OTHER (\d+); UNRESOLVED/UNDECIDED (\d+)", a.ledger_line.strip())
assert m, "ledger line not recognised: " + a.ledger_line
tot, lic, notl, oth, unr = map(int, m.groups()); assert lic + notl + oth + unr == tot
labels = ["Licensed", "Not licensed or refuted", "Unresolved", "Screen"]; vals = [lic, notl, unr, oth]
fig, ax = plt.subplots(figsize=(6.4, 2.6))
bars = ax.barh(labels[::-1], vals[::-1], color=["#718096", "#a0aec0", "#c05621", "#2b6cb0"])
for b, v in zip(bars, vals[::-1]): ax.text(b.get_width() + 0.15, b.get_y() + b.get_height() / 2, str(v), va="center", fontsize=10)
ax.set_xlabel(f"main (primary) tests, {tot} in all"); ax.spines[["top", "right"]].set_visible(False); ax.set_xlim(0, max(vals) + 2)
for ext in ("svg", "png"): fig.savefig(f"fig-ledger.{ext}", dpi=160, bbox_inches="tight")
print("figures written; ledger", tot, lic, notl, unr, oth)
