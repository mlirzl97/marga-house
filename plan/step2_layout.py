import os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, FancyBboxPatch, Ellipse, Circle
T=0.15; t=0.10
fig,ax=plt.subplots(figsize=(8.5,14)); ax.set_aspect('equal'); ax.axis('off')
ax.set_xlim(-1.9,6.9); ax.set_ylim(-2.2,14.2)
K='#222'
def wall(x1,y1,x2,y2,th=T,c=K):
    if y1==y2: ax.add_patch(Rectangle((min(x1,x2)-th/2,y1-th/2),abs(x2-x1)+th,th,color=c,zorder=3))
    else: ax.add_patch(Rectangle((x1-th/2,min(y1,y2)-th/2),th,abs(y2-y1)+th,color=c,zorder=3))
def gap(x1,y1,x2,y2,th=T):
    th+=0.04
    if y1==y2: ax.add_patch(Rectangle((x1,y1-th/2),x2-x1,th,color='white',zorder=4))
    else: ax.add_patch(Rectangle((x1-th/2,y1),th,y2-y1,color='white',zorder=4))
def window(x1,y,x2):
    gap(x1,y,x2,y)
    for d in (-0.07,0,0.07): ax.plot([x1,x2],[y+d,y+d],color=K,lw=0.8,zorder=5)
def door(hx,hy,w,a1,a2,leaf):
    import math
    ax.add_patch(Arc((hx,hy),2*w,2*w,theta1=a1,theta2=a2,color=K,lw=0.7,ls='--',zorder=5))
    ax.plot([hx,hx+w*math.cos(math.radians(leaf))],[hy,hy+w*math.sin(math.radians(leaf))],color=K,lw=1.4,zorder=5)

FW='#7a4e2a'; FF='#f4ebe0'
def slide(a,b,c,o):
    ax.add_patch(Rectangle((a,c-0.03),b-a,0.06,color=FW,zorder=6))
    ax.annotate('',xy=(a+0.05,c),xytext=(a+0.35,c),arrowprops=dict(arrowstyle='->',lw=0.6,color=FW),zorder=6)
def tele():
    for xx in (1.70,1.76):
        ax.add_patch(Rectangle((xx-0.02,7.22),0.04,0.5,color=FW,zorder=6))
    ax.plot([1.66,1.66],[7.75,8.42],ls=':',color=FW,lw=1,zorder=6)
def furn(x,y,w,h,txt='',fs=6,rot=0):
    ax.add_patch(Rectangle((x,y),w,h,facecolor=FF,edgecolor=FW,lw=1,zorder=5))
    if txt: ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,color='#5a3a1e',rotation=rot,zorder=6)
