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

## 进阶模式 setup (local Claude, no API key)

Requirements: Python 3.8+ and [Claude Code](https://claude.com/claude-code) installed and signed in.

1. Download [`bridge.py`](bridge.py) (or clone this repo).
2. Run it and keep the window open:
   ```bash
   python bridge.py
   ```
3. Open the paper, go to Section 6 and click **进阶模式**. It connects automatically.

The bridge listens only on `127.0.0.1:8765`, accepts requests only from this page, and runs Claude Code in an empty temporary folder with one turn per message. Use Chrome or Edge; if the browser asks whether the page may access devices on your local network, allow it.

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
