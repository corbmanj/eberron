import os
OUT=os.path.dirname(os.path.abspath(__file__))
P=10          # px per foot
M=40          # margin
LEG=390       # legend width
BG="#f4ecd8"; WALL="#2e2622"; GRID="#ddd0b3"; RED="#8b1e1e"; INK="#3a2f28"; WIN="#7fa7c9"

def floor(fname,title,w,h,rooms,doors,windows,stairs,feats,extra_h=0,notes=()):
    W=M*2+w*P+LEG; H=M*2+(h+extra_h)*P+40
    X=lambda f:M+f*P; Y=lambda f:M+30+f*P
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Georgia, serif">',
       f'<rect width="{W}" height="{H}" fill="{BG}"/>',
       f'<text x="{M}" y="{M+8}" font-size="22" fill="{INK}" font-weight="bold">{title}</text>']
    # grid
    for gx in range(0,w+1,5): o.append(f'<line x1="{X(gx)}" y1="{Y(0)}" x2="{X(gx)}" y2="{Y(h+extra_h)}" stroke="{GRID}" stroke-width="1"/>')
    for gy in range(0,h+extra_h+1,5): o.append(f'<line x1="{X(0)}" y1="{Y(gy)}" x2="{X(w)}" y2="{Y(gy)}" stroke="{GRID}" stroke-width="1"/>')
    # rooms
    for r in rooms:
        n,name,(x0,y0,x1,y1),kind=r[:4]
        if kind=="outside":
            o.append(f'<rect x="{X(x0)}" y="{Y(y0)}" width="{(x1-x0)*P}" height="{(y1-y0)*P}" fill="#e6dcc3" stroke="{WALL}" stroke-width="2" stroke-dasharray="8 5"/>')
        else:
            fill={"scorch":"#d9c7a8","ritual":"#efe2c9"}.get(kind,"none")
            o.append(f'<rect x="{X(x0)}" y="{Y(y0)}" width="{(x1-x0)*P}" height="{(y1-y0)*P}" fill="{fill}" fill-opacity="0.9" stroke="{WALL}" stroke-width="6"/>')
    # stairs
    for (x0,y0,x1,y1,d,label) in stairs:
        o.append(f'<rect x="{X(x0)}" y="{Y(y0)}" width="{(x1-x0)*P}" height="{(y1-y0)*P}" fill="#e9dfc6" stroke="{INK}" stroke-width="2"/>')
        if d in "ns":
            for yy in range(int(y0)+1,int(y1)): o.append(f'<line x1="{X(x0)}" y1="{Y(yy)}" x2="{X(x1)}" y2="{Y(yy)}" stroke="{INK}" stroke-width="1.2"/>')
            ya,yb=(Y(y1)-8,Y(y0)+8) if d=="n" else (Y(y0)+8,Y(y1)-8)
            xm=X((x0+x1)/2); o.append(f'<line x1="{xm}" y1="{ya}" x2="{xm}" y2="{yb}" stroke="{RED}" stroke-width="2.5" marker-end="url(#ar)"/>')
        else:
            for xx in range(int(x0)+1,int(x1)): o.append(f'<line x1="{X(xx)}" y1="{Y(y0)}" x2="{X(xx)}" y2="{Y(y1)}" stroke="{INK}" stroke-width="1.2"/>')
        o.append(f'<text x="{X((x0+x1)/2)}" y="{Y(y1)+14}" font-size="11" text-anchor="middle" fill="{RED}" font-style="italic">{label}</text>')
    # features
    for f in feats:
        kind=f[0]
        if kind=="rect":
            _,x0,y0,x1,y1,label=f[:6]; col=f[6] if len(f)>6 else "#c8b48f"
            o.append(f'<rect x="{X(x0)}" y="{Y(y0)}" width="{(x1-x0)*P}" height="{(y1-y0)*P}" fill="{col}" stroke="{INK}" stroke-width="1.5"/>')
            if label: o.append(f'<text x="{X((x0+x1)/2)}" y="{Y((y0+y1)/2)+4}" font-size="10" text-anchor="middle" fill="{INK}">{label}</text>')
        elif kind=="circle":
            _,cx,cy,r,label,col=f
            o.append(f'<circle cx="{X(cx)}" cy="{Y(cy)}" r="{r*P}" fill="{col}" stroke="{INK}" stroke-width="1.5"/>')
            if label: o.append(f'<text x="{X(cx)}" y="{Y(cy)+4}" font-size="10" text-anchor="middle" fill="{INK}">{label}</text>')
        elif kind=="ritual":
            _,cx,cy,r=f
            for i in range(7): o.append(f'<circle cx="{X(cx)}" cy="{Y(cy)}" r="{(r-i*0.9)*P}" fill="none" stroke="{RED}" stroke-width="1" stroke-dasharray="{"3 3" if i%2 else "none"}"/>')
        elif kind=="grave":
            _,x0,y0,x1,y1,label=f
            o.append(f'<rect x="{X(x0)}" y="{Y(y0)}" width="{(x1-x0)*P}" height="{(y1-y0)*P}" fill="#a8906b" stroke="{RED}" stroke-width="2" stroke-dasharray="5 3"/>')
            o.append(f'<text x="{X((x0+x1)/2)}" y="{Y((y0+y1)/2)+4}" font-size="10" text-anchor="middle" fill="{RED}" font-weight="bold">{label}</text>')
        elif kind=="doll":
            _,cx,cy=f
            o.append(f'<circle cx="{X(cx)}" cy="{Y(cy)}" r="5" fill="#f7f1e6" stroke="{RED}" stroke-width="2"/>')
        elif kind=="text":
            _,cx,cy,t=f
            o.append(f'<text x="{X(cx)}" y="{Y(cy)}" font-size="10" text-anchor="middle" fill="{INK}" font-style="italic">{t}</text>')
    # windows
    for (o_,a,b0,b1) in windows:
        if o_=="h": o.append(f'<rect x="{X(b0)}" y="{Y(a)-3}" width="{(b1-b0)*P}" height="6" fill="{WIN}" stroke="{WALL}" stroke-width="1"/>')
        else: o.append(f'<rect x="{X(a)-3}" y="{Y(b0)}" width="6" height="{(b1-b0)*P}" fill="{WIN}" stroke="{WALL}" stroke-width="1"/>')
    # doors
    for (o_,a,b0,b1,*rest) in doors:
        style=rest[0] if rest else "door"
        if o_=="h":
            o.append(f'<rect x="{X(b0)}" y="{Y(a)-4}" width="{(b1-b0)*P}" height="8" fill="{BG}"/>')
            col=RED if style in("locked","front") else INK
            o.append(f'<line x1="{X(b0)}" y1="{Y(a)}" x2="{X(b1)}" y2="{Y(a)}" stroke="{col}" stroke-width="{3 if style!="door" else 1.5}" stroke-dasharray="{"6 3" if style=="boarded" else "none"}"/>')
            if style=="locked": o.append(f'<text x="{X((b0+b1)/2)}" y="{Y(a)-7}" font-size="9" text-anchor="middle" fill="{RED}">locked</text>')
        else:
            o.append(f'<rect x="{X(a)-4}" y="{Y(b0)}" width="8" height="{(b1-b0)*P}" fill="{BG}"/>')
            col=RED if style in("locked","front") else INK
            o.append(f'<line x1="{X(a)}" y1="{Y(b0)}" x2="{X(a)}" y2="{Y(b1)}" stroke="{col}" stroke-width="{3 if style!="door" else 1.5}" stroke-dasharray="{"6 3" if style=="boarded" else "none"}"/>')
            if style=="locked": o.append(f'<text x="{X(a)+6}" y="{Y((b0+b1)/2)}" font-size="9" fill="{RED}">locked</text>')
    # room numbers
    for r in rooms:
        n,name,(x0,y0,x1,y1),kind=r[:4]
        if len(r)>4: cx,cy=X(r[4][0]),Y(r[4][1])
        else: cx,cy=X((x0+x1)/2),(Y(y0)+18 if kind!="outside" else Y((y0+y1)/2))
        o.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{RED}"/><text x="{cx}" y="{cy+5}" font-size="13" text-anchor="middle" fill="white" font-weight="bold">{n}</text>')
    # legend
    lx=M+w*P+30; ly=Y(0)
    o.append(f'<text x="{lx}" y="{ly}" font-size="15" fill="{INK}" font-weight="bold">Key</text>')
    ly+=22
    for r in rooms:
        n,name=r[0],r[1]
        o.append(f'<circle cx="{lx+9}" cy="{ly-4}" r="9" fill="{RED}"/><text x="{lx+9}" y="{ly}" font-size="11" text-anchor="middle" fill="white" font-weight="bold">{n}</text><text x="{lx+24}" y="{ly}" font-size="13" fill="{INK}">{name}</text>')
        ly+=22
    ly+=10
    syms=[(lambda y:f'<line x1="{lx}" y1="{y-4}" x2="{lx+18}" y2="{y-4}" stroke="{INK}" stroke-width="1.5"/>',"Door"),
          (lambda y:f'<line x1="{lx}" y1="{y-4}" x2="{lx+18}" y2="{y-4}" stroke="{RED}" stroke-width="3"/>',"Locked, sealed, or looping door"),
          (lambda y:f'<line x1="{lx}" y1="{y-4}" x2="{lx+18}" y2="{y-4}" stroke="{RED}" stroke-width="3" stroke-dasharray="6 3"/>',"Boarded door"),
          (lambda y:f'<rect x="{lx}" y="{y-7}" width="18" height="6" fill="{WIN}" stroke="{WALL}"/>',"Window"),
          (lambda y:f'<circle cx="{lx+9}" cy="{y-4}" r="5" fill="#f7f1e6" stroke="{RED}" stroke-width="2"/>',"Doll (starting spot)")]
    for fn,label in syms:
        o.append(fn(ly)); o.append(f'<text x="{lx+26}" y="{ly}" font-size="12" fill="{INK}">{label}</text>'); ly+=20
    ly+=8
    for line in notes:
        o.append(f'<text x="{lx}" y="{ly}" font-size="11" fill="{INK}" font-style="italic">{line}</text>'); ly+=16
    # scale + compass
    sy=Y(h+extra_h)+24
    o.append(f'<line x1="{X(0)}" y1="{sy}" x2="{X(10)}" y2="{sy}" stroke="{INK}" stroke-width="3"/><text x="{X(10)+8}" y="{sy+4}" font-size="11" fill="{INK}">10 ft · each square is 5 ft</text>')
    o.append(f'<text x="{X(w)-10}" y="{sy+4}" font-size="14" fill="{INK}" font-weight="bold" text-anchor="end">N ↑</text>')
    o.insert(1,f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{RED}"/></marker></defs>')
    o.append('</svg>')
    open(os.path.join(OUT,fname),"w").write("\n".join(o).replace(" & "," &amp; "))

# ---------------- MAIN FLOOR ----------------
floor("house_main_floor.svg","The Maker's House: Main Floor",60,50,
 rooms=[(1,"Front Porch",(10,50,50,58),"outside",(20,54)),(2,"Foyer",(22,20,38,50),"room",(34.5,46)),(3,"Toy Shop",(38,30,60,50),"room",(41.5,37.5)),
        (4,"Parlor",(0,20,22,50),"scorch",(18,46)),(5,"Dining Room",(38,18,50,30),"room",(48.3,28.3)),(6,"Kitchen",(38,0,60,18),"room",(40.5,15)),
        (7,"Pantry & Cellar Door",(50,18,60,30),"room",(51.3,25)),(8,"Study",(0,0,22,20),"room",(18.5,16.5)),(9,"Back Hall",(22,0,38,20),"room",(25,3.5))],
 doors=[("h",50,28,32,"front"),("v",22,40,44),("v",38,40,44),("h",20,31,36),("v",22,8,12),("v",38,8,12),("h",0,28,32,"front"),
        ("h",18,42,46),("h",18,54,58),("h",30,42,46),("h",50,53,57,"boarded")],
 windows=[("h",50,4,9),("h",50,13,18),("v",0,28,34),("v",0,38,44),("v",0,6,12),("h",0,6,12),("h",0,44,52),("v",60,4,12),
          ("h",50,40,50),("v",60,36,44),("h",50,23,26),("h",50,34,37)],
 stairs=[(24,22,30,38,"n","up"),(52,22,59,28,"s","")],
 feats=[("rect",35,21,37,23,"",'#6b4a2e'),("text",32,25,"clock"),("rect",40,31,58,34,"shelves"),("rect",44,40,52,43,"counter"),
        ("rect",41,46,50,49,"display window"),("rect",2,22,8,25,"hearth",'#9a8468'),("rect",6,36,14,40,"settee"),("circle",11,26,1.5,"",'#c8b48f'),("text",11,29.5,"cradle"),
        ("rect",40,21,48,27,"table"),("rect",40,1,58,4,"counter & stove"),("rect",45,8,53,13,"table"),
        ("rect",51,19,59,21,"shelves"),("rect",2,2,12,7,"desk"),("rect",14,1,21,4,"bookcase"),
        ("doll",47,45.3),("doll",26,37),("doll",36,26),("doll",6.8,37),("doll",11,26),("doll",47,26.3),("doll",3.5,6.2),("doll",42,32.5),("doll",51,41.5),("doll",53.5,32.5),("doll",57,46),("doll",58.2,8),("doll",46.5,12.2),("doll",23.5,14),("doll",57,32.5)],
 notes=["Parlor is fire-scorched; front windows","are smashed. Cellar stairs in the","pantry lead down to the basement.","Both outside doors loop to the foyer."],extra_h=9)

# ---------------- UPPER FLOOR ----------------
floor("house_upper_floor.svg","The Maker's House: Upper Floor",60,50,
 rooms=[(10,"Upper Hall & Gallery",(22,0,38,50),"room",(25,46)),(11,"Master Bedroom",(0,0,22,22),"room",(16,11)),(12,"Painting Room",(0,22,22,50),"room",(18,46)),
        (13,"Rosie's Room",(38,0,60,18),"room",(41.5,4)),(14,"Washroom",(38,18,60,30),"room",(42,27)),(15,"Guest Room",(38,30,60,50),"scorch",(42,46))],
 doors=[("v",22,10,14),("v",22,34,38),("v",38,8,12),("v",38,22,26),("v",38,40,44)],
 windows=[("h",0,6,14),("v",0,6,14),("h",50,4,10),("h",50,13,18),("v",0,30,40),("h",0,44,54),("v",60,5,12),("h",50,42,54),("v",60,36,44),("h",50,27,33)],
 stairs=[(24,22,30,38,"s","down to foyer")],
 feats=[("rect",3,3,11,10,"bed"),("rect",13,1,15,4,"stand"),("text",14,6,"journal"),("rect",18,14,21,20,"mirror",'#b9c7cf'),("rect",2,15,8,20,"wardrobe"),
        ("rect",2,24,14,28,"paint table"),("rect",16,24,21,34,"shelves"),("text",18.5,37,"ledger"),("rect",4,40,12,46,"easel"),
        ("rect",48,2,57,8,"small bed"),("text",52.5,10,"Rosie's empty doll"),("rect",40,12,43,15,"toy chest"),("text",52.5,12,"key on hook"),
        ("rect",50,20,58,25,"tub"),("rect",46,34,55,40,"burned bed",'#8a7358'),("rect",30.5,2,37,8,"linen press"),("rect",30.5,42,37,48,"window seat")],
 notes=["Rosie's empty doll sits on the small","bed. The basement key hangs beside it.","Guest room is burned through at the","south window where torches came in."])

# ---------------- BASEMENT ----------------
floor("house_basement.svg","The Maker's House: Basement",60,45,
 rooms=[(16,"Stair Hall",(35,15,60,28),"room",(40,24.5)),(17,"Root Cellar",(35,0,60,15),"room",(40,10)),(18,"Workshop (Ritual Chamber)",(0,0,35,45),"ritual",(7,18)),
        (19,"Kiln Room",(35,28,60,45),"room",(47.5,31.5)),(20,"Mold Storage",(0,0,12,12),"room",(6,8))],
 doors=[("h",15,44,48),("v",35,19,24),("h",28,40,44),("v",35,36,40),("h",12,4,8),("v",60,30,34,"front")],
 windows=[],
 stairs=[(52,18,60,28,"n","")],
 feats=[("ritual",17,24,6.5),("circle",17,24,1.5,"",'#f7f1e6'),("text",17,32.5,"faceless doll · ritual circle"),
        ("rect",14,1,33,4,"workbench (mortar)"),("rect",1,30,4,43,"bench"),("rect",22,40,33,44,"drawer cabinet (eyes)"),("rect",27,14,33,18,"lathe"),
        ("rect",5,40,12,44,"parts rack"),("rect",37,1,58,4,"shelves & barrels"),("rect",50,33,58,43,"kiln",'#9a6b4a'),
        ("grave",38,37,45,43,"grave"),("text",55,31,"coal chute"),("text",48,17,"stairs up to pantry"),("rect",1,1,11,4,"molds"),("circle",8,33,1,"",'#6b4a2e'),("circle",27,27,1,"",'#6b4a2e'),("text",8,36,"post"),("text",27,30,"post")],
 notes=["The grave is under the brick floor,","shown to the party in the first dream.","The coal chute loops to the foyer.","Workshop is 35 x 45 ft."])
print("done")
