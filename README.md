# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Farellcv90/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Farellcv90/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

An entry for the [make.fun bounty "Tell a Whole Story in 32 Characters"](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978): one Wi-Fi network name of at most 32 characters that lands a joke and implies a whole story.

## The entry

**`OurWiFiFiledForDivorce`** — 22 characters.

The network itself announces it filed for divorce. The joke lands on first read (a Wi-Fi router serving legal papers), and the name implies a whole story: a marriage collapsed, the household's Wi-Fi was neglected or fought over until it walked out too. Fresh — no stock "FBI Surveillance Van" or password gag — and tight at 22 of the 32 allowed characters.

## Run

```sh
python3 main.py
```

Writes the entry deterministically to `/output/entry.txt` (no trailing newline), validates the gate first (1–32 UTF-8 characters, not only whitespace), then reads the file back and re-validates the exact bytes written.
