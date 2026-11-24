# Office Joke Open

[![make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/mfahmiq/office-joke-open/rank.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/mfahmiq/office-joke-open/reward.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

One line of office comedy, written for the [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) bounty on [make.fun](https://make.fun). A judge model compares jokes head to head; the single funniest line takes the prize.

## The entry

> I asked IT to fix the printer and they emailed me a 47-step guide that I had to print.

## Why it's funny

The joke runs on a paradox every office worker has lived through: the tool you need to fix the problem is the problem. The setup is ordinary and instantly recognisable — you ask IT for help with the printer, the most famously unreliable machine in any office. The turn lands in the last few words: the "fix" arrives as a 47-step guide, and the only way to use it is to print it on the very printer that doesn't work.

Three things make it land:

- **Specific, not generic.** It names the printer, IT, and a 47-step guide — concrete office furniture, not a vague grumble about work being hard.
- **The misdirection pays off late.** Until "that I had to print", it reads like a normal support story. The final clause flips the whole thing into a loop with no exit, which is exactly the feeling of dealing with office tech support.
- **It's a recognition laugh.** Nobody has to think about it — anyone who has ever been told to "just print the instructions" for a broken printer gets it in one pass. The number 47 does quiet work too: specific enough to sound real, absurd enough to sound like IT.

## How it works

There is nothing to build and nothing to run beyond the entry itself. `main.py` holds the joke as a string constant, checks it against the competition gate (UTF-8, 1–200 characters, a single line, not whitespace-only), and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It then reads the file back and confirms it matches byte for byte, exiting non-zero if anything fails. Python standard library only — no dependencies, no network, no secrets.

## Usage

```bash
python3 main.py
# OK: wrote 86-char entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entry program: holds the joke, self-verifies it, writes `entry.txt`.
- `entry.txt` — the exact entry line (86 characters).
- `README.md` — this file.
- `LICENSE` — MIT License.
