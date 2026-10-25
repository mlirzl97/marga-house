# Instructions for AI assistants (ChatGPT/Codex and Claude)

Both assistants work on this repo for the owner. The owner relays between them; neither is notified of the other's changes, so always pull before working.

1. Before any design work, read `BRIEF.md`, `DECISIONS.md`, `MEASUREMENTS.md` and `plan/README.md`.
2. Never redraw the floor plan from scratch. Layout changes go through the code in `plan/`. Do not change the coordinates listed in `plan/README.md` unless a measurement in `MEASUREMENTS.md` changes.
3. New design steps go in new files (e.g. `plan/step2_layout.py`), built by copying `plan/base_plan.py`.
4. Work on a branch with a clear name and commit message. Merge to `main` only after the owner approves.
5. When the owner settles something in chat, add it to `DECISIONS.md` with the date.
6. Keep the exact block and lot number out of all files.
7. Renders go in `renders/` only after the matching plan is approved, labeled "illustrative".
