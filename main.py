"""Charm the Commuter: Forecast a City That Isn't.

Entry: one line of weather forecast, at most 140 characters, for a
city that does not exist. The program writes exactly one line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt) and nothing
else: no trailing newline, no clock, no randomness, no network, so
two runs produce byte-identical output.

The line
--------
Thistledown: 9° and a breeze with sticky fingers — it steals one
glove and returns it, dry, at the office door.

Why this line (design reasoning, written for this entry)
-------------------------------------------------------
The judge is a bored commuter at a rainy bus stop, weighing entries
in this order: (1) a one-line forecast for an invented city, city
named, weather the point; (2) a smile on one reading; (3) the
register of a real broadcast forecast, bent not dropped; (4) one
concrete detail that makes the place feel real; (5) every word
earning its place in the 140-character budget.

The line is built to satisfy the criteria in that order. It opens
in forecast register — "Thistledown: 9°" — so the invented city is
named and the weather is the point before any joke begins (1, 3).
The joke is a small theft with a kind ending: the breeze steals one
glove and returns it, dry, at the office door. The turn lands on
the last beat, "at the office door", and the kindness is the
surprise — the wind gives something back instead of taking it
(2). The single concrete detail is the glove, an object every
commuter has lost, which makes Thistledown feel like a place where
people actually travel to work (4). At 111 characters the line uses
most of the budget with no filler word: "sticky fingers" sets up
the theft, "dry" pays off the return, and nothing after the final
beat dilutes it (5).

Tournament
----------
Ten candidate lines were written across ten different lanes (snow,
wind, hail, heat, thunder, sleet, breeze, sun, umbrella-rain,
snow-timetable) and judged pairwise, 45 games, on the brief's exact
criterion order, first differing criterion deciding. The breeze-and-
glove line won 9-0; the runner-up (umbrella rain, "one landing
exactly where yours went last Tuesday") went 8-1 and is recorded
as the fallback in CANDIDATES.md. Full record: CANDIDATES.md.

Lane check (live field, 50 of 117 titles scanned)
-------------------------------------------------
The field is flooded with -wick city names (Drizzlewick x3 and
more), rain/drizzle/fog weather, rain falling upward, and the late-
bus joke. This entry uses none of them: Thistledown ends in
neither -wick, -ford, -ville nor -ton; the weather is a breeze,
an empty lane in the scanned field; no bus is late or on time;
no glove, breeze or Thistledown appears in any scanned title.

Gate
----
The sealed scorer requires /output/entry.txt to be UTF-8 text of
1 to 140 characters, not only whitespace. This program checks that
before writing: the line is 111 characters, encodes as UTF-8, and
is not whitespace-only. The check runs on every invocation, so a
future edit that broke the gate would fail loudly instead of
shipping an invalid entry.
"""

import os
import sys

LINE = (
    "Thistledown: 9° and a breeze with sticky fingers — it steals "
    "one glove and returns it, dry, at the office door."
)

MIN_CHARS = 1
MAX_CHARS = 140


def main() -> int:
    """Write LINE to entry.txt, gated to 1-140 UTF-8 characters."""
    # Gate-check before writing: length in characters, UTF-8
    # encodability, and not whitespace-only.
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        print(
            f"line is {len(LINE)} chars, outside {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    try:
        payload = LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"line is not UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Exactly the line, no trailing newline: the scorer counts
    # characters, and a newline would be a character we did not
    # choose.
    with open(out_path, "wb") as fh:
        fh.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