ax.add_patch(Rectangle((0,0),5,12,fill=False,ls=(0,(6,3)),color='#888',lw=1))
wall(0,4.75,0,10.75); wall(5,3.75,5,10.75); wall(0,10.75,5,10.75)
wall(0,4.75,2.7,4.75); wall(2.7,3.75,5,3.75); wall(2.7,3.75,2.7,4.75)
wall(2.7,4.75,2.7,10.75,t); wall(0,7.15,2.7,7.15,t); wall(0,8.5,2.7,8.5,t); wall(1.6,7.15,1.6,8.5,t)
gap(2.85,3.75,3.65,3.75); door(2.85,3.75,0.8,270,360,270)
gap(3.95,10.75,4.75,10.75); door(4.75,10.75,0.8,180,270,270)
gap(2.7,7.21,2.7,8.44,t); gap(1.8,7.15,2.55,7.15,t); slide(1.0,1.8,7.04,'h')
gap(1.6,7.75,1.6,8.42,t); tele()
gap(1.8,8.5,2.55,8.5,t); slide(1.0,1.8,8.6,'h')
window(0.5,4.75,2.0); window(3.9,3.75,4.7); window(2.9,10.75,3.6); window(0.6,10.75,1.9)
ax.add_patch(Rectangle((2.76,10.07),1.0,0.6,fill=False,color=K,lw=1))
ax.add_patch(Rectangle((3.28,10.18),0.42,0.38,fill=False,color=K,lw=0.8))
ax.text(3.45,9.85,'counter + sink (no cooking)',ha='center',fontsize=7)
ax.add_patch(Circle((0.45,8.18),0.05,fill=False,color='#1f6fd1',lw=1,zorder=6)); ax.text(0.45,8.27,'floor drain',fontsize=4.5,ha='center',color='#1f6fd1'); ax.add_patch(Circle((1.15,7.55),0.07,fill=False,color='#1f6fd1',lw=1,zorder=6)); ax.text(1.15,7.65,'toilet outlet (approx.)',fontsize=4.2,ha='center',va='bottom',color='#1f6fd1'); ax.plot([0.6,0.8],[7.24,7.24],color='#1f6fd1',lw=2.5,zorder=6); ax.text(0.7,7.3,'water stubs',fontsize=4.2,ha='center',color='#1f6fd1'); ax.text(0.8,7.95,'T&B 1.60×1.35\nfixtures open to redesign',fontsize=5,ha='center',fontweight='bold')
ax.text(2.2,8.22,'HALL 1.10',ha='center',fontsize=6.5,fontweight='bold')
ax.plot([0,0,2.2,2.2,5,5],[4.75,4.15,4.15,3.15,3.15,3.75],ls=':',color='#555',lw=1.3,zorder=7); ax.text(1.1,4.27,'canopy above (≈0.6)',fontsize=5.5,ha='center',color='#555',zorder=7)
ax.add_patch(Rectangle((2.8,3.4),0.9,0.33,facecolor='#ddd',edgecolor=K,lw=0.6)); ax.text(3.25,3.52,'step',fontsize=6,ha='center')
ax.add_patch(Rectangle((-0.06,0.1),0.12,4.65,color='#999',zorder=3))
ax.text(-0.12,1.9,'low boundary wall',rotation=90,fontsize=6.5,color='#555',va='center',ha='right')
for xx in (0.25,0.42): ax.add_patch(Circle((xx,0.12),0.05,color='#1f6fd1',zorder=6))
ax.text(0.55,0.07,'water stubs',fontsize=6,color='#1f6fd1')
ax.add_patch(FancyBboxPatch((0.12,0.07),1.81,4.31,boxstyle='round,pad=0,rounding_size=0.35',fill=False,ls='--',color='#c0392b',lw=1.4,zorder=6))
ax.add_patch(Rectangle((0.3,1.35),1.45,0.45,fill=False,color='#c0392b',lw=0.8,zorder=6))
ax.text(1.025,2.9,'CAR\nMG ZS\n4.31 × 1.81',ha='center',va='center',fontsize=8,color='#c0392b',fontweight='bold')
ax.text(1.025,0.3,'▼ nose',ha='center',fontsize=7,color='#c0392b'); ax.text(1.025,4.48,'≈0.3 gap',ha='center',fontsize=5.5,color='#c0392b')


ax.add_patch(Rectangle((2.72,2.3),2.23,0.2,facecolor='#d9d4cc',edgecolor=K,lw=0.8,zorder=5)); ax.text(3.83,2.38,'breeze-block privacy wall (covers door)',fontsize=4.8,ha='center',va='center',zorder=6)
ax.add_patch(Rectangle((3.05,1.75),1.9,0.55,facecolor='#e3efdc',edgecolor='#6b8f5a',lw=0.7,zorder=4)); ax.text(4.0,2.0,'planting bed',fontsize=5,ha='center',color='#4d6e3f')
ax.annotate('',xy=(2.27,2.85),xytext=(2.27,1.2),arrowprops=dict(arrowstyle='-',lw=0.8,color='#555')); ax.annotate('',xy=(2.75,2.85),xytext=(2.3,2.85),arrowprops=dict(arrowstyle='->',lw=0.8,color='#555')); ax.text(2.27,1.0,'entry path ≈0.8\ndriver door ≈1.0',fontsize=5,color='#555',ha='center',va='top')
def lab(x,y,name,dims,area):
    ax.text(x,y+0.15,name,ha='center',fontsize=9.5,fontweight='bold')
    ax.text(x,y-0.2,f'{dims}\n{area} sqm',ha='center',va='top',fontsize=7,color='#444')
