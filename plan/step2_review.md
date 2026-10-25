# Step 2 — furniture and electrical proposal

2026-10-25. **For owner approval; not an approved layout or construction electrical plan.**

Built by copying `base_plan.py` and adding overlays in `step2_layout.py`. All original walls, windows, openings, doors, sliders, plumbing markers, counter, sink, canopy, privacy wall, planting bed, car and step remain at their original coordinates. No measurements or settled decisions were changed. The existing decisions already include the 55-inch TV and minimum 8 cm bunk clearance.

Run `python3 plan/step2_layout.py` with matplotlib installed. It writes:

- `plan/step2_layout.png` — furniture and clearances.
- `plan/step2_electrical.png` — electrical point IDs over the same layout.

Run `python3 -m unittest discover -s plan -p 'test_*.py'` for the geometry regression check. It executes both scripts in a temporary directory and compares every original patch and line, without overwriting the committed base PNG.

## Furniture and fit

All coordinates below are proposed bounding boxes in metres, from their lower-left corner. Dimensions in furniture labels are centimetres. Wall faces, rather than centerlines, control the fit. New items are proposals, not additions to settled decisions.

| Item | x, y | Width × depth in plan | Fit / use |
|---|---|---|---|
| BR1 queen / flush platform | 0.115, 4.825 | 1.90 × 1.52 | Mattress 152 × 190, head to left. Separate 4 cm headboard at x 0.075. No protruding platform lip. 75.5 cm access on the hall side; 63.5 cm at foot. Drawer fronts open toward the 75.5 cm side. |
| BR2 bunk outer frame | 0.075, 8.675 | 1.50 × 2.00 | Upper double 137 × 190; lower single 91 × 190. 12.5 cm between frame and inside face of door wall. **min 8 cm clear between bunk and door wall for sliding panel**. |
| Bunk ladder reservation | 1.575, 9.10 | 0.35 × 0.45 | Leaves 72.5 cm to opposite wall; frame, ladder, guardrails and ceiling height need fabrication verification. Do not widen into circulation. |
| Locked owner cabinet | 2.35, 9.90 | 0.30 × 0.70 | Right BR2 wall, 77.5 cm approach from bunk; sliding fronts proposed. Shelf capacity to suit personal items, not a full wardrobe. |
| Sofa | 2.75, 4.75 | 0.78 × 1.70 | Left Living wall. Owner photo gallery above; no central coffee table. Small 35 × 30 side table at (2.75, 6.55). |
| TV | right-wall face x 4.825; y 5.00–6.23 | 1.23 long on wall; 0.71 high | 55-inch screen, center 100–110 cm above floor; recess 8–10 cm. Estimated seated eye x 3.20 gives 1.625 m to screen. Confirm TV depth, bracket and ventilation before cabinetry. |
| Dining table | 4.275, 7.15 | 0.55 × 1.20 | Fold-down table; **two seats at a time**. Two 50 × 45 chairs face right. Route remains 77.5 cm after allowing 20 cm extra chair pullback. Fold/store chairs when table is closed. Five guests eat in shifts; not represented as a five-seat table. |
| Compact fridge + microwave above | 4.225, 8.95 | 0.60 × 0.60 | Cabinet bay opens toward left. Reserve 75 cm for approach; rear-door swing remains free. Microwave on a ventilated shelf above a low fridge, not on the 100 cm sink counter. Appliance sizes must fit this envelope with manufacturer ventilation allowances. |
| Counter appliances | water at (2.78, 10.15), kettle at (3.08, 10.15) | 0.28 × 0.30; 0.18 × 0.22 | Compact tabletop dispenser and kettle use the existing counter's narrow left segment. Existing sink stays unchanged. Only limited landing space remains; use the dining table for breakfast preparation. Dishes for five in sealed undercounter storage. |
| T&B toilet | 0.96, 7.20 | 0.38 × 0.68 | Full-size fixture envelope, existing outlet at (1.15, 7.55). 57 cm clear in front meets the 55 cm toilet-front requirement, but does **not** meet the separate 60 cm walkway rule. Select a compatible rough-in; no outlet relocation assumed. |
| T&B basin + cabinet | 0.15, 7.20 | 0.50 × 0.30 | Slim, moisture-resistant cabinet; connections from existing front-wall stubs. |
| Shower zone | 0.075, 7.65 | 0.80 × 0.80 | Rain shower at existing rear-left drain zone. **Open wet-room proposal**, pending owner approval; no fixed glass panel is drawn as approved. |
| Shoe bench | 3.80, 3.20 | 1.00 × 0.35 | Behind privacy wall and under existing canopy, outside front-door swing. |
| Three outdoor AC units | x 0.15 / 1.10 / 2.05; y 10.90 | each 0.75 × 0.30 reserved | Wall-mounted service-area reservations only. Verify actual units, service/airflow clearances and tank/drying arrangement; rear-door approach remains free. |

