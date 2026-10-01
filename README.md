<div align="center">

# Losing Heroines Are All You Need

### Regret-Optimal Preference Alignment under Non-Stationary Affection

**Anon Chihaya** · Haneoka Girls’ High School · MyGO!!!!!

*Dedicated to Zeru “Bianbian” on his 24th birthday.*

![arXiv](https://img.shields.io/badge/arXiv-2609.30024-b31b1b)
![Venue](https://img.shields.io/badge/Birthday%20Track-Accepted%20(Oral)-c4302b)
![Regret](https://img.shields.io/badge/Regret-O(%E2%88%9AT%20log%20K)%20%2B%2024-4f74a8)
![Heroines](https://img.shields.io/badge/losing%20heroines-never%20forgotten-6b5a8e)

</div>

---

## TL;DR

Preference optimization collapses onto one mode and forgets everyone else. We call the forgotten modes **losing heroines**, add a log-barrier that keeps them alive (**LHPO**), and prove a regret bound whose additive constant is exactly **24**. The bound is tight on birthdays.

## How to read the paper

**Option 1 (recommended):** open the GitHub Pages link for this repo.

**Option 2:** clone and open locally.

```bash
git clone <this-repo-url>
```

Then open `index.html` in any browser. An internet connection is needed for fonts and math rendering.

## Reproducing the results

1. Read the paper.
2. Complete **at least 3 rounds** of the interactive human evaluation in Section 6. You can talk to each reference heroine alone, or open **☕ 败犬茶话会** to talk to all three at once.
   - **标准模式** works out of the box, using pre-written lines (`lines.js`).
   - **进阶模式** lets you chat freely with your own Anthropic API key. The key stays in your browser and is sent only to `api.anthropic.com`.
3. Wait for Reviewer #2 (Kazusa Touma).
4. Click the final decision. Turn your sound on.

| Method | HeroineBench-24 ↑ | Route Regret ↓ |
|---|---:|---:|
| GRPO | 71.4 | 298.4 |
| **LHPO (ours)** | **93.0** | **24.0** |

## Citation

```bibtex
@article{chihaya2026losing,
  title   = {Losing Heroines Are All You Need: Regret-Optimal Preference
             Alignment under Non-Stationary Affection},
  author  = {Chihaya, Anon},
  journal = {Birthday Track},
  year    = {2026},
  note    = {Dedicated to Zeru on his 24th birthday}
}
```

## Credits

- Characters belong to their original creators: *Saekano* (Fumiaki Maruto / Kurehito Misaki), *White Album 2* (Leaf / Aquaplus), *Monogatari* (NisiOisin / VOFAN), *BanG Dream! It's MyGO!!!!!* (Bushiroad).
- Illustrations are fan art from pixiv, used for a personal, non-commercial birthday gift:
  - Eriri: https://www.pixiv.net/artworks/149361125
  - Setsuna: https://www.pixiv.net/artworks/149341177
  - Tsubasa Hanekawa: https://www.pixiv.net/artworks/150063807
  - Anon Chihaya: https://www.pixiv.net/artworks/113069520
- All dialogue, the paper and the data are original and entirely made up.

---

<div align="center"><i>— Anonymous Author (double-blind, name withheld)</i></div>