ax.text(1.35,6.75,'BEDROOM 1  2.70 × ≈2.40',ha='center',fontsize=7,fontweight='bold')

ax.text(2.08,9.7,'BEDROOM 2\n2.70 × 2.25',ha='center',fontsize=7,fontweight='bold')
ax.text(3.6,6.3,'LIVING\n2.30 × ≈3.40',ha='center',fontsize=7.5,fontweight='bold')
ax.text(3.45,8.6,'DINING /\nKITCHEN\n2.30 × 3.60',ha='center',fontsize=7.5,fontweight='bold')
ax.text(2.5,11.45,'REAR SERVICE AREA  ≈1.25 m deep (VERIFY)',ha='center',fontsize=8,fontweight='bold')
ax.text(4.1,0.75,'FRONT YARD (right)\n≈3.75 m deep',ha='center',fontsize=7.5,color='#444')
ax.text(2.5,-0.45,'S T R E E T',ha='center',fontsize=11,fontweight='bold',color='#666')
def dim(x1,y1,x2,y2,txt,vert):
    ax.annotate('',xy=(x1,y1),xytext=(x2,y2),arrowprops=dict(arrowstyle='<->',lw=0.6,color='#333',shrinkA=0,shrinkB=0))
    if vert: ax.text(x1-0.08,(y1+y2)/2,txt,rotation=90,ha='right',va='center',fontsize=7)
    else: ax.text((x1+x2)/2,y1+0.08,txt,ha='center',va='bottom',fontsize=7)
for a,b,s in [(0,4.75,'≈4.75'),(4.75,7.15,'≈2.40'),(7.15,8.5,'1.35'),(8.5,10.75,'2.25'),(10.75,12,'≈1.25')]: dim(-0.55,a,-0.55,b,s,True)
dim(-1.25,0,-1.25,12,'12.00 (lot depth, assumed)',True)
for a,b,s in [(0,3.75,'≈3.75'),(3.75,7.15,'≈3.40'),(7.15,10.75,'3.60'),(10.75,12,'≈1.25')]: dim(5.85,a,5.85,b,s,True)
dim(6.45,3.75,6.45,10.75,'7.00 house',True)
dim(0,12.35,2.7,12.35,'2.70',False); dim(2.7,12.35,5,12.35,'2.30',False)
dim(0,12.9,5,12.9,'5.00 (lot width, assumed)',False)
ax.text(2.5,13.75,'MARGA UNIT — PLEASANT HOMES II, DAET',ha='center',fontsize=13,fontweight='bold')
ax.text(2.5,13.4,'Base plan for interior design (to scale, unfurnished) · Lot 60 sqm · Floor area 32.3 sqm',ha='center',fontsize=8.5,color='#444')
for i in range(2): ax.add_patch(Rectangle((3.6+i,-1.0),1,0.12,color=K if i==0 else 'white',ec=K,lw=0.6))
ax.text(3.6,-1.25,'0',fontsize=6.5,ha='center'); ax.text(4.6,-1.25,'1',fontsize=6.5,ha='center'); ax.text(5.6,-1.25,'2 m',fontsize=6.5,ha='center')
ax.text(-1.8,-1.55,'≈ / VERIFY = estimated, confirm on site. Dimensions in metres, approx. centerlines.\nBrown bars = sliding doors inside rooms; T&B door = 2-panel telescopic slider; blue = existing plumbing points. Front door swings OUT.\nCar reversed in, hugging left wall: driver exits right, passengers alight on street. Do not idle (exhaust faces Bedroom 1 window).\nCanopy = one continuous stepped slab over Bedroom 1 window and entrance (overhead; car clears it).',fontsize=6.5,color='#555',va='top')

