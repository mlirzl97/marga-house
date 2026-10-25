# plan/

Floor plan drawing code for the Marga unit. Edit this code for any layout change; never redraw the plan from scratch.

## Files
- `base_plan.py` → `marga_base_plan.png` — **the controlling base plan.** Walls, openings, doors, existing plumbing points, kitchen counter, canopy, privacy wall, parking. Unfurnished; T&B fixtures removed for redesign.
- `furnished_reference.py` → `marga_furnished_reference.png` — earlier furnished layout by Claude. **Reference for positions and orientation only** (door, counter, car, front step). Furniture and T&B fixtures here are superseded by the design process.

Run: `python3 plan/base_plan.py` (needs matplotlib). Output PNG is written next to the script.

## Coordinate system (metres)
- Origin (0,0) = front-left corner of the lot at the street. x → right, y → toward the rear.
- Lot 5.00 × 12.00 (assumed; width to be measured).
- Walls drawn on centerlines. Exterior 150 mm, interior 100 mm. Clear room sizes are ~10–15 cm smaller than centerline sizes.
- Left column x 0–2.70; right column x 2.70–5.00.
- Bedroom 1 front wall y = 4.75; Living front wall y = 3.75 (projects 1.00 m further).
- Bedroom 1 / T&B / Bedroom 2 boundaries: y = 7.15, 8.50. Rear wall y = 10.75.
- Hall alcove: x 1.60–2.70, y 7.15–8.50 (open to Dining at x = 2.70).
- Front door: x 2.85–3.65 on y = 3.75, swings OUT. Rear door: x 3.95–4.75 on y = 10.75, hinge at right.
- Bedroom doors: openings x 1.80–2.55 on y = 7.15 (BR1) and y = 8.50 (BR2); sliding panels inside each room over x 1.00–1.80.
- T&B door: opening y 7.75–8.42 on x = 1.60; 2-panel telescopic slider stacking on the hall side over y 7.20–7.75.
- Existing kitchen counter: x 2.76–3.76, y 10.07–10.67 (rear-left of Dining).
- Existing plumbing (T&B): floor drain ≈(0.45, 8.18); toilet outlet ≈(1.15, 7.55); water stubs on y = 7.15 wall at x ≈0.6–0.8.
- Canopy: stepped slab ≈0.6 m deep — over BR1 front (y 4.15–4.75, x 0–2.2), steps forward at x = 2.2 to y 3.15 over the entrance.
- Car (MG ZS 1.81 × 4.31): x 0.12–1.93, y 0.07–4.38, reversed in.
- Privacy wall: x 2.72–4.95, y 2.30–2.50; planting bed street-side.

Values marked ≈ or VERIFY in the drawing are estimates; see `MEASUREMENTS.md`.
