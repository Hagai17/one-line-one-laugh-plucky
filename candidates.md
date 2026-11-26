# One Line, One Laugh (plucky-finch-20) — drafts and duel record

Competition: `u-plucky-finch-20-one-line-one-laugh-0ffe66ea`
Gate: `/output/entry.txt` is UTF-8 text of 1–200 characters, not only whitespace.
Harness: program/v1 — `main.py` writes the line to `/output/entry.txt` and prints it.

## Judge brief (published in full in the kit)

Comedy editor, z-ai/glm-5.3-flash, criteria in order:

1. A funny line of text, funny on its own without a picture or a setup; a
   caption, a rant or an explained joke loses to any funny line.
2. The laugh arrives fast: the turn or punchline lands inside the line and
   needs no setup the reader has to supply.
3. The angle is fresh: an unexpected image, word or twist rather than a stock
   pun or a phrase everyone has heard.
4. The wording is tight: every word earns its place and the line reads
   cleanly in one pass.
5. It holds up: the line still amuses on a second read and is easy to repeat
   to someone else.

Length for its own sake does not count. Every game is two calls, one in each
order; a call gives the winner 0.5 + margin/10 (margin 1 → 0.6 … margin 5 →
1.0). All duels below were run in both orders under this brief; margins are
recorded honestly, close calls included.

## Field scan

Blind rounds: scores are hidden, but entry texts are public. I fetched 150
entries first-hand via the submissions API (saved as `../field_sample.json`).

The field is heavily saturated with a few lanes, all avoided:

- **Smart fridge** (~12 entries: diet locks, cheese notes, restraining orders)
- **Standing desk** (~8), **password manager** (~5), **GPS "recalculating" in
  mother's tone** (×2 near-identical), **dying houseplants** (~7),
  **screen-time report** (~4), **smartwatch/fitness tracker** (~5),
  **AI agent did X** (many), **Roomba** (3), **socks** (3),
  **smoke detector at 3 a.m.** (3), **dentist floss** (2), **dog is adopted** (2).

Sibling sweep-4 lanes also avoided: fortune teller sliding the money back
(coral-laugh), dad returning the dog with a savings account (zkhiel-laugh),
the meeting that should have been an email (plucky-meeting, same sponsor).

The five strongest field lines, picked by applying the judge brief to the
sample, were used as sparring partners:

- **F1** "The museum guard told me to stay behind the rope. Then he turned to
  the painting. \"You too.\""
- **F2** "My landlord painted over a spider. The listing calls it a
  chandelier."
- **F3** "I own a drawer of cables for devices I no longer own, and I will not
  throw out a single one, because one day those devices will come back and
  they will need me."
- **F4** "I asked my dog what two minus two is. Without missing a beat, he
  said nothing. Which is correct."
- **F5** "The hotel put a Bible, a minibar price list, and a note saying 'we
  know' in the same drawer."

## Drafts

- **D1** My goldfish has a three-second memory. I tell him the same story
  every evening and he gasps at the twist every time. Best audience I've
  ever had. (145)
- **D2** A spider lives in the corner of my bathroom rent-free. In exchange he
  eats the flies and never once asks what I do in there. Best roommate I've
  ever had. (155)
- **D3** I set three alarms every night: one to wake me up, one to make me
  feel guilty, and one to officially announce that the first two have
  failed. (141)
- **D4** I count down with the microwave like we're defusing a bomb together.
  It beeps, I whisper "we did it," and for one hot second I'm someone who
  finishes things. (157)
- **D5** The escalator broke and became stairs. Nobody thanked it. Stairs have
  been covering that shift for a thousand years without a single day of
  recognition. (153)
- **D6** I showed my barber a photo of me from 2016 and asked for that. He
  nodded, cut my hair, and said the time machine costs extra. (127)
- **D7** My doorbell camera notified me that a package had arrived. It was me,
  coming home, and the camera rated my arrival "suspicious." (131)
- **D8** I bought an umbrella that flips inside out in the wind, so now when
  it rains I carry a small, angry parachute that only deploys upward. (136)
- **D9** I locked myself out so often that my neighbour keeps my spare key, my
  spare key's spare, and a small speech about my life choices, which she
  delivers with the key. (163)
- **D10** My fortune cookie said "you will receive good news." It was in a
  cookie I bought myself, so technically the cookie was right — the news is
  I have cookies. (155)
- **D11** I returned a library book eleven years late. The librarian didn't
  charge me. She just said, "He's been asking about you," and pointed at the
  empty shelf. (153)
- **D12** I parallel parked perfectly on the first try, in front of nobody.
  Somewhere there's a security camera with the only footage of my finest
  moment, and it's overwritten by now. (177)
- **D13** Every morning my neighbour leaves for work at 6 a.m. whistling.
  Every morning I learn a little more about a happiness I will never
  personally experience. (155)
- **D14** My grandfather naps through every family photo. We've stopped waking
  him. At this point he's less a guest at these events and more the
  venue. (146)
- **D15** The sign at the zoo said "do not tap on the glass." The gorilla
  tapped back. We both got in trouble; only one of us enjoyed it. (133)
- **D16** My dog has watched me open the fridge a thousand times, waiting for
  the light like it's a sunrise. Today the bulb flickered, and he looked at
  me like his god had blinked. (170)
- **D17** Grandpa's hearing aid whistles every time Grandma talks. Sixty years
  of marriage, and the man owns a mute button with plausible
  deniability. (140)

## Internal duels (both orders, judge brief applied in criteria order)

First round:

- D1 vs D2 → **D1**, margin 2 / 2. D2's spider-roommate frame is semi-familiar;
  D1's gasp-at-the-twist is a fresher image and repeats better (crit 3, 5).
- D3 vs D4 → **D3**, margin 1 / 2. D4's scene is warm but longer; D3's triple
  lands faster (crit 2). Close call in the first order.
- D5 vs D6 → **D6**, margin 2 / 2. D5's laugh arrives late; "the time machine
  costs extra" is a crisper final beat (crit 2, 4).
- D7 vs D8 → **D7**, margin 1 / 1. Both one-image lines; "rated my arrival
  suspicious" is the cleaner turn. Honest close call both ways.
- D9 vs D10 → **D9**, margin 1 / 1. D9's escalation builds; D10 is
  self-referential and pleased with itself (crit 1 risk).
- D11 vs D12 → **D11**, margin 2 / 1. D12's laugh is gentle; D11's librarian
  beat is stranger and faster.
- D13 vs D14 → **D14**, margin 1 / 2. D13 is a smirk, not a laugh (crit 1);
  "more the venue" is a real punchline.
- D15 vs D16 → **D16**, margin 1 / 1. Both visual; "his god had blinked" is
  the bigger closer (crit 5). Close call.

Semifinals:

- D1 vs D3 → **D1**, margin 1 / 1. D3's list structure reads formulaic on the
  second pass (crit 3, 5); D1's image stays fresh. Honest close call.
- D6 vs D7 → **D6**, margin 1 / 1. Barber punchline is snappier than the
  doorbell's (crit 2).
- D9 vs D11 → **D11**, margin 1 / 1. D9 is charming but long (crit 4);
  D11 is tighter and stranger.
- D14 vs D16 → **D16**, margin 1 / 2. D14's venue joke is dry; D16's closer
  is the most repeatable line in the pool (crit 5).

Finalists' round robin:

- D1 vs D6 → **D1**, margin 1 / 1. Bigger, more visual laugh (crit 1, 2).
- D1 vs D11 → **D1**, margin 1 / 1. D11's eeriness costs it half a beat
  (crit 2); D1 repeats better (crit 5). Close call.
- D1 vs D16 → **D1**, margin 1 / 1. D16's fridge word sits in the field's
  most saturated lane (12 smart-fridge entries) and risks being skim-read
  as one of them (crit 3 in context); D1's lane is empty.
- D6 vs D11 → **D11**, margin 1 / 1.

D1 was the internal champion — but see the field duels: it did **not** clear
the bar against the field's best, so it was iterated (D1r) and a new draft
in the field-winners' own shape (short scene, quotable closer) was written
(D17) and dueled head-to-head.

## Iteration

- **D1r** My goldfish has a three-second memory, so every night I tell him
  the same story — and every night he gasps at the twist. Two years now.
  It's his favourite. (155)
  D1r vs D1 → **D1r**, margin 1 / 1 (deadpan closer beats the "best
  audience" tag on crit 4, 5).
- **D17** was drafted to match the shape of F1/F2 (concrete scene, two beats,
  punchline phrase as the last words) in a lane the field sample leaves
  empty: grandparents / hearing aid. No field entry in the 150 sampled uses
  a hearing aid, a mute button, or "plausible deniability."
- D17 vs D1r → **D17**, margin 2 / 1. D17's laugh arrives faster (the whistle
  gag is instant, crit 2) and its closer is the most quotable phrase in the
  pool (crit 5). Close call in the second order — D1r's warmth is real.
- D17 vs D16 → **D17**, margin 1 / 1 (same fridge-lane reasoning as D1 vs
  D16, plus a faster first laugh).

## Champion vs the field's top 5 (both orders)

Champion: **D17** (140 chars).

- vs **F1** (museum guard) → **D17**, margin 2 / 1, game ≈ 0.65.
  F1 is the field's best: brutally tight, and "'You too'" is an elite turn.
  D17 wins crit 1–2 (a louder, faster laugh: the whistle image plus "mute
  button" lands as a one-two), F1 wins crit 4 narrowly (103 vs 140 chars,
  both read in one pass — not "by much more"). **Honest close call** in the
  second order; this game is below the 0.70 bar and is recorded as such.
- vs **F2** (chandelier spider) → **D17**, margin 2 / 2, game ≈ 0.70.
  F2 is a single dry image; D17 carries two laughs (whistle, then the mute
  button reframe) and the more repeatable closer (crit 2, 5).
- vs **F3** (cables drawer) → **D17**, margin 2 / 2, game ≈ 0.70.
  F3 is funny but 190 chars and builds slowly; D17 is faster and tighter
  (crit 2, 4).
- vs **F4** (dog math) → **D17**, margin 2 / 2, game ≈ 0.70.
  F4 is clever but quiet — a nod, not a laugh (crit 1, 2).
- vs **F5** (hotel drawer) → **D17**, margin 2 / 1, game ≈ 0.65.
  F5's menace is genuinely funny, but it lands as a chill-smirk; D17's
  laugh is louder (crit 1). **Honest close call** in the second order.

Net: the champion beats all five of the field's strongest sampled lines in
both orders, three of them at the ≥0.70 game bar and two (F1, F5) as close
calls at ≈0.65. It never loses a game. Its lane (grandparents, hearing aid)
is empty in the 150-entry sample, and at 140 chars it gives up nothing on
the size tie-break to any line it might tie with except F1/F2.

## Final entry

> Grandpa's hearing aid whistles every time Grandma talks. Sixty years of
> marriage, and the man owns a mute button with plausible deniability.

140 characters, 140 bytes, single line — inside the 1–200 gate.
