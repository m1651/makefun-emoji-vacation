# One Emoji, One Dream Vacation

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/m1651/makefun-emoji-vacation/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/m1651/makefun-emoji-vacation/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for the make.fun bounty **One Emoji, One Dream Vacation**
(`u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35`, $2, winner takes all).

## The entry

🗻 — Mount Fuji.

One emoji, nothing else. A snow-capped mountain in Japan: a specific,
iconic dream trip, instantly readable as a postcard at any size, rather
than a generic beach or plane. It is a single Unicode code point
(U+1F5FB), so the entry is 1 character and 4 UTF-8 bytes — well inside
the gate of 1–8 characters.

## How it works

`main.py` (Python 3, standard library only, deterministic) writes the
chosen emoji to `/output/entry.txt`, then reads it back and validates
its own output:

- the file bytes are exactly the chosen emoji's UTF-8 encoding;
- the text is exactly 1 character (within the 1–8 character gate);
- it is not whitespace, not alphanumeric, and not ASCII — i.e. an emoji.

It exits non-zero if any check fails.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — entrypoint
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
