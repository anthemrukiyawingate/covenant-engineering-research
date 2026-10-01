## List of figures

### Overview

**The ring world and its two languages.** The 32-position ring. Outer ring: language A, boundaries at 0 and 16. Inner ring: language B′, boundaries at 3 and 13.

![The ring world and its two languages](figures/fig-world.png)

**Trial ledger.** Every main (primary) test by verdict: 10 licensed, 5 not licensed or refuted, 10 unresolved, 1 screen (26 in all).

![Trial ledger: verdicts of the 26 main tests](figures/fig-ledger.png)

### Generation 1 (first instrument)

These figures show generation 1, read on the first instrument: 128 held-out pairs, and the rank of each language's own placement among its 16 rotations. Language B here is A rotated by 8 positions. The structurally different language B′ was introduced later.

**Figure 1. The world.** Thirty-two positions on a ring, each shown to the model as an arbitrary token; the model learns only whether two positions are near (within 8 steps) or far. Language A splits the ring at positions 0 and 16.

![Figure 1. The world](figures/gen1/fig1-world.png)

**Figure 2. The rotation test.** For each trained model, the boundary effect computed at the language's own placement and at all 15 turned copies on the same model. If the language shaped the model, its own placement should stand out.

![Figure 2. The rotation test](figures/gen1/fig2-rotation-waves.png)

**Figure 3. The tally.** Each dot is one model, placed at the rank of its language's own placement among the sixteen; the shaded column is first place. Hollow dots fell below the accuracy gate.

![Figure 3. The tally](figures/gen1/fig3-rank-tally.png)

**Figure 4. How large the effect is.** Seed by seed, the boundary effect at A's split in the model trained with language A against the model trained with the same seed and no language. The paired difference is about three logits.

![Figure 4. How large the effect is](figures/gen1/fig4-effect-size.png)

**Figure 5. How close to the boundary the peak sits.** How many rotations separate the best placement from the language's own placement. Chance puts the mean at 4; language A's models average 0.4. A softer, descriptive reading, not the pre-registered test.

![Figure 5. How close to the boundary the peak sits](figures/gen1/fig5-phase-distance.png)

**Figure 6. The accuracy gate.** A model is read only if it learned the task to between 0.60 and 0.95 accuracy on the held-out pairs. Three of the twenty models fell below 0.60.

![Figure 6. The accuracy gate](figures/gen1/fig6-accuracy-gate.png)

**Figure 7. Where in the model the split lives.** An independent, layer-by-layer reading of the model's internal representation. A cell is coloured when that split fits the representation of the ring better than every rotation and reflection of it.

![Figure 7. Where in the model the split lives](figures/gen1/fig7-geometry-layers.png)

**Figure 8. The four conditions learned the same ring.** The fraction of "far" answers by ring distance, averaged over seeds. The curves overlap, so differences between conditions are not differences in how well the task was learned.

![Figure 8. The four conditions learned the same ring](figures/gen1/fig8-response-curves.png)

### Generations 7 to 9 (second instrument)

Each figure is drawn from its sealed analysis's own data loader. Before drawing, it recomputes its headline number and stops if that number does not match the trial ledger.

**Figure 9. Generation 7 core.** Paired change in the boundary effect at A's boundaries, each language-A model against its untrained twin (n = 20; licensed).

![Figure 9. Generation 7 core](figures/gen7-9/fig9-gen7-core.png)

**Figure 10. Generation 7 dose.** The boundary effect against the share of language A taught (0, 0.25, 0.5, 1), one line per seed (10 of 11 seeds with a positive slope; licensed).

![Figure 10. Generation 7 dose](figures/gen7-9/fig10-gen7-dose.png)

**Figure 11. Language B′.** The boundary effect at B′'s own boundaries, B′-trained models against their untrained twins (n = 30; licensed). Specificity was settled later by generations 8 and 9.

![Figure 11. Language B′](figures/gen7-9/fig11-gen7-bprime.png)

**Figure 12. Generation 8.** Change in the boundary effect at A's boundaries for each turned copy of B′, plotted against how much that copy agrees with A (n = 29). The negative effect is licensed; the trend line across agreement is descriptive.

![Figure 12. Generation 8](figures/gen7-9/fig12-gen8-overlap.png)

**Figure 13. Generation 9.** The disagreeing copy of B′ lowers the effect at A's boundaries more than a low-disagreement copy with the same accuracy cost (n = 30; licensed). The drop is not explained by the shared accuracy cost.

![Figure 13. Generation 9](figures/gen7-9/fig13-gen9-accuracy-matched.png)