# STEP 2 OVERLAY — copied base above is intentionally unchanged.
# Proposal only; do not move base geometry to accommodate furniture.
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent
fig.set_size_inches(11, 18)
base_texts = list(ax.texts)
for label in base_texts:
    value = label.get_text()
    if value.startswith(('BEDROOM ', 'LIVING\n', 'DINING /', 'T&B 1.60',
                         'counter + sink', 'floor drain', 'toilet outlet', 'water stubs')):
        # Presentation labels only. Every original patch and line remains intact.
        label.set_visible(False)
    if value.startswith('Base plan for interior design'):
        label.set_text('STEP 2 / FURNITURE — proposal for owner approval · fixed base coordinates unchanged')
        subtitle = label

floor_items = []
overlay_artists = []

def box(key, x, y, w, h, label='', color='#f1e7d9', dashed=False, floor=True, fs=6):
    patch = Rectangle((x, y), w, h, facecolor=color, edgecolor='#806044',
                      lw=0.9, ls='--' if dashed else '-', zorder=8)
    patch.set_gid(key)
    ax.add_patch(patch)
    overlay_artists.append(patch)
    if floor:
        floor_items.append((key, x, y, w, h))
    if label:
        text = ax.text(x+w/2, y+h/2, label, ha='center', va='center',
                       fontsize=fs, color='#493b2f', zorder=10)
        overlay_artists.append(text)
    return patch

def note(x, y, text, size=6, color='#344b45', rotation=0):
    artist = ax.text(x, y, text, fontsize=size, ha='center', va='center',
                     color=color, rotation=rotation, zorder=12,
                     bbox=dict(facecolor='white', edgecolor='none', alpha=0.85, pad=1))
    overlay_artists.append(artist)
    return artist

def clearance(x1, y1, x2, y2, label, text_xy):
    artist = ax.annotate('', xy=(x1,y1), xytext=(x2,y2), zorder=12,
                         arrowprops=dict(arrowstyle='<->', color='#377e65', lw=0.8,
                                         shrinkA=0, shrinkB=0))
    overlay_artists.append(artist)
    note(*text_xy, label, size=5.6)

# Conservative continuous 100 mm right-wall build-up, measured INWARD
# from x=4.925 (inside face), never out into an invented room extension.
box('cladding', 4.825, 3.825, .10, 6.85, '', '#c8b195', floor=False)

# Bedroom 1: mattress-sized flush platform; separate 40 mm headboard.
box('queen', .115, 4.825, 1.90, 1.52, 'BR1 / QUEEN\n152 × 190\nflush platform + drawers', fs=7)
box('headboard', .075, 4.825, .04, 1.52)
box('queen-pillow', .18, 4.98, .40, .55, floor=False, color='#fffdf8')
box('queen-pillow2', .18, 5.65, .40, .55, floor=False, color='#fffdf8')
clearance(2.25, 6.345, 2.25, 7.10, '75.5 cm access', (1.15,6.72))
clearance(2.015,5.60,2.65,5.60,'63.5 cm foot',(2.33,5.85))
note(.12, 6.52, 'B&W photo wall above headboard', size=5.1)
note(2.40, 6.52, 'hooks above\nfoot route', size=5.1)

# Bedroom 2: the specified OUTER frame, not a shrunken mattress outline.
box('bunk', .075, 8.675, 1.50, 2.00, 'BR2 / BUNK\nframe 150 × 200\nupper double 137 × 190\nlower single 91 × 190', fs=6.1)
box('upper-mattress', .14, 8.725, 1.37, 1.90, '', floor=False, dashed=True)
box('bunk-ladder', 1.575, 9.10, .35, .45, 'ladder', fs=4.8)
box('owner-cabinet', 2.35, 9.90, .30, .70, 'LOCKED\nowner\n30 × 70', fs=5.0)
note(1.35, 8.83, '12.5 cm at door wall', size=5)
clearance(1.925,9.35,2.65,9.35,'72.5 cm',(2.27,9.12))
note(.825, 9.06, 'min 8 cm clear between bunk\nand door wall for sliding panel', size=4.7)