The right-wall cladding is shown with a conservative continuous 10 cm inward build-up from the inside wall face x = 4.925. The usable face is x = 4.825. The fridge projects further into the room; a 60 cm fridge is not hidden inside a 10 cm wall build-up. Cladding remains plywood on battens with an air gap; keep aligned joints at the TV, fridge bay and door heads.

## Items for owner review

1. **Bathroom circulation and glass — unresolved fit:** the 57 cm strip in front of the toilet is also the route to the shower; its usable overlap with the fixed doorway is only 54 cm (y = 7.88–8.42). This is below the brief's 60 cm circulation rule. **The bathroom is not shown as a compliant fit**; this needs a further fixture-layout study or explicit owner acceptance of the shortfall before approval. The full-size 38 × 68 cm toilet and all base coordinates remain unchanged. **Glass:** a full-depth side divider beside the shower would block the entry route from the fixed hall opening, given the full-size toilet at the existing outlet. Closest workable proposal here is an open wet zone with a retractable curtain. A glass solution needs a separate fit study; no plumbing point was moved to make one appear to fit. Glass remains the owner's preference, not an approved deletion from `DECISIONS.md`.
2. **Dining:** two simultaneous diners, with staggered use for larger parties. No miniature furniture or obstructed hall was used to claim seating for five.
3. **BR1 storage:** platform drawers and high hooks; the optional 30 cm cabinet is omitted because it would reduce the 63.5 cm foot route below 60 cm. Locked owner storage is in BR2 instead.
4. **Bunk fabrication:** the specified height stack totals 250 cm inside an estimated 260 cm ceiling, leaving 10 cm tolerance. Verify actual ceiling, structural frame, guardrails and ladder before fabrication. Retain full-size mattresses and the minimum 8 cm panel allowance.

Owner mode: unlock the cabinet and put out personal belongings/curated lamps. Guest mode: lock personal items away, clear surfaces and retain the photo gallery. Neither mode requires moving large furniture.

## Electrical points

Coordinates are point locations in the drawing, not cable routes. Heights below are proposals above finished floor (AFF), to be checked against actual equipment, window/door heads and the measured ceiling. Keep switches and outlets outside moving slider envelopes. Use one 3000 K light temperature throughout; make task, ambient and photo lighting separately switchable. The exact block and lot numbers are intentionally absent.

