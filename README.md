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

https://psytzou.github.io/birthday-tea-party/

## Supplementary material: running 进阶模式 locally
1. [Download the project](https://github.com/psytzou/birthday-tea-party/archive/refs/heads/main.zip) and unzip it.
2. Double-click **`start.bat`** (Windows) or **`start.command`** (Mac). The page opens in your browser.
3. In Section 6, click **进阶模式**, then **Connect** if it does not connect by itself.

Requires Python 3 and [Claude Code](https://claude.com/claude-code). The copy bundled with the Claude desktop app works too, but it must be signed in once on its own: double-click **`login.bat`** (Windows) or **`login.command`** (Mac), type `/login`, finish in the browser, then type `/exit`. On a Mac, if the first double-click is blocked, right-click `start.command` and choose **Open**.

| Method | HeroineBench-24 ↑ | Route Regret ↓ |
|---|---:|---:|
| GRPO | 71.4 | 298.4 |
| **LHPO (ours)** | **93.0** | **24.0** |



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