# Living: sofa against shared wall; no floor-standing media unit or coffee table.
box('sofa', 2.75, 4.75, .78, 1.70, 'SOFA\n170 × 78', fs=6.6)
box('sofa-back', 2.75, 4.75, .12, 1.70, '', '#d3c1ac', floor=False)
box('side-table', 2.75, 6.55, .35, .30, 'side', fs=4.7)
box('tv', 4.825, 5.00, .045, 1.23, '', '#252b2a', floor=False)
note(4.50, 5.54, '55" TV\n123 × 71\nrecess 8–10 cm', size=5.4)
clearance(3.20,6.10,4.825,6.10,'≈1.6 m eye → screen',(4.0,6.30))
note(3.84,4.23,'ENTRY / keep clear',size=6)
note(2.88,5.62,'photo gallery above sofa',size=4.7,rotation=90)

# Dining: two seated places, not a fictitious five-seat arrangement.
box('dining-table', 4.275, 7.15, .55, 1.20, 'fold-down\ntable\n120 × 55', fs=5.6)
box('dining-chair1', 3.725, 7.225, .50, .45, 'chair', fs=4.8)
box('dining-chair2', 3.725, 7.825, .50, .45, 'chair', fs=4.8)
clearance(2.75,7.55,3.525,7.55,'77.5 cm route*',(3.12,7.34))
note(3.52,8.68,'DINING / KITCHENETTE\n2 seats; *allows 20 cm chair pullback',size=5.8)

# Compact fridge with microwave shelf ABOVE; neither touches the fixed counter.
box('fridge', 4.225, 8.95, .60, .60, 'FRIDGE\n60 × 60\nmicro above', fs=5.3)
# Small appliances on existing counter (elevated, not floor obstacles).
box('water-dispenser', 2.78, 10.15, .28, .30, 'water', fs=4.4, floor=False)
box('kettle', 3.08, 10.15, .18, .22, 'K', fs=4.4, floor=False)
note(3.36,10.52,'fixed counter / sink',size=4.8)
clearance(3.25,9.32,3.25,10.07,'75 cm counter approach',(3.52,9.62))
note(4.36,9.80,'rear-door swing kept clear',size=5.0)

# T&B: full-size toilet uses the existing outlet; no new drain locations.
# Wet-room proposal leaves shower access open. Glass needs owner review.
box('shower-zone', .075, 7.65, .80, .80, 'SHOWER\n80 × 80\nopen wet zone', '#e3eee9', dashed=True, floor=False, fs=5.2)
box('toilet', .96, 7.20, .38, .68, 'WC\n38 × 68', '#fffdf8', fs=4.9)
box('basin', .15, 7.20, .50, .30, 'basin 50 × 30', '#fffdf8', fs=4.6)
clearance(1.15,7.88,1.15,8.45,'57 cm WC front',(1.29,8.17))
note(.55,8.55,'T&B route 54–57 cm < 60: REVIEW',size=5.2,color='#a05232')
# Keep existing blue plumbing markers visible over new fixture footprints.
ax.scatter([.45,1.15],[8.18,7.55],s=10,facecolors='none',edgecolors='#1f6fd1',zorder=16)

# Covered court and service equipment reservations, all new/proposed.
box('shoe-bench', 3.80, 3.20, 1.00, .35, 'shoe bench 100 × 35', fs=5.1)
for index, x in enumerate((.15, 1.10, 2.05), 1):
    box(f'condenser-{index}', x, 10.90, .75, .30, f'ODU {index}',
        '#e7ecef', dashed=True, floor=False, fs=4.9)
