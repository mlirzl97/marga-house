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
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)),'marga_base_plan.png'),dpi=220,bbox_inches='tight',facecolor='white')
