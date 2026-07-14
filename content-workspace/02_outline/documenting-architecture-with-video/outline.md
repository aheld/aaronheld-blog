# Outline: Same Architecture, One Hour Each

**Content type**: tutorial / standard post (Pattern B). *Downgraded from Pattern C on 2026-07-13*: the "too long" instinct was right. The deep-dive version was doing double duty (documenting the harvester AND comparing the media). The linked doc and the video carry the system now; the article only argues the comparison.
**Word target**: 1000–1300
**Estimated drafting time**: ~1 hour

## What changed and why (2026-07-13)

- **Effort came in as a tie**: ~1 hour each. That collapses the old "The Bill" section (a table + caveats) into the *hook*. The surprising fact leads the piece.
- **The tie is conditional**, and the conditions are the best material: it only holds because the code was already documented, the Remotion framework existed, and the diagram framework existed. Plus a polish tax video pays and text never does. See `effort-log.md` "three layers."
- **Cut the full C4 walkthrough.** The old Section 2 re-explained containers/components the reader can see in the embedded diagram. Gone. One tight paragraph + the flow diagram.
- **Two real screenshots added** (`harvester-admin-queue.jpg`, `harvester-admin-diff.jpg`): they ground the abstract diagrams in the actual review UI, which is the human gate the whole piece hinges on.
- **Video is live**: https://youtu.be/j1sVF2LklaM

## Opening Hook (final, not draft)

I documented the same system two ways this month. A written architecture doc, four C4 diagrams and a few thousand words, and a five-minute animated video that explains the same pipeline. Each one took about an hour. That surprised me enough to make me distrust it, so this post is me pulling on the thread: an hour each is true, and it's true for reasons that don't transfer.

## Section Beats

### The system, in one breath
- Purpose: give the reader just enough of the harvester to make "it's a loop, not a pipe" land. Not the full C4 tour.
- Draws on: the one-paragraph statement + `harvestor-flow.svg`. Embed the flow diagram. Link the full written doc for anyone who wants the reference.
- Notes: end on the confession from the doc's own section 8: structure photographs well, the loop doesn't.

### What the page can't do, and the video can
- Purpose: the turn. The value is four mechanisms that are all *motion* (replay, review gate, sticky fields, quality score). A static diagram freezes the loop and asks the reader to animate it in their head. The video animates it for them.
- Draws on: the four mechanisms (compressed to a sentence each), the published video (embed here), the `harvester-admin-diff.jpg` screenshot showing a real pending diff (coords being ADDED) so the abstract "review gate" is concrete.
- Notes: name the anti-transience design honestly (recap poster frame, chapters, doc linked as the dwell companion) so the Tversky critique is answered in the open, not dodged.

### The hour-each is real, and it's a trap
- Purpose: the honest center. The three-layer cost story.
- Draws on: `effort-log.md` three layers. Marginal tie (conditional on prior investment), cold-start (not a tie, first Remotion videos took days), polish tax (a day or two, every time, never amortizes; deliberately unpaid here).
- Notes: this is where the `harvester-admin-queue.jpg` screenshot can sit, as the "here's the real tool; the video is a good-enough draft, not creator-polished" beat. The contrarian view's "most favorable accounting" critique gets conceded right here.

### Did the motion actually teach, or did I just enjoy making it
- Purpose: effectiveness, confounds confessed first. I'm the worst judge; the video went second. Then Tversky (motion is transient, the reader loses control) vs. Mayer (narration synced to the exact arrow). Concede docs-as-code: the written doc stays canonical, versioned, greppable; the video is a bootstrap with an expiration date.
- Draws on: `contrarian-view.md`. Naive reader/viewer data if it arrives; otherwise say plainly this half is observational.
- Notes: the attention counterpoint is the video's real win: a complete doc nobody finishes teaches nothing.

### When each earns its hour
- Purpose: land the narrow claim. Video pays off only when the pipeline is already amortized AND the behavior is dynamic AND the audience is wide/recurring AND the thing is stable enough to outlive the render (so the polish tax is worth paying). Otherwise: write the diagram, keep it in git.
- Draws on: contrarian §4–5.
- Notes: conditions, not commandments. Comfortable telling most readers not to make the video.

## Closing (final, not draft)

I'll keep writing the diagram first, every time. It's where the thinking happens and it's the only version I trust to stay true as the code moves under it. The video is the thing I make when the diagram is done and I can see people's eyes slide off the part that matters, the part that moves. An hour each was a gift of a lot of prior work, and I don't expect the gift twice. Go look at the last architecture doc you shipped. Does anything in it change state over time? If it does, every reader is animating that loop in their head right now, each one a little differently, and you're the only one who can run it for them once, correctly.

## Contrarian View Placement

"Did the motion actually teach" carries the engagement (confounds, Tversky, docs-as-code). "The hour-each is real, and it's a trap" concedes the most-favorable-accounting critique. "When each earns its hour" narrows the claim so it's defensible.

## Signature Moves Used

- **Concrete-scene opener**: documenting the same system twice and distrusting the tie.
- **Contrarian acknowledgment**: confounds and Tversky named before any effectiveness claim; the cost tie's conditions conceded.
- **Personal-then-systemic**: my two artifacts → when any team should reach for which → back to the reader's own doc.

## Companion artifacts

- Video (live): https://youtu.be/j1sVF2LklaM
- `03_draft/.../effort-log.md`: the three-layer cost story.
- `03_draft/.../harvester-admin-queue.jpg`, `harvester-admin-diff.jpg`: real review UI.