note(2.50,11.90,'wall-mounted outdoor units; tank + drying locations to verify',size=5.7)

# Furniture checks use wall faces, never the room's nominal centerline width.
assert abs((7.15-.05)-(4.825+1.52)-.755) < 1e-9
assert abs(8.675-(8.50+.05)-.125) < 1e-9
assert 8.675-(8.50+.05) >= .08
assert 2.65-(1.575+.35) >= .60
assert 8.45-(7.20+.68) >= .55
note(2.50, -.02, 'PROPOSAL — dimensions in metres; furniture labels in cm. See step2_review.md.',size=6.4)
fig.savefig(OUTPUT_DIR / 'step2_layout.png', dpi=220, bbox_inches='tight', facecolor='white')

# Electrical sheet: same geometry and furniture, subdued for legible point IDs.
for artist in overlay_artists:
    artist.set_alpha(.22)
subtitle.set_text('STEP 2 / ELECTRICAL — proposed point locations · circuit capacity and routing unverified')

# ID, x, y, category. Coordinates are proposed point locations, not wire routes.
ELECTRICAL = [
    ('A1',2.65,6.15,'ac'), ('A2',2.65,10.15,'ac'), ('A3',2.75,4.35,'ac'),
    ('H1',.12,8.30,'power'), ('U1',.12,6.24,'power'),
    ('U2',.12,10.45,'power'), ('U3',.12,10.15,'power'),
    ('P1',4.87,5.62,'power'), ('P2',4.87,9.25,'power'),
    ('P3',3.10,10.67,'power'), ('P4',4.87,7.75,'power'),
    ('P5',2.75,6.70,'power'), ('P6',4.65,3.70,'power'),
    ('C1',4.95,3.75,'data'), ('K1',3.60,3.75,'data'),
    ('G1',.075,5.62,'light'), ('G2',2.75,5.62,'light'),
    ('L1',1.35,6.75,'light'), ('L2',2.05,9.60,'light'),
    ('L3',3.85,5.60,'light'), ('L4',3.70,8.00,'light'),
    ('L5',1.05,8.10,'light'), ('L6',2.20,7.80,'light'),
    ('L7',4.15,3.20,'light'), ('L8',4.20,11.15,'light'),
    ('L9',3.05,10.15,'light'),
    ('S1',3.80,3.80,'switch'), ('S2',2.60,6.85,'switch'),
    ('S3',2.60,8.85,'switch'), ('S4',1.70,8.48,'switch'),
    ('S5',4.87,9.65,'switch'),
]
COLORS = dict(ac='#2c7f91',power='#ac482d',data='#785ba3',light='#b3840b',switch='#326846')
MARKERS = dict(ac='s',power='s',data='D',light='o',switch='^')
for key,x,y,kind in ELECTRICAL:
    ax.scatter([x],[y],s=24,c='white',edgecolors=COLORS[kind],
               marker=MARKERS[kind],linewidths=1,zorder=21)
    # Alternate cramped bedside points; keep identifiers within the plot.
    dx = -.28 if x > 4.8 else .19
    dy = .12
    if key in ('U3','P3','L9','K1','S1','S4','L5','P6'):
        dy = -.16
    ax.text(x+dx,y+dy,key,fontsize=6.0,color=COLORS[kind],zorder=22,
            ha='center',va='center',bbox=dict(fc='white',ec='none',alpha=.93,pad=.6))
note(2.5,11.64,'A1/A2/A3: three dedicated AC circuits · H1: dedicated heater circuit',size=6.0)
note(2.5,11.42,'Panel location / rating / free slots: NEEDED — no panel invented',size=6.0,color='#a05232')
note(2.5,-.06,'A = AC   H/U/P = power   C/K = CCTV/lock   L/G = lights   S = switches',size=6.0)
fig.savefig(OUTPUT_DIR / 'step2_electrical.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close(fig)