| ID | Drawing point (x, y) | Proposed function / height |
|---|---|---|
| A1 | 2.65, 6.15 | BR1 split AC; high on shared wall, unit top to manufacturer ceiling clearance. Dedicated AC circuit 1. |
| A2 | 2.65, 10.15 | BR2 split AC; high on right wall above cabinet zone, independent of cabinet ventilation. Dedicated AC circuit 2. |
| A3 | 2.75, 4.35 | Living split AC on stepped/shared wall; verify clear wall length, pipe path and airflow. Dedicated AC circuit 3. |
| H1 | 0.12, 8.30 | Water heater feed high in shower zone, dedicated circuit and appropriately protected supply. Isolator outside wet area; final type/location by installer. |
| U1 | 0.12, 6.24 | BR1 headboard USB + socket, 65–75 cm AFF on accessible side. |
| U2 | 0.12, 10.45 | BR2 upper-bunk USB, about 175 cm AFF, set by final mattress elevation. |
| U3 | 0.12, 10.15 | BR2 lower-bunk USB + socket, about 65–75 cm AFF. Keep fixed wiring and loose cords away from ladder/guardrails. |
| P1 | 4.87, 5.62 | TV and router recess: sockets + data, around 100–110 cm AFF, accessible service panel and ventilated router shelf. |
| P2 | 4.87, 9.25 | Fridge and microwave bay; separate accessible sockets set to actual shelf heights, outside fridge heat/ventilation path. Final grouping/load check needed. |
| P3 | 3.10, 10.67 | Counter appliance sockets above counter, with suitable sink separation/protection. Position must be checked against existing rear window; use underside/side service strip if rear wall space is insufficient. |
| P4 | 4.87, 7.75 | Dining/laptop outlet above fold-down tabletop, about 95–105 cm AFF. |
| P5 | 2.75, 6.70 | Living side-table/general outlet, about 30 cm AFF. |
| P6 | 4.65, 3.70 | Weather-protected outdoor outlet on Living front wall facing court, about 110 cm AFF. |
| C1 | 4.95, 3.75 | Exterior front-corner CCTV; concealed PoE/data feed from P1 router, camera mounted beneath canopy. Frame entrance/car within property. |
| K1 | 3.60, 3.75 | Smart-lock location at front door; concealed front-entry low-voltage provision. Confirm chosen lock's power method; do not assume mains-compatible lock hardware. |
| G1 | 0.075, 5.62 | BR1 headboard photo-wall wash; height set to art/rail, clear of AC and curtains. Picture-light circuit. |
| G2 | 2.75, 5.62 | Sofa photo-wall wash; same art/rail system and picture-light circuit. |
| L1 | 1.35, 6.75 | BR1 ceiling ambient light over access side. |
| L2 | 2.05, 9.60 | BR2 ceiling ambient light over clear aisle. |
| L3 | 3.85, 5.60 | Living ceiling ambient light. |
| L4 | 3.70, 8.00 | Dining ceiling light, with task illumination toward table. |
| L5 | 1.05, 8.10 | Bathroom ceiling light, wet-area appropriate. |
| L6 | 2.20, 7.80 | Hall ceiling light. |
| L7 | 4.15, 3.20 | Covered entry ceiling light under canopy. |
| L8 | 4.20, 11.15 | Rear exterior light, mounted to wall/bracket above service area. |
| L9 | 3.05, 10.15 | Ceiling task light aimed at counter; no new cabinet across rear window. |
| S1 | 3.80, 3.80 | Entry switch group, approximately 110 cm AFF: Living, entry and photo lights. |
| S2 | 2.60, 6.85 | BR1 switch group on right wall, outside slider travel: ambient and headboard/photo light. |
| S3 | 2.60, 8.85 | BR2 switch on right wall, outside slider travel. |
| S4 | 1.70, 8.48 | Hall-facing solid wall segment beside BR2 opening: hall/bath light group and heater isolation provision outside wet area. Check actual jamb and plate space. |
| S5 | 4.87, 9.65 | Kitchen/rear switch group, beyond fridge envelope: dining, counter task and rear light. |

**Panel inspection is outstanding.** Its location, main rating, free slots, earthing and service capacity are unknown. Reserve three dedicated AC circuits and one dedicated heater circuit plus provision for appliance, general/outdoor, lighting and picture-light groups. No conductor sizes, breaker ratings, panel location, concealed routes, or upgrade decision are invented. A panel upgrade may be needed if capacity or slots are insufficient; the photo/nameplate and connected-load check determine this. CCTV uses PoE and the smart lock uses its selected low-voltage/battery system, not an assumed shared mains circuit.

## Approval boundary

Only this proposal branch is to be pushed. No merge to `main`, no changes to the controlling base plan, no renders, pricing list or procurement. Resolve the owner-review items before treating this layout as approved.
