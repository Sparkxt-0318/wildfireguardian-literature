# BINDER_STRUCTURE.md

Physical binder layout for the Korea Code Fair. The binder is a *defense
instrument*, not a reading list. Its job is to let us answer a hostile question
in 30 seconds with a page in hand.

---

## Design principles

1. **Findable under pressure.** Tabs are questions, not topics. When a judge
   asks "isn't this just Cova?", we open the tab labelled *"Isn't this just
   Cova?"* — not the tab labelled "Trigger modeling."
2. **One page per threat.** A Tier 1 paper that takes more than one page to
   rebut is a paper we do not understand well enough yet.
3. **The threatening papers go in the binder.** Including the ones that
   weakened our claims. If a judge finds a paper we did not include, the
   omission is worse than the paper.
4. **Nothing in the binder is unverified.** Every citation on every page has
   passed `bibliography/verify_dois.py`.

---

## Section order

| Tab | Contents | Why here |
|---|---|---|
| **0. One page** | The claim, the comparator, the result, the limitation | First thing opened; the whole defense in one page |
| **1. What we claim** | `novelty/SURVIVING_CLAIMS.md`, condensed to a table | Precise claim wording; stops us over-claiming when nervous |
| **2. What we do NOT claim** | `novelty/ABANDONED_CLAIMS.md` | Disarms the strongest attacks by conceding first |
| **3. Closest prior art** | Top-10 ranking table + one-sentence differences | The single most likely line of questioning |
| **4. Tier 1 annotation sheets** | One page per paper, `MUST_PRINT.md` Tier 1 | Answering "have you read X?" with "yes, here" |
| **5. Method defense** | Comparator tuning, OSSE design, statistics | For the methodological judge |
| **6. Korea** | Korean prior art, agency systems, why Korea matters (or does not) | Q7; Korean judges will know this area better than we do |
| **7. Numbers** | Verified figures only, each with source | Never quote a number we cannot source |
| **8. Judge questions** | `JUDGE_QUESTIONS.md` with 30-second answers | Drill material; do not read from it live |
| **9. Bibliography** | Full verified bibliography, status-labelled | Proof of diligence |

---

## Print rules

- Tier 1: print the **annotation sheet** always; print the paper itself only if
  open access and if the figure/table matters.
- Tier 2: annotation sheet only.
- Tier 3: digital only — carry on a device with offline copies; assume no
  network at the venue.
- Every printed page carries the `paper_id` in the footer so it maps back to
  `literature/notes/`.
- Preprints are stamped **PREPRINT** on the sheet. Government reports are
  stamped **GOVERNMENT REPORT — NOT PEER REVIEWED**. If we are careless about
  this in the binder we will be careless about it out loud.

---

## Pre-fair rehearsal checklist

- [ ] Every Tier 1 paper read at evidence level E3 or better
- [ ] Every Tier 1 sheet answerable without looking at it
- [ ] Every judge question answered in ≤30 seconds, then a 2-minute version
- [ ] One person can find any tab in under 5 seconds
- [ ] The "what we do not claim" list can be recited from memory — this is what
      keeps us from over-claiming under pressure
- [ ] `bibliography/verify_dois.py` exits clean on the printed set
