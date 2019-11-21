import pygame, sys, random, time
pygame.init()
inf = pygame.display.Info()
w,h = int(inf.current_w),int(inf.current_h)
screen = pygame.display.set_mode((w,h),pygame.FULLSCREEN)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
turq = (12,120,126)
brown = (196, 113, 35)
pygame.display.flip()
bg = pygame.image.load('Bangalorecity.jpg')
mapp = pygame.image.load('bangaloremap.jpg')
pygame.display.set_caption("Bangalore City Travel Guide")
fonta = pygame.font.Font(None,50)
arrow = fonta.render("->",10,black)
h1 = h2 = h3 = h4 = 0
c1 = c2 = c3 = c4 = 0
count1 = count2 = 0
chpl2 = ''
chpl = []
chp = []
gh1 = [[999.0, 7.9, 8.6, 6.0],
       [7.9, 999.0, 2.0, 5.0],
       [8.6, 2.0, 999.0, 5.3],
       [6.0, 5.0, 5.3, 999.0]]
gh = [[0]*4]*4
srcs = [0,0,0,0]
hnames = ["Lumbini Gardens","Jayaprakash Narayan Park","IISc","Hebbal Lake Park"]
hnames2 = []
ah = bh = 1
hb1 = hb2 = hb3 = hb4 = 0
cb1 = cb2 = cb3 = cb4 = 0
countb1 = countb2 = 0
chplb2 = ''
chplb = []
chpb = []
gb1 = [[999.0, 3.4, 1.1, 3.7],
       [3.4, 999.0, 1.8, 2.5],
       [1.1, 1.8, 999.0, 2.5],
       [3.7, 2.5, 2.5, 999.0]]
gb = [[0]*4]*4
srcs2 = [0,0,0,0]
bnames = ["Ashoka Pillar","Bull Temple","Lalbagh","Tippu Sultan Palace"]
bnames2 = []
ab = bb = 1
hm1 = hm2 = hm3 = hm4 = 0
cm1 = cm2 = cm3 = cm4 = 0
countm1 = countm2 = 0
chplm2 = ''
chplm = []
chpm = []
gm1 = [[999.0, 1.3, 1.7, 2.3],
       [1.3, 999.0, 2.9, 2.8],
       [1.7, 2.9, 999.0, 2.2],
       [2.3, 2.8, 2.2, 999.0]]
gm = [[0]*4]*4
srcs3 = [0,0,0,0]
mnames = ["Vidhana Soudha","Cubbon Park","Jawaharlal Nehru Planetarium","St.Mary's Basilica"]
mnames2 = []
am = bm = 1
hr1 = hr2 = hr3 = hr4 = 0
cr1 = cr2 = cr3 = cr4 = 0
countr1 = countr2 = 0
chplr2 = ''
chplr = []
chpr = []
gr1 = [[999.0, 3.6, 6.4, 8.5],
       [3.6, 999.0, 3.8, 6.0],
       [6.4, 3.8, 999.0, 1.8],
       [8.6, 6.0, 1.8, 999.0]]
gr = [[0]*4]*4
srcs4 = [0,0,0,0]
rnames = ["Bangalore Palace","Sankey Tank","World Trade Center","Iskcon Temple"]
rnames2 = []
ar = br = 1
hj1 = hj2 = hj3 = hj4 = 0
cj1 = cj2 = cj3 = cj4 = 0
countj1 = countj2 = 0
chplj2 = ''
chplj = []
chpj = []
gj1 = [[999.0, 1.3, 5.1, 4.9],
       [1.3, 999.0, 3.7, 2.2],
       [5.1, 3.7, 999.0, 3.3],
       [4.9, 2.2, 3.3, 999.0]]
gj = [[0]*4]*4
srcs5 = [0,0,0,0]
jnames = ["KR Market","Freedom Park","Mantri Square","Race Course"]
jnames2 = []
aj = bj = 1
f = 0
f1 = 0
out = True
def dijkstra(matrix,m,k,cnt):
    cost=[[0 for x in range(cnt)] for x in range(1)]
    offsets = []
    summ = 0.0
    offsets.append(k)
    elepos=0
    for j in range(cnt):
        cost[0][j]=matrix[k][j]
    mini=999.0
    for x in range(cnt-1):
        mini=999.0
        for j in range (cnt):
                if cost[0][j]<=mini and j not in offsets:
                        mini=cost[0][j]
                        elepos=j
        offsets.append(elepos)
        for j in range (cnt):
            if cost[0][j] >cost[0][elepos]+matrix[elepos][j]:
                cost[0][j]=cost[0][elepos]+matrix[elepos][j]
    return offsets
def distance(matrix,chpp):
    dist = 0.0
    j = k = 0
    for i in chpp:
        if k==(len(chpp)-1):
            break
        k = k + 1
        dist = dist + matrix[i][chpp[k]]
    return dist
while out:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            out = False
            break
        if f==0:
            #HomeScreen
            screen.fill(black)
            imagRect = bg.get_rect()
            size = (w,h) = bg.get_size()
            x,y = screen.get_size()
            screen.blit(bg,(0,0))
            fontbig = pygame.font.Font(None, 70)
            font = pygame.font.Font(None, 50)
            fonts = pygame.font.Font(None, 30)
            txt1 = fontbig.render("Welcome to Bangalore City!", 10, black)
            start = font.render("Start Tour ->", 10, black)
            startbut = pygame.draw.rect(screen,white,pygame.Rect(560,340,200,40))
            exitt = fonts.render("EXIT", 10, black)
            exitbut = pygame.draw.rect(screen,white,pygame.Rect(1100,500,55,22))
            screen.blit(txt1,(350,170))
            screen.blit(start,startbut)
            screen.blit(exitt,exitbut)
            pos = pygame.mouse.get_pos()
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            if startbut.collidepoint(pos):
                startbut = pygame.draw.rect(screen,turq,pygame.Rect(560,340,200,40))
                screen.blit(start,startbut)
                if pressed1==1:
                    pygame.display.flip()
                    f = 1
                    break
                break
            if exitbut.collidepoint(pos):
                exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1100,500,55,22))
                screen.blit(exitt,exitbut)
                if pressed1==1:
                    pygame.display.flip()
                    out = False
                    f = -1
                    break
                break
            break
        if f==1:
            #SecondScreen
            screen.fill(white)
            mappRect = mapp.get_rect()
            size = (w,h) = mapp.get_size()
            x,y = screen.get_size()
            screen.blit(mapp,(0,0))
            fontbig = pygame.font.Font(None, 70)
            font = pygame.font.Font(None, 80)
            fonts = pygame.font.Font(None, 30)
            ques1 = font.render("Which one of these places ",10,black)
            ques2 = font.render("are you closest to?",10,black)
            heb = fontbig.render("Hebbal", 10, white)
            bsk = fontbig.render("Banashankari", 10, white)
            mg = fontbig.render("MG Road", 10, white)
            raj = fontbig.render("Rajajinagar", 10, white)
            maj = fontbig.render("Majestic", 10, white)
            exitt = fonts.render("EXIT", 10, black)
            hebbt = pygame.draw.rect(screen,black,pygame.Rect(600,120,190,45))
            bskbt = pygame.draw.rect(screen,black,pygame.Rect(950,565,340,45))
            mgbt = pygame.draw.rect(screen,black,pygame.Rect(150,580,240,45))
            rajbt = pygame.draw.rect(screen,black,pygame.Rect(980,270,280,45))
            majbt = pygame.draw.rect(screen,black,pygame.Rect(150,270,200,45))
            exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1150,670,55,22))
            screen.blit(ques1,(370,375))
            screen.blit(ques2,(420,420))
            screen.blit(heb,hebbt)
            screen.blit(bsk,bskbt)
            screen.blit(mg,mgbt)
            screen.blit(raj,rajbt)
            screen.blit(maj,majbt)
            screen.blit(exitt,exitbut)
            pos = pygame.mouse.get_pos()
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            if hebbt.collidepoint(pos):
                heb = fontbig.render("Hebbal", 10, black)
                hebbtt = pygame.draw.rect(screen,turq,pygame.Rect(600,120,190,45))
                screen.blit(heb,hebbt)
                if pressed1==1:
                    pygame.display.flip()
                    f = 2
                    f1 = 1
                    break
                break
            if bskbt.collidepoint(pos):
                bsk = fontbig.render("Banashankari", 10, black)
                bskbt = pygame.draw.rect(screen,turq,pygame.Rect(950,565,340,45))
                screen.blit(bsk,bskbt)
                if pressed1==1:
                    pygame.display.flip()
                    f = 2
                    f1 = 2
                    break
                break
            if mgbt.collidepoint(pos):
                mg = fontbig.render("MG Road", 10, black)
                mgbt = pygame.draw.rect(screen,turq,pygame.Rect(150,580,240,45))
                screen.blit(mg,mgbt)
                if pressed1==1:
                    pygame.display.flip()
                    f = 2
                    f1 = 3
                    break
                break
            if rajbt.collidepoint(pos):
                raj = fontbig.render("Rajajinagar", 10, black)
                rajbt = pygame.draw.rect(screen,turq,pygame.Rect(980,270,280,45))
                screen.blit(raj,rajbt)
                if pressed1==1:
                    pygame.display.flip()
                    f = 2
                    f1 = 4
                    break
                break
            if majbt.collidepoint(pos):
                maj = fontbig.render("Majestic", 10, black)
                majbt = pygame.draw.rect(screen,turq,pygame.Rect(150,270,200,45))
                screen.blit(maj,majbt)
                if pressed1==1:
                    pygame.display.flip()
                    f = 2
                    f1 = 5
                    break
                break
            if exitbut.collidepoint(pos):
                exitt = fonts.render("EXIT", 10, white)
                exitbut = pygame.draw.rect(screen,black,pygame.Rect(1150,670,55,22))
                screen.blit(exitt,exitbut)
                if pressed1==1:
                    pygame.display.flip()
                    out = False
                    f = -1
                    break
                break
            break
        if f==2:
            if f1==1:
                #Hebbal places selection screen
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                fontbig = pygame.font.Font(None, 70)
                font = pygame.font.Font(None, 80)
                fonts = pygame.font.Font(None, 30)
                fontt = pygame.font.Font(None, 50)
                if c1==0:
                    color1 = white
                    colorr1 = black
                else:
                    color1 = black
                    colorr1 = turq
                if c2==0:
                    color2 = white
                    colorr2 = black
                else:
                    color2 = black
                    colorr2 = turq
                if c3==0:
                    color3 = white
                    colorr3 = black
                else:
                    color3 = black
                    colorr3 = turq
                if c4==0:
                    color4 = white
                    colorr4 = black
                else:
                    color4 = black
                    colorr4 = turq
                lg = fontbig.render("Lumbini Gardens", 10, color1)
                jp = fontbig.render("JP Narayan Park", 10, color2)
                ii = fontbig.render("IISc", 10, color3)
                hl = fontbig.render("Hebbal Lake Park", 10, color4)
                go = font.render("GO ->",10,black)
                ques = font.render("Select the places you want to visit", 10, black)
                lgbt = pygame.draw.rect(screen,colorr1,pygame.Rect(920,535,400,45))
                jpbt = pygame.draw.rect(screen,colorr2,pygame.Rect(120,540,400,45))
                iibt = pygame.draw.rect(screen,colorr3,pygame.Rect(1100,230,95,45))
                hlbt = pygame.draw.rect(screen,colorr4,pygame.Rect(120,230,430,45))
                gobt = pygame.draw.rect(screen,white,pygame.Rect(660,600,150,45))
                quesbt = pygame.draw.rect(screen,white,pygame.Rect(290,85,950,70))
                screen.blit(lg,lgbt)
                screen.blit(jp,jpbt)
                screen.blit(ii,iibt)
                screen.blit(hl,hlbt)
                screen.blit(go,gobt)
                screen.blit(ques,(300,85))
                pygame.draw.line(screen, black, (1100,260),(550,260),7)
                pygame.draw.line(screen, black, (1120,270),(1130,535),7)
                pygame.draw.line(screen, black, (1100,265),(300,540),7)
                pygame.draw.line(screen, black, (380,270),(300,540),7)
                pygame.draw.line(screen, black, (540,270),(1100,537),7)
                pygame.draw.line(screen, black, (505,565),(922,565),7)
                gd1 = fontt.render("7.9km",10,red)
                gd2 = fontt.render("8.6km",10,red)
                gd3 = fontt.render("5.0km",10,red)
                gd4 = fontt.render("5.3km",10,red)
                gd5 = fontt.render("2.0km",10,red)
                gd6 = fontt.render("6.0km",10,red)
                gd1bt = pygame.draw.rect(screen,white,pygame.Rect(720,525,100,40))
                gd2bt = pygame.draw.rect(screen,white,pygame.Rect(1130,350,100,40))
                gd3bt = pygame.draw.rect(screen,white,pygame.Rect(230,350,100,40))
                gd4bt = pygame.draw.rect(screen,white,pygame.Rect(700,215,100,40))
                gd5bt = pygame.draw.rect(screen,white,pygame.Rect(920,340,100,40))
                gd6bt = pygame.draw.rect(screen,white,pygame.Rect(530,330,100,40))
                screen.blit(gd1,gd1bt)
                screen.blit(gd2,gd2bt)
                screen.blit(gd3,gd3bt)
                screen.blit(gd4,gd4bt)
                screen.blit(gd5,gd5bt)
                screen.blit(gd6,gd6bt)
                exitt = fonts.render("EXIT", 10, black)
                exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1150,670,55,22))
                screen.blit(exitt,exitbut)
                back = fonts.render("BACK", 10, black)
                backbut = pygame.draw.rect(screen,turq,pygame.Rect(150,670,55,22))
                screen.blit(back,backbut)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if lgbt.collidepoint(pos):
                    lg = fontbig.render("Lumbini Gardens", 10, black)
                    lgbt = pygame.draw.rect(screen,turq,pygame.Rect(920,535,400,45))
                    screen.blit(lg,lgbt)
                    if pressed1==1:
                        pygame.display.flip()
                        h1=h1+1
                        if h1%2!=0:
                            c1 = 1
                        else:
                            c1 = 0
                        break
                    break
                if jpbt.collidepoint(pos):
                    jp = fontbig.render("JP Narayan Park", 10, black)
                    jpbt = pygame.draw.rect(screen,turq,pygame.Rect(120,540,400,45))
                    screen.blit(jp,jpbt)
                    if pressed1==1:
                        pygame.display.flip()
                        h2=h2+1
                        if h2%2!=0:
                            c2 = 1
                        else:
                            c2 = 0
                        break
                    break
                if iibt.collidepoint(pos):
                    ii = fontbig.render("IISc", 10, black)
                    iibt = pygame.draw.rect(screen,turq,pygame.Rect(1100,230,95,45))
                    screen.blit(ii,iibt)
                    if pressed1==1:
                        pygame.display.flip()
                        h3=h3+1
                        if h3%2!=0:
                            c3 = 1
                        else:
                            c3 = 0
                        break
                    break
                if hlbt.collidepoint(pos):
                    hl = fontbig.render("Hebbal Lake Park", 10, black)
                    hlbt = pygame.draw.rect(screen,turq,pygame.Rect(120,230,430,45))
                    screen.blit(hl,hlbt)
                    if pressed1==1:
                        h4=h4+1
                        if h4%2!=0:
                            c4 = 1
                        else:
                            c4 = 0
                        break
                    break
                if gobt.collidepoint(pos):
                    go = font.render("GO ->",10,black)
                    gobt = pygame.draw.rect(screen,turq,pygame.Rect(660,600,150,45))
                    screen.blit(go,gobt)
                    if pressed1==1:
                        pygame.display.flip()
                        ch = [c1,c2,c3,c4]
                        for i in ch:
                            if i==1:
                                count1+=1
                        if count1==0:
                            f = 3
                            f2 = count1
                            break
                        elif count1==1:
                            f = 3
                            f2 = count1
                            break
                        else:
                            if c1==1 and c2==1 and c3==1 and c4==1:
                                gh = [[999.0, 7.9, 8.6, 6.0],
                                      [7.9, 999.0, 2.0, 5.0],
                                      [8.6, 2.0, 999.0, 5.3],
                                      [6.0, 5.0, 5.3, 999.0]]
                            if c1==1 and c2==1 and c3==1 and c4!=1:
                                gh = [[999.0, 7.9, 8.6],
                                      [7.9, 999.0, 2.0],
                                      [8.6, 2.0, 999.0]]
                            if c1==1 and c2==1 and c3!=1 and c4==1:
                                gh = [[999.0, 7.9, 6.0],
                                      [7.9, 999.0, 5.0],
                                      [6.0, 5.0, 999.0]]
                            if c1==1 and c2!=1 and c3==1 and c4==1:
                                gh = [[999.0, 8.6, 6.0],
                                      [8.6, 999.0, 5.3],
                                      [6.0, 5.3, 999.0]]
                            if c1!=1 and c2==1 and c3==1 and c4==1:
                                gh = [[999.0, 2.0, 5.0],
                                      [2.0, 999.0, 5.3],
                                      [5.0, 5.3, 999.0]]
                            if c1==1 and c2==1 and c3!=1 and c4!=1:
                                gh = [[999.0, 7.9],
                                      [7.9, 999.0]]
                            if c1==1 and c2!=1 and c3==1 and c4!=1:
                                gh = [[999.0, 8.6],
                                      [8.6, 999.0]]
                            if c1==1 and c2!=1 and c3!=1 and c4==1:
                                gh = [[999.0, 6.0],
                                      [6.0, 999.0]]
                            if c1!=1 and c2==1 and c3==1 and c4!=1:
                                gh = [[999.0, 2.0],
                                      [2.0, 999.0]]
                            if c1!=1 and c2==1 and c3!=1 and c4==1:
                                gh = [[999.0, 5.0],
                                      [5.0, 999.0]]
                            if c1!=1 and c2!=1 and c3==1 and c4==1:
                                gh = [[999.0, 5.3],
                                      [5.3,999.0]]
                            f = 3
                            f2 = count1
                            break
                if backbut.collidepoint(pos):
                    back = fonts.render("BACK", 10, white)
                    backbut = pygame.draw.rect(screen,black,pygame.Rect(150,670,55,22))
                    screen.blit(back,backbut)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 1
                        break
                    break
                if exitbut.collidepoint(pos):
                    exitt = fonts.render("EXIT", 10, white)
                    exitbut = pygame.draw.rect(screen,black,pygame.Rect(1150,670,55,22))
                    screen.blit(exitt,exitbut)
                    if pressed1==1:
                        pygame.display.flip()
                        out = False
                        f = -1
                        break
                    break
                break
            if f1==2:
                #Banashankari places selection screen
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                fontbig = pygame.font.Font(None, 70)
                font = pygame.font.Font(None, 80)
                fonts = pygame.font.Font(None, 30)
                fontt = pygame.font.Font(None, 50)
                if cb1==0:
                    color1 = white
                    colorr1 = black
                else:
                    color1 = black
                    colorr1 = turq
                if cb2==0:
                    color2 = white
                    colorr2 = black
                else:
                    color2 = black
                    colorr2 = turq
                if cb3==0:
                    color3 = white
                    colorr3 = black
                else:
                    color3 = black
                    colorr3 = turq
                if cb4==0:
                    color4 = white
                    colorr4 = black
                else:
                    color4 = black
                    colorr4 = turq
                ap = fontbig.render("Ashoka Pillar", 10, color1)
                bt = fontbig.render("Bull Temple", 10, color2)
                lb = fontbig.render("Lalbagh", 10, color3)
                ts = fontbig.render("Tippu Sultan Palace", 10, color4)
                go = font.render("GO ->",10,black)
                ques = font.render("Select the places you want to visit", 10, black)
                apbt = pygame.draw.rect(screen,colorr1,pygame.Rect(920,535,350,45))
                btbt = pygame.draw.rect(screen,colorr2,pygame.Rect(120,540,300,45))
                lbbt = pygame.draw.rect(screen,colorr3,pygame.Rect(1100,230,200,45))
                tsbt = pygame.draw.rect(screen,colorr4,pygame.Rect(60,230,500,45))
                gobt = pygame.draw.rect(screen,white,pygame.Rect(660,600,150,45))
                quesbt = pygame.draw.rect(screen,white,pygame.Rect(290,85,950,70))
                screen.blit(ap,apbt)
                screen.blit(bt,btbt)
                screen.blit(lb,lbbt)
                screen.blit(ts,tsbt)
                screen.blit(go,gobt)
                screen.blit(ques,(300,85))
                pygame.draw.line(screen, black, (1100,260),(550,260),7)
                pygame.draw.line(screen, black, (1120,270),(1130,535),7)
                pygame.draw.line(screen, black, (1100,265),(300,540),7)
                pygame.draw.line(screen, black, (380,270),(300,540),7)
                pygame.draw.line(screen, black, (540,270),(1100,537),7)
                pygame.draw.line(screen, black, (400,565),(922,565),7)
                gd1 = fontt.render("3.4km",10,red)
                gd2 = fontt.render("1.1km",10,red)
                gd3 = fontt.render("2.5km",10,red)
                gd4 = fontt.render("2.5km",10,red)
                gd5 = fontt.render("1.8km",10,red)
                gd6 = fontt.render("3.7km",10,red)
                gd1bt = pygame.draw.rect(screen,white,pygame.Rect(720,525,100,40))
                gd2bt = pygame.draw.rect(screen,white,pygame.Rect(1130,350,100,40))
                gd3bt = pygame.draw.rect(screen,white,pygame.Rect(230,350,100,40))
                gd4bt = pygame.draw.rect(screen,white,pygame.Rect(700,215,100,40))
                gd5bt = pygame.draw.rect(screen,white,pygame.Rect(920,340,100,40))
                gd6bt = pygame.draw.rect(screen,white,pygame.Rect(530,330,100,40))
                screen.blit(gd1,gd1bt)
                screen.blit(gd2,gd2bt)
                screen.blit(gd3,gd3bt)
                screen.blit(gd4,gd4bt)
                screen.blit(gd5,gd5bt)
                screen.blit(gd6,gd6bt)
                exitt = fonts.render("EXIT", 10, black)
                exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1150,670,55,22))
                screen.blit(exitt,exitbut)
                back = fonts.render("BACK", 10, black)
                backbut = pygame.draw.rect(screen,turq,pygame.Rect(150,670,55,22))
                screen.blit(back,backbut)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if apbt.collidepoint(pos):
                    ap = fontbig.render("Ashoka Pillar", 10, black)
                    apbt = pygame.draw.rect(screen,turq,pygame.Rect(920,535,350,45))
                    screen.blit(ap,apbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hb1=hb1+1
                        if hb1%2!=0:
                            cb1 = 1
                        else:
                            cb1 = 0
                        break
                    break
                if btbt.collidepoint(pos):
                    bt = fontbig.render("Bull Temple", 10, black)
                    btbt = pygame.draw.rect(screen,turq,pygame.Rect(120,540,300,45))
                    screen.blit(bt,btbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hb2=hb2+1
                        if hb2%2!=0:
                            cb2 = 1
                        else:
                            cb2 = 0
                        break
                    break
                if lbbt.collidepoint(pos):
                    lb = fontbig.render("Lalbagh", 10, black)
                    lbbt = pygame.draw.rect(screen,turq,pygame.Rect(1100,230,200,45))
                    screen.blit(lb,lbbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hb3=hb3+1
                        if hb3%2!=0:
                            cb3 = 1
                        else:
                            cb3 = 0
                        break
                    break
                if tsbt.collidepoint(pos):
                    ts = fontbig.render("Tippu Sultan Palace", 10, black)
                    tsbt = pygame.draw.rect(screen,turq,pygame.Rect(60,230,500,45))
                    screen.blit(ts,tsbt)
                    if pressed1==1:
                        hb4=hb4+1
                        if hb4%2!=0:
                            cb4 = 1
                        else:
                            cb4 = 0
                        break
                    break
                if gobt.collidepoint(pos):
                    go = font.render("GO ->",10,black)
                    gobt = pygame.draw.rect(screen,turq,pygame.Rect(660,600,150,45))
                    screen.blit(go,gobt)
                    if pressed1==1:
                        pygame.display.flip()
                        chb = [cb1,cb2,cb3,cb4]
                        for i in chb:
                            if i==1:
                                countb1+=1
                        if countb1==0:
                            f = 4
                            f2 = countb1
                            break
                        elif countb1==1:
                            f = 4
                            f2 = countb1
                            break
                        else:
                            if cb1==1 and cb2==1 and cb3==1 and cb4==1:
                                gb = [[999.0, 3.4, 1.1, 3.7],
                                      [3.4, 999.0, 1.8, 2.5],
                                      [1.1, 1.8, 999.0, 2.5],
                                      [3.7, 2.5, 2.5, 999.0]]
                            if cb1==1 and cb2==1 and cb3==1 and cb4!=1:
                                gb = [[999.0, 3.4, 1.1],
                                      [3.4, 999.0, 1.8],
                                      [1.1, 1.8, 999.0]]
                            if cb1==1 and cb2==1 and cb3!=1 and cb4==1:
                                gb = [[999.0, 3.4, 3.7],
                                      [3.4, 999.0, 2.5],
                                      [3.7, 2.5, 999.0]]
                            if cb1==1 and cb2!=1 and cb3==1 and cb4==1:
                                gb = [[999.0, 1.1, 3.7],
                                      [1.1, 999.0, 2.5],
                                      [3.7, 2.5, 999.0]]
                            if cb1!=1 and cb2==1 and cb3==1 and cb4==1:
                                gb = [[999.0, 1.8, 2.5],
                                      [1.8, 999.0, 2.5],
                                      [2.5, 2.5, 999.0]]
                            if cb1==1 and cb2==1 and cb3!=1 and cb4!=1:
                                gb = [[999.0, 3.4],
                                      [3.4, 999.0]]
                            if cb1==1 and cb2!=1 and cb3==1 and cb4!=1:
                                gb = [[999.0, 1.1],
                                      [1.1, 999.0]]
                            if cb1==1 and cb2!=1 and cb3!=1 and cb4==1:
                                gb = [[999.0, 3.7],
                                      [3.7, 999.0]]
                            if cb1!=1 and cb2==1 and cb3==1 and cb4!=1:
                                gb = [[999.0, 1.8],
                                      [1.8, 999.0]]
                            if cb1!=1 and cb2==1 and cb3!=1 and cb4==1:
                                gb = [[999.0, 2.5],
                                      [2.5, 999.0]]
                            if cb1!=1 and cb2!=1 and cb3==1 and cb4==1:
                                gb = [[999.0, 2.5],
                                      [2.5,999.0]]
                            f = 4
                            f2 = countb1
                            break
                if backbut.collidepoint(pos):
                    back = fonts.render("BACK", 10, white)
                    backbut = pygame.draw.rect(screen,black,pygame.Rect(150,670,55,22))
                    screen.blit(back,backbut)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 1
                        break
                    break
                if exitbut.collidepoint(pos):
                    exitt = fonts.render("EXIT", 10, white)
                    exitbut = pygame.draw.rect(screen,black,pygame.Rect(1150,670,55,22))
                    screen.blit(exitt,exitbut)
                    if pressed1==1:
                        pygame.display.flip()
                        out = False
                        f = -1
                        break
                    break
                break
            if f1==3:
                #MG Road places selection screen
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                fontbig = pygame.font.Font(None, 70)
                font = pygame.font.Font(None, 80)
                fonts = pygame.font.Font(None, 30)
                fontt = pygame.font.Font(None, 50)
                font2 = pygame.font.Font(None, 65)
                if cm1==0:
                    color1 = white
                    colorr1 = black
                else:
                    color1 = black
                    colorr1 = turq
                if cm2==0:
                    color2 = white
                    colorr2 = black
                else:
                    color2 = black
                    colorr2 = turq
                if cm3==0:
                    color3 = white
                    colorr3 = black
                else:
                    color3 = black
                    colorr3 = turq
                if cm4==0:
                    color4 = white
                    colorr4 = black
                else:
                    color4 = black
                    colorr4 = turq
                vs = fontbig.render("Vidhana Soudha", 10, color1)
                cb = fontbig.render("Cubbon Park", 10, color2)
                jn = font2.render("Jawaharlal Nehru Planetorium", 10, color3)
                sm = fontbig.render("St.Mary's Basilica", 10, color4)
                go = font.render("GO ->",10,black)
                ques = font.render("Select the places you want to visit", 10, black)
                vsbt = pygame.draw.rect(screen,colorr1,pygame.Rect(880,535,400,45))
                cbbt = pygame.draw.rect(screen,colorr2,pygame.Rect(100,540,335,45))
                jnbt = pygame.draw.rect(screen,colorr3,pygame.Rect(650,230,655,40))
                smbt = pygame.draw.rect(screen,colorr4,pygame.Rect(50,230,430,45))
                gobt = pygame.draw.rect(screen,white,pygame.Rect(660,600,150,45))
                quesbt = pygame.draw.rect(screen,white,pygame.Rect(290,85,950,70))
                screen.blit(vs,vsbt)
                screen.blit(cb,cbbt)
                screen.blit(jn,jnbt)
                screen.blit(sm,smbt)
                screen.blit(go,gobt)
                screen.blit(ques,(300,85))
                pygame.draw.line(screen, black, (650,260),(470,260),7)
                pygame.draw.line(screen, black, (1120,270),(1130,535),7)
                pygame.draw.line(screen, black, (200,265),(300,540),7)
                pygame.draw.line(screen, black, (750,270),(300,540),7)
                pygame.draw.line(screen, black, (480,270),(900,537),7)
                pygame.draw.line(screen, black, (430,565),(890,565),7)
                gd1 = fontt.render("1.3km",10,red)
                gd2 = fontt.render("1.7km",10,red)
                gd3 = fontt.render("2.8km",10,red)
                gd4 = fontt.render("2.2km",10,red)
                gd5 = fontt.render("2.9km",10,red)
                gd6 = fontt.render("2.3km",10,red)
                gd1bt = pygame.draw.rect(screen,white,pygame.Rect(600,523,100,37))
                gd2bt = pygame.draw.rect(screen,white,pygame.Rect(1130,350,100,37))
                gd3bt = pygame.draw.rect(screen,white,pygame.Rect(130,350,100,37))
                gd4bt = pygame.draw.rect(screen,white,pygame.Rect(520,215,100,37))
                gd5bt = pygame.draw.rect(screen,white,pygame.Rect(390,390,100,37))
                gd6bt = pygame.draw.rect(screen,white,pygame.Rect(760,420,100,37))
                screen.blit(gd1,gd1bt)
                screen.blit(gd2,gd2bt)
                screen.blit(gd3,gd3bt)
                screen.blit(gd4,gd4bt)
                screen.blit(gd5,gd5bt)
                screen.blit(gd6,gd6bt)
                exitt = fonts.render("EXIT", 10, black)
                exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1150,670,55,22))
                screen.blit(exitt,exitbut)
                back = fonts.render("BACK", 10, black)
                backbut = pygame.draw.rect(screen,turq,pygame.Rect(150,670,55,22))
                screen.blit(back,backbut)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if vsbt.collidepoint(pos):
                    vs = fontbig.render("Vidhana Soudha", 10, black)
                    vsbt = pygame.draw.rect(screen,turq,pygame.Rect(880,535,400,45))
                    screen.blit(vs,vsbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hm1=hm1+1
                        if hm1%2!=0:
                            cm1 = 1
                        else:
                            cm1 = 0
                        break
                    break
                if cbbt.collidepoint(pos):
                    cb = fontbig.render("Cubbon Park", 10, black)
                    cbbt = pygame.draw.rect(screen,turq,pygame.Rect(100,540,335,45))
                    screen.blit(cb,cbbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hm2=hm2+1
                        if hm2%2!=0:
                            cm2 = 1
                        else:
                            cm2 = 0
                        break
                    break
                if jnbt.collidepoint(pos):
                    jn = font2.render("Jawaharlal Nehru Planetorium", 10, black)
                    jnbt = pygame.draw.rect(screen,turq,pygame.Rect(650,230,655,40))
                    screen.blit(jn,jnbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hm3=hm3+1
                        if hm3%2!=0:
                            cm3 = 1
                        else:
                            cm3 = 0
                        break
                    break
                if smbt.collidepoint(pos):
                    sm = fontbig.render("St.Mary's Basilica", 10, black)
                    smbt = pygame.draw.rect(screen,turq,pygame.Rect(50,230,430,45))
                    screen.blit(sm,smbt)
                    if pressed1==1:
                        hm4=hm4+1
                        if hm4%2!=0:
                            cm4 = 1
                        else:
                            cm4 = 0
                        break
                    break
                if gobt.collidepoint(pos):
                    go = font.render("GO ->",10,black)
                    gobt = pygame.draw.rect(screen,turq,pygame.Rect(660,600,150,45))
                    screen.blit(go,gobt)
                    if pressed1==1:
                        pygame.display.flip()
                        chm = [cm1,cm2,cm3,cm4]
                        for i in chm:
                            if i==1:
                                countm1+=1
                        if countm1==0:
                            f = 5
                            f2 = countm1
                            break
                        elif countm1==1:
                            f = 5
                            f2 = countm1
                            break
                        else:
                            if cm1==1 and cm2==1 and cm3==1 and cm4==1:
                                gm = [[999.0, 1.3, 1.7, 2.3],
                                      [1.3, 999.0, 2.9, 2.8],
                                      [1.7, 2.9, 999.0, 2.2],
                                      [2.3, 2.8, 2.2, 999.0]]
                            if cm1==1 and cm2==1 and cm3==1 and cm4!=1:
                                gm = [[999.0, 1.3, 1.7],
                                      [1.3, 999.0, 2.9],
                                      [1.7, 2.9, 999.0]]
                            if cm1==1 and cm2==1 and cm3!=1 and cm4==1:
                                gm = [[999.0, 1.3, 2.3],
                                      [1.3, 999.0, 2.8],
                                      [2.3, 2.8, 999.0]]
                            if cm1==1 and cm2!=1 and cm3==1 and cm4==1:
                                gm = [[999.0, 1.7, 2.3],
                                      [1.7, 999.0, 2.2],
                                      [2.3, 2.2, 999.0]]
                            if cm1!=1 and cm2==1 and cm3==1 and cm4==1:
                                gm = [[999.0, 2.9, 2.8],
                                      [2.9, 999.0, 2.2],
                                      [2.8, 2.2, 999.0]]
                            if cm1==1 and cm2==1 and cm3!=1 and cm4!=1:
                                gm = [[999.0, 1.3],
                                      [1.3, 999.0]]
                            if cm1==1 and cm2!=1 and cm3==1 and cm4!=1:
                                gm = [[999.0, 1.7],
                                      [1.7, 999.0]]
                            if cm1==1 and cm2!=1 and cm3!=1 and cm4==1:
                                gm = [[999.0, 2.3],
                                      [2.3, 999.0]]
                            if cm1!=1 and cm2==1 and cm3==1 and cm4!=1:
                                gm = [[999.0, 2.9],
                                      [2.9, 999.0]]
                            if cm1!=1 and cm2==1 and cm3!=1 and cm4==1:
                                gm = [[999.0, 2.8],
                                      [2.8, 999.0]]
                            if cm1!=1 and cm2!=1 and cm3==1 and cm4==1:
                                gm = [[999.0, 2.2],
                                      [2.2,999.0]]
                            f = 5
                            f2 = countm1
                            break
                if backbut.collidepoint(pos):
                    back = fonts.render("BACK", 10, white)
                    backbut = pygame.draw.rect(screen,black,pygame.Rect(150,670,55,22))
                    screen.blit(back,backbut)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 1
                        break
                    break
                if exitbut.collidepoint(pos):
                    exitt = fonts.render("EXIT", 10, white)
                    exitbut = pygame.draw.rect(screen,black,pygame.Rect(1150,670,55,22))
                    screen.blit(exitt,exitbut)
                    if pressed1==1:
                        pygame.display.flip()
                        out = False
                        f = -1
                        break
                    break
                break
            if f1==4:
                #Rajajinagar places selection screen
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                fontbig = pygame.font.Font(None, 70)
                font = pygame.font.Font(None, 80)
                fonts = pygame.font.Font(None, 30)
                fontt = pygame.font.Font(None, 50)
                if cr1==0:
                    color1 = white
                    colorr1 = black
                else:
                    color1 = black
                    colorr1 = turq
                if cr2==0:
                    color2 = white
                    colorr2 = black
                else:
                    color2 = black
                    colorr2 = turq
                if cr3==0:
                    color3 = white
                    colorr3 = black
                else:
                    color3 = black
                    colorr3 = turq
                if cr4==0:
                    color4 = white
                    colorr4 = black
                else:
                    color4 = black
                    colorr4 = turq
                bp = fontbig.render("Bangalore Palace", 10, color1)
                st = fontbig.render("Sankey Tank", 10, color2)
                wt = fontbig.render("World Trade Center", 10, color3)
                it = fontbig.render("Iskcon Temple", 10, color4)
                go = font.render("GO ->",10,black)
                ques = font.render("Select the places you want to visit", 10, black)
                bpbt = pygame.draw.rect(screen,colorr1,pygame.Rect(920,535,420,45))
                stbt = pygame.draw.rect(screen,colorr2,pygame.Rect(120,540,300,45))
                wtbt = pygame.draw.rect(screen,colorr3,pygame.Rect(900,230,485,45))
                itbt = pygame.draw.rect(screen,colorr4,pygame.Rect(120,230,350,45))
                gobt = pygame.draw.rect(screen,white,pygame.Rect(660,600,150,45))
                quesbt = pygame.draw.rect(screen,white,pygame.Rect(290,85,950,70))
                screen.blit(bp,bpbt)
                screen.blit(st,stbt)
                screen.blit(wt,wtbt)
                screen.blit(it,itbt)
                screen.blit(go,gobt)
                screen.blit(ques,(300,85))
                pygame.draw.line(screen, black, (900,260),(470,260),7)
                pygame.draw.line(screen, black, (1120,270),(1130,535),7)
                pygame.draw.line(screen, black, (1100,265),(300,540),7)
                pygame.draw.line(screen, black, (380,270),(300,540),7)
                pygame.draw.line(screen, black, (450,260),(1100,537),7)
                pygame.draw.line(screen, black, (420,565),(920,565),7)
                gd1 = fontt.render("3.6km",10,red)
                gd2 = fontt.render("6.4km",10,red)
                gd3 = fontt.render("6.0km",10,red)
                gd4 = fontt.render("1.8km",10,red)
                gd5 = fontt.render("3.8km",10,red)
                gd6 = fontt.render("8.5km",10,red)
                gd1bt = pygame.draw.rect(screen,white,pygame.Rect(720,525,100,37))
                gd2bt = pygame.draw.rect(screen,white,pygame.Rect(1130,350,100,37))
                gd3bt = pygame.draw.rect(screen,white,pygame.Rect(230,350,100,37))
                gd4bt = pygame.draw.rect(screen,white,pygame.Rect(700,215,100,37))
                gd5bt = pygame.draw.rect(screen,white,pygame.Rect(920,340,100,37))
                gd6bt = pygame.draw.rect(screen,white,pygame.Rect(530,330,100,37))
                screen.blit(gd1,gd1bt)
                screen.blit(gd2,gd2bt)
                screen.blit(gd3,gd3bt)
                screen.blit(gd4,gd4bt)
                screen.blit(gd5,gd5bt)
                screen.blit(gd6,gd6bt)
                exitt = fonts.render("EXIT", 10, black)
                exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1150,670,55,22))
                screen.blit(exitt,exitbut)
                back = fonts.render("BACK", 10, black)
                backbut = pygame.draw.rect(screen,turq,pygame.Rect(150,670,55,22))
                screen.blit(back,backbut)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if bpbt.collidepoint(pos):
                    bp = fontbig.render("Bangalore Palace", 10, black)
                    bpbt = pygame.draw.rect(screen,turq,pygame.Rect(920,535,420,45))
                    screen.blit(bp,bpbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hr1=hr1+1
                        if hr1%2!=0:
                            cr1 = 1
                        else:
                            cr1 = 0
                        break
                    break
                if stbt.collidepoint(pos):
                    st = fontbig.render("Sankey Tank", 10, black)
                    stbt = pygame.draw.rect(screen,turq,pygame.Rect(120,540,300,45))
                    screen.blit(st,stbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hr2=hr2+1
                        if hr2%2!=0:
                            cr2 = 1
                        else:
                            cr2 = 0
                        break
                    break
                if wtbt.collidepoint(pos):
                    wt = fontbig.render("World Trade Center", 10, black)
                    wtbt = pygame.draw.rect(screen,turq,pygame.Rect(900,230,485,45))
                    screen.blit(wt,wtbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hr3=hr3+1
                        if hr3%2!=0:
                            cr3 = 1
                        else:
                            cr3 = 0
                        break
                    break
                if itbt.collidepoint(pos):
                    it = fontbig.render("Iskcon Temple", 10, black)
                    itbt = pygame.draw.rect(screen,turq,pygame.Rect(120,230,350,45))
                    screen.blit(it,itbt)
                    if pressed1==1:
                        hr4=hr4+1
                        if hr4%2!=0:
                            cr4 = 1
                        else:
                            cr4 = 0
                        break
                    break
                if gobt.collidepoint(pos):
                    go = font.render("GO ->",10,black)
                    gobt = pygame.draw.rect(screen,turq,pygame.Rect(660,600,150,45))
                    screen.blit(go,gobt)
                    if pressed1==1:
                        pygame.display.flip()
                        chrr = [cr1,cr2,cr3,cr4]
                        for i in chrr:
                            if i==1:
                                countr1+=1
                        if countr1==0:
                            f = 6
                            f2 = countr1
                            break
                        elif countr1==1:
                            f = 6
                            f2 = countr1
                            break
                        else:
                            if cr1==1 and cr2==1 and cr3==1 and cr4==1:
                                gr = [[999.0, 3.6, 6.4, 8.5],
                                      [3.6, 999.0, 3.8, 6.0],
                                      [6.4, 3.8, 999.0, 1.8],
                                      [8.6, 6.0, 1.8, 999.0]]
                            if cr1==1 and cr2==1 and cr3==1 and cr4!=1:
                                gr = [[999.0, 3.6, 6.4],
                                      [3.6, 999.0, 3.8],
                                      [6.4, 3.8, 999.0]]
                            if cr1==1 and cr2==1 and cr3!=1 and cr4==1:
                                gr = [[999.0, 3.6, 8.5],
                                      [3.6, 999.0, 6.0],
                                      [8.6, 6.0, 999.0]]
                            if cr1==1 and cr2!=1 and cr3==1 and cr4==1:
                                gr = [[999.0, 6.4, 8.5],
                                      [6.4, 999.0, 1.8],
                                      [8.6, 1.8, 999.0]]
                            if cr1!=1 and cr2==1 and cr3==1 and cr4==1:
                                gr = [[999.0, 3.8, 6.0],
                                      [3.8, 999.0, 1.8],
                                      [6.0, 1.8, 999.0]]
                            if cr1==1 and cr2==1 and cr3!=1 and cr4!=1:
                                gr = [[999.0, 3.6],
                                      [3.6, 999.0]]
                            if cr1==1 and cr2!=1 and cr3==1 and cr4!=1:
                                gr = [[999.0, 6.4],
                                      [6.4, 999.0]]
                            if cr1==1 and cr2!=1 and cr3!=1 and cr4==1:
                                gr = [[999.0, 8.5],
                                      [8.5, 999.0]]
                            if cr1!=1 and cr2==1 and cr3==1 and cr4!=1:
                                gr = [[999.0, 3.8],
                                      [3.8, 999.0]]
                            if cr1!=1 and cr2==1 and cr3!=1 and cr4==1:
                                gr = [[999.0, 6.0],
                                      [6.0, 999.0]]
                            if cr1!=1 and cr2!=1 and cr3==1 and cr4==1:
                                gr = [[999.0, 1.8],
                                      [1.8, 999.0]]
                            f = 6
                            f2 = countr1
                            break
                if backbut.collidepoint(pos):
                    back = fonts.render("BACK", 10, white)
                    backbut = pygame.draw.rect(screen,black,pygame.Rect(150,670,55,22))
                    screen.blit(back,backbut)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 1
                        break
                    break
                if exitbut.collidepoint(pos):
                    exitt = fonts.render("EXIT", 10, white)
                    exitbut = pygame.draw.rect(screen,black,pygame.Rect(1150,670,55,22))
                    screen.blit(exitt,exitbut)
                    if pressed1==1:
                        pygame.display.flip()
                        out = False
                        f = -1
                        break
                    break
                break
            if f1==5:
                #Majestic places selection screen
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                fontbig = pygame.font.Font(None, 70)
                font = pygame.font.Font(None, 80)
                fonts = pygame.font.Font(None, 30)
                fontt = pygame.font.Font(None, 50)
                if cj1==0:
                    color1 = white
                    colorr1 = black
                else:
                    color1 = black
                    colorr1 = turq
                if cj2==0:
                    color2 = white
                    colorr2 = black
                else:
                    color2 = black
                    colorr2 = turq
                if cj3==0:
                    color3 = white
                    colorr3 = black
                else:
                    color3 = black
                    colorr3 = turq
                if cj4==0:
                    color4 = white
                    colorr4 = black
                else:
                    color4 = black
                    colorr4 = turq
                kr = fontbig.render("KR Market", 10, color1)
                fp = fontbig.render("Freedom Park", 10, color2)
                ms = fontbig.render("Mantri Square", 10, color3)
                rc = fontbig.render("Race Course", 10, color4)
                go = font.render("GO ->",10,black)
                ques = font.render("Select the places you want to visit", 10, black)
                krbt = pygame.draw.rect(screen,colorr1,pygame.Rect(920,535,300,45))
                fpbt = pygame.draw.rect(screen,colorr2,pygame.Rect(120,540,350,45))
                msbt = pygame.draw.rect(screen,colorr3,pygame.Rect(900,230,370,45))
                rcbt = pygame.draw.rect(screen,colorr4,pygame.Rect(120,230,330,45))
                gobt = pygame.draw.rect(screen,white,pygame.Rect(660,600,150,45))
                quesbt = pygame.draw.rect(screen,white,pygame.Rect(290,85,950,70))
                screen.blit(kr,krbt)
                screen.blit(fp,fpbt)
                screen.blit(ms,msbt)
                screen.blit(rc,rcbt)
                screen.blit(go,gobt)
                screen.blit(ques,(300,85))
                pygame.draw.line(screen, black, (900,260),(450,260),7)
                pygame.draw.line(screen, black, (1120,270),(1130,535),7)
                pygame.draw.line(screen, black, (1100,265),(300,540),7)
                pygame.draw.line(screen, black, (380,270),(300,540),7)
                pygame.draw.line(screen, black, (500,265),(1100,537),7)
                pygame.draw.line(screen, black, (470,565),(922,565),7)
                gd1 = fontt.render("1.3km",10,red)
                gd2 = fontt.render("5.1km",10,red)
                gd3 = fontt.render("2.2km",10,red)
                gd4 = fontt.render("3.3km",10,red)
                gd5 = fontt.render("3.7km",10,red)
                gd6 = fontt.render("4.9km",10,red)
                gd1bt = pygame.draw.rect(screen,white,pygame.Rect(720,525,100,37))
                gd2bt = pygame.draw.rect(screen,white,pygame.Rect(1130,350,100,37))
                gd3bt = pygame.draw.rect(screen,white,pygame.Rect(230,350,100,37))
                gd4bt = pygame.draw.rect(screen,white,pygame.Rect(700,215,100,37))
                gd5bt = pygame.draw.rect(screen,white,pygame.Rect(920,340,100,37))
                gd6bt = pygame.draw.rect(screen,white,pygame.Rect(530,330,100,37))
                screen.blit(gd1,gd1bt)
                screen.blit(gd2,gd2bt)
                screen.blit(gd3,gd3bt)
                screen.blit(gd4,gd4bt)
                screen.blit(gd5,gd5bt)
                screen.blit(gd6,gd6bt)
                exitt = fonts.render("EXIT", 10, black)
                exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1150,670,55,22))
                screen.blit(exitt,exitbut)
                back = fonts.render("BACK", 10, black)
                backbut = pygame.draw.rect(screen,turq,pygame.Rect(150,670,55,22))
                screen.blit(back,backbut)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if krbt.collidepoint(pos):
                    kr = fontbig.render("KR Market", 10, black)
                    krbt = pygame.draw.rect(screen,turq,pygame.Rect(920,535,300,45))
                    screen.blit(kr,krbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hj1=hj1+1
                        if hj1%2!=0:
                            cj1 = 1
                        else:
                            cj1 = 0
                        break
                    break
                if fpbt.collidepoint(pos):
                    fp = fontbig.render("Freedom Park", 10, black)
                    fpbt = pygame.draw.rect(screen,turq,pygame.Rect(120,540,400,45))
                    screen.blit(fp,fpbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hj2=hj2+1
                        if hj2%2!=0:
                            cj2 = 1
                        else:
                            cj2 = 0
                        break
                    break
                if msbt.collidepoint(pos):
                    ms = fontbig.render("Mantri Square", 10, black)
                    msbt = pygame.draw.rect(screen,turq,pygame.Rect(1100,230,95,45))
                    screen.blit(ms,msbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hj3=hj3+1
                        if hj3%2!=0:
                            cj3 = 1
                        else:
                            cj3 = 0
                        break
                    break
                if rcbt.collidepoint(pos):
                    rc = fontbig.render("Race Course", 10, black)
                    rcbt = pygame.draw.rect(screen,turq,pygame.Rect(120,230,330,45))
                    screen.blit(rc,rcbt)
                    if pressed1==1:
                        hj4=hj4+1
                        if hj4%2!=0:
                            cj4 = 1
                        else:
                            cj4 = 0
                        break
                    break
                if gobt.collidepoint(pos):
                    go = font.render("GO ->",10,black)
                    gobt = pygame.draw.rect(screen,turq,pygame.Rect(660,600,150,45))
                    screen.blit(go,gobt)
                    if pressed1==1:
                        pygame.display.flip()
                        chj = [cj1,cj2,cj3,cj4]
                        for i in chj:
                            if i==1:
                                countj1+=1
                        if countj1==0:
                            f = 7
                            f2 = countj1
                            break
                        elif countj1==1:
                            f = 7
                            f2 = countj1
                            break
                        else:
                            if cj1==1 and cj2==1 and cj3==1 and cj4==1:
                                gj = [[999.0, 1.3, 5.1, 4.9],
                                      [1.3, 999.0, 3.7, 2.2],
                                      [5.1, 3.7, 999.0, 3.3],
                                      [4.9, 2.2, 3.3, 999.0]]
                            if cj1==1 and cj2==1 and cj3==1 and cj4!=1:
                                gj = [[999.0, 1.3, 5.1],
                                      [1.3, 999.0, 3.7],
                                      [5.1, 3.7, 999.0]]
                            if cj1==1 and cj2==1 and cj3!=1 and cj4==1:
                                gj = [[999.0, 1.3, 4.9],
                                      [1.3, 999.0, 2.2],
                                      [4.9, 2.2, 999.0]]
                            if cj1==1 and cj2!=1 and cj3==1 and cj4==1:
                                gj = [[999.0, 5.1, 4.9],
                                      [5.1, 999.0, 3.3],
                                      [4.9, 3.3, 999.0]]
                            if cj1!=1 and cj2==1 and cj3==1 and cj4==1:
                                gj = [[999.0, 3.7, 2.2],
                                      [3.7, 999.0, 3.3],
                                      [2.2, 3.3, 999.0]]
                            if cj1==1 and cj2==1 and cj3!=1 and cj4!=1:
                                gj = [[999.0, 1.3],
                                      [1.3, 999.0]]
                            if cj1==1 and cj2!=1 and cj3==1 and cj4!=1:
                                gj = [[999.0, 5.1],
                                      [5.1, 999.0]]
                            if cj1==1 and cj2!=1 and cj3!=1 and cj4==1:
                                gj = [[999.0, 4.9],
                                      [4.9, 999.0]]
                            if cj1!=1 and cj2==1 and cj3==1 and cj4!=1:
                                gj = [[999.0, 3.7],
                                      [3.7, 999.0]]
                            if cj1!=1 and cj2==1 and cj3!=1 and cj4==1:
                                gj = [[999.0, 2.2],
                                      [2.2, 999.0]]
                            if cj1!=1 and cj2!=1 and cj3==1 and cj4==1:
                                gj = [[999.0, 3.3],
                                      [3.3,999.0]]
                            f = 7
                            f2 = countj1
                            break
                exitt = fonts.render("EXIT", 10, black)
                exitbut = pygame.draw.rect(screen,turq,pygame.Rect(1150,670,55,22))
                screen.blit(exitt,exitbut)
                back = fonts.render("BACK", 10, black)
                backbut = pygame.draw.rect(screen,turq,pygame.Rect(150,670,55,22))
                screen.blit(back,backbut)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backbut.collidepoint(pos):
                    back = fonts.render("BACK", 10, white)
                    backbut = pygame.draw.rect(screen,black,pygame.Rect(150,670,55,22))
                    screen.blit(back,backbut)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 1
                        break
                    break
                if exitbut.collidepoint(pos):
                    exitt = fonts.render("EXIT", 10, white)
                    exitbut = pygame.draw.rect(screen,black,pygame.Rect(1150,670,55,22))
                    screen.blit(exitt,exitbut)
                    if pressed1==1:
                        pygame.display.flip()
                        out = False
                        f = -1
                        break
                    break
                break
            break
        if f==3:
            #Hebbal Dijkstra result screen
            fontbig = pygame.font.Font(None, 100)
            font = pygame.font.Font(None, 80)
            fonts = pygame.font.Font(None, 30)
            fontt = pygame.font.Font(None, 50)
            if f2==0:
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                err1 = fontbig.render("Please select atleast two places to visit",10,red)
                err1bt = pygame.draw.rect(screen,white,pygame.Rect(30,200,1350,90))
                screen.blit(err1,(30,200))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 1
                        break
                    break
                break
            if f2==1:
                screen.fill((100,100,100))
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                disp1 = fontbig.render("You have chosen only one place",10,black)
                screen.blit(disp1,(200,275))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                h1 = h2 = h3 = h4 = 0
                c1 = c2 = c3 = c4 = 0
                count1 = 0
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 1
                        f2 = 0
                        break
                    break
                break
            if f2>1:
                screen.fill(brown)
                pl = "Places chosen : "
                srcstr = "Starting point : "
                sh = "Shortest path : "
                d1 = "Distance by bus route : "
                pltxt = fontt.render(pl,10,black)
                srctxt = fontt.render(srcstr,10,black)
                shtxt = fontt.render(sh,10,black)
                d1txt = fontt.render(d1,10,black)
                screen.blit(pltxt,(100,100))
                screen.blit(srctxt,(100,220))
                screen.blit(shtxt,(100,350))
                screen.blit(d1txt,(100,600))
                nextt = font.render("NEXT",10, white)
                nexttbt = pygame.draw.rect(screen, black,pygame.Rect(1000,600,160,50))
                screen.blit(nextt,nexttbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                for i in range(4):
                    j = 0
                    if ch[i]==1:
                        srcs[i] = j
                        j += 1
                        srcname = hnames[i]
                        break
                src = srcs[0]
                djheb = dijkstra(gh,f2,src,f2)
                for i in range(4):
                    if ch[i]==1:
                        chp.append(i)
                for i in djheb:
                    if bh==1:
                        a = chp[i]
                        hnames2.append(hnames[a])
                bh = 0
                hh = 0
                #printing shortest path
                for i in range(len(hnames2)):
                    if i==len(hnames2)-1:
                        screen.blit(fontt.render(hnames2[i],10,black),(400,350+hh))
                    else:
                        screen.blit(fontt.render(hnames2[i]+"->",10,black),(400,350+hh))
                    hh = hh + 50  
                #printing chosen places
                for i in range(4):
                    if ch[i]==1:
                        chpl.append(hnames[i])
                if ah==1:
                    for i in range(len(djheb)):
                        chpl2 = chpl2 + chpl[i] + ","
                    ah = 0
                chpl2 = chpl2.rstrip(", ")
                screen.blit(fontt.render(chpl2,10,black),(400,100))
                source1 = fontt.render(srcname,10,black)
                screen.blit(source1,(400,220))
                #printing distance travelled
                dt = distance(gh,djheb)
                dtt = fontt.render(str(dt) + "kms",10,black)
                screen.blit(dtt,(550,600))
                if nexttbt.collidepoint(pos):
                    nextt = font.render("NEXT", 10, black)
                    nexttbt = pygame.draw.rect(screen,turq,pygame.Rect(1000,600,160,50))
                    screen.blit(nextt,nexttbt)
                    if pressed1==1:
                        pygame.display.flip()
                        h1 = h2 = h3 = h4 = 0
                        c1 = c2 = c3 = c4 = 0
                        ah = bh = 1
                        hnames2 = []
                        chpl = []
                        chp = []
                        chpl2 = ""
                        count1 = 0
                        f = 1
                        f1 = 1
                        f2 = 0
                        break
                    break
                break
            break
        if f==4:
            #Banashankari Dijkstra result screen
            fontbig = pygame.font.Font(None, 100)
            font = pygame.font.Font(None, 80)
            fonts = pygame.font.Font(None, 30)
            fontt = pygame.font.Font(None, 50)
            if f2==0:
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                err1 = fontbig.render("Please select atleast two places to visit",10,red)
                err1bt = pygame.draw.rect(screen,white,pygame.Rect(30,200,1350,90))
                screen.blit(err1,(30,200))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 2
                        break
                    break
                break
            if f2==1:
                screen.fill((100,100,100))
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                disp1 = fontbig.render("You have chosen only one place",10,black)
                screen.blit(disp1,(200,275))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                hb1 = hb2 = hb3 = hb4 = 0
                cb1 = cb2 = cb3 = cb4 = 0
                countb1 = 0
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 2
                        f2 = 0
                        break
                    break
                break
            if f2>1:
                screen.fill(brown)
                pl = "Places chosen : "
                srcstr = "Starting point : "
                sh = "Shortest path : "
                d1 = "Distance by bus route : "
                pltxt = fontt.render(pl,10,black)
                srctxt = fontt.render(srcstr,10,black)
                shtxt = fontt.render(sh,10,black)
                d1txt = fontt.render(d1,10,black)
                screen.blit(pltxt,(100,100))
                screen.blit(srctxt,(100,220))
                screen.blit(shtxt,(100,350))
                screen.blit(d1txt,(100,600))
                nextt = font.render("NEXT",10, white)
                nexttbt = pygame.draw.rect(screen, black,pygame.Rect(1000,600,160,50))
                screen.blit(nextt,nexttbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                for i in range(4):
                    j = 0
                    if chb[i]==1:
                        srcs2[i] = j
                        j += 1
                        srcname = bnames[i]
                        break
                src = srcs2[0]
                djban = dijkstra(gb,f2,src,f2)
                for i in range(4):
                    if chb[i]==1:
                        chpb.append(i)
                for i in djban:
                    if bb==1:
                        a = chpb[i]
                        bnames2.append(bnames[a])
                bb = 0
                hh = 0
                #printing shortest path
                for i in range(len(bnames2)):
                    if i==len(bnames2)-1:
                        screen.blit(fontt.render(bnames2[i],10,black),(400,350+hh))
                    else:
                        screen.blit(fontt.render(bnames2[i]+"->",10,black),(400,350+hh))
                    hh = hh + 50  
                #printing chosen places
                for i in range(4):
                    if chb[i]==1:
                        chplb.append(bnames[i])
                if ab==1:
                    for i in range(len(djban)):
                        chplb2 = chplb2 + chplb[i] + ","
                    ab = 0
                chplb2 = chplb2.rstrip(", ")
                screen.blit(fontt.render(chplb2,10,black),(400,100))
                source1 = fontt.render(srcname,10,black)
                screen.blit(source1,(400,220))
                #printing distance travelled
                dt = distance(gb,djban)
                dtt = fontt.render(str(dt) + "kms",10,black)
                screen.blit(dtt,(550,600))
                if nexttbt.collidepoint(pos):
                    nextt = font.render("NEXT", 10, black)
                    nexttbt = pygame.draw.rect(screen,turq,pygame.Rect(1000,600,160,50))
                    screen.blit(nextt,nexttbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hb1 = hb2 = hb3 = hb4 = 0
                        cb1 = cb2 = cb3 = cb4 = 0
                        ab = bb = 1
                        bnames2 = []
                        chplb = []
                        chpb = []
                        chplb2 = ""
                        countb1 = 0
                        f = 1
                        f1 = 1
                        f2 = 0
                        break
                    break
                break
            break
        if f==5:
            #MG Road Dijkstra result screen
            fontbig = pygame.font.Font(None, 100)
            font = pygame.font.Font(None, 80)
            fonts = pygame.font.Font(None, 30)
            fontt = pygame.font.Font(None, 50)
            if f2==0:
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                err1 = fontbig.render("Please select atleast two places to visit",10,red)
                err1bt = pygame.draw.rect(screen,white,pygame.Rect(30,200,1350,90))
                screen.blit(err1,(30,200))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 3
                        break
                    break
                break
            if f2==1:
                screen.fill((100,100,100))
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                disp1 = fontbig.render("You have chosen only one place",10,black)
                screen.blit(disp1,(200,275))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                hm1 = hm2 = hm3 = hm4 = 0
                cm1 = cm2 = cm3 = cm4 = 0
                countm1 = 0
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 3
                        f2 = 0
                        break
                    break
                break
            if f2>1:
                screen.fill(brown)
                pl = "Places chosen : "
                srcstr = "Starting point : "
                sh = "Shortest path : "
                d1 = "Distance by bus route : "
                pltxt = fontt.render(pl,10,black)
                srctxt = fontt.render(srcstr,10,black)
                shtxt = fontt.render(sh,10,black)
                d1txt = fontt.render(d1,10,black)
                screen.blit(pltxt,(100,100))
                screen.blit(srctxt,(100,220))
                screen.blit(shtxt,(100,350))
                screen.blit(d1txt,(100,600))
                nextt = font.render("NEXT",10, white)
                nexttbt = pygame.draw.rect(screen, black,pygame.Rect(1000,600,160,50))
                screen.blit(nextt,nexttbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                for i in range(4):
                    j = 0
                    if chm[i]==1:
                        srcs3[i] = j
                        j += 1
                        srcname = mnames[i]
                        break
                src = srcs3[0]
                djmg = dijkstra(gm,f2,src,f2)
                for i in range(4):
                    if chm[i]==1:
                        chpm.append(i)
                for i in djmg:
                    if bm==1:
                        a = chpm[i]
                        mnames2.append(mnames[a])
                bm = 0
                hh = 0
                #printing shortest path
                for i in range(len(mnames2)):
                    if i==len(mnames2)-1:
                        screen.blit(fontt.render(mnames2[i],10,black),(400,350+hh))
                    else:
                        screen.blit(fontt.render(mnames2[i]+"->",10,black),(400,350+hh))
                    hh = hh + 50  
                #printing chosen places
                for i in range(4):
                    if chm[i]==1:
                        chplm.append(mnames[i])
                if am==1:
                    for i in range(len(djmg)):
                        chplm2 = chplm2 + chplm[i] + ","
                    am = 0
                chplm2 = chplm2.rstrip(", ")
                screen.blit(fontt.render(chplm2,10,black),(400,100))
                source1 = fontt.render(srcname,10,black)
                screen.blit(source1,(400,220))
                #printing distance travelled
                dt = distance(gm,djmg)
                dtt = fontt.render(str(dt) + "kms",10,black)
                screen.blit(dtt,(550,600))
                if nexttbt.collidepoint(pos):
                    nextt = font.render("NEXT", 10, black)
                    nexttbt = pygame.draw.rect(screen,turq,pygame.Rect(1000,600,160,50))
                    screen.blit(nextt,nexttbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hm1 = hm2 = hm3 = hm4 = 0
                        cm1 = cm2 = cm3 = cm4 = 0
                        countm1 = 0
                        am = bm = 1
                        mnames2 = []
                        chplm = []
                        chpm = []
                        chplm2 = ""
                        f = 1
                        f1 = 1
                        f2 = 0
                        break
                    break
                break
            break
        if f==6:
            #Rajajinagar Dijkstra result screen
            fontbig = pygame.font.Font(None, 100)
            font = pygame.font.Font(None, 80)
            fonts = pygame.font.Font(None, 30)
            fontt = pygame.font.Font(None, 50)
            if f2==0:
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                err1 = fontbig.render("Please select atleast two places to visit",10,red)
                err1bt = pygame.draw.rect(screen,white,pygame.Rect(30,200,1350,90))
                screen.blit(err1,(30,200))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 4
                        break
                    break
                break
            if f2==1:
                screen.fill((100,100,100))
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                disp1 = fontbig.render("You have chosen only one place",10,black)
                screen.blit(disp1,(200,275))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                hr1 = hr2 = hr3 = hr4 = 0
                cr1 = cr2 = cr3 = cr4 = 0
                countr1 = 0
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 4
                        f2 = 0
                        break
                    break
                break
            if f2>1:
                screen.fill(brown)
                pl = "Places chosen : "
                srcstr = "Starting point : "
                sh = "Shortest path : "
                d1 = "Distance by bus route : "
                pltxt = fontt.render(pl,10,black)
                srctxt = fontt.render(srcstr,10,black)
                shtxt = fontt.render(sh,10,black)
                d1txt = fontt.render(d1,10,black)
                screen.blit(pltxt,(100,100))
                screen.blit(srctxt,(100,220))
                screen.blit(shtxt,(100,350))
                screen.blit(d1txt,(100,600))
                nextt = font.render("NEXT",10, white)
                nexttbt = pygame.draw.rect(screen, black,pygame.Rect(1000,600,160,50))
                screen.blit(nextt,nexttbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                for i in range(4):
                    j = 0
                    if chrr[i]==1:
                        srcs4[i] = j
                        j += 1
                        srcname = rnames[i]
                        break
                src = srcs4[0]
                djraj = dijkstra(gr,f2,src,f2)
                for i in range(4):
                    if chrr[i]==1:
                        chpr.append(i)
                for i in djraj:
                    if br==1:
                        a = chpr[i]
                        rnames2.append(rnames[a])
                br = 0
                hh = 0
                #printing shortest path
                for i in range(len(rnames2)):
                    if i==len(rnames2)-1:
                        screen.blit(fontt.render(rnames2[i],10,black),(400,350+hh))
                    else:
                        screen.blit(fontt.render(rnames2[i]+"->",10,black),(400,350+hh))
                    hh = hh + 50  
                #printing chosen places
                for i in range(4):
                    if chrr[i]==1:
                        chplr.append(rnames[i])
                if ar==1:
                    for i in range(len(djraj)):
                        chplr2 = chplr2 + chplr[i] + ","
                    ar = 0
                chplr2 = chplr2.rstrip(", ")
                screen.blit(fontt.render(chplr2,10,black),(400,100))
                source1 = fontt.render(srcname,10,black)
                screen.blit(source1,(400,220))
                #printing distance travelled
                dt = distance(gr,djraj)
                dtt = fontt.render(str(dt) + "kms",10,black)
                screen.blit(dtt,(550,600))
                if nexttbt.collidepoint(pos):
                    nextt = font.render("NEXT", 10, black)
                    nexttbt = pygame.draw.rect(screen,turq,pygame.Rect(1000,600,160,50))
                    screen.blit(nextt,nexttbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hr1 = hr2 = hr3 = hr4 = 0
                        cr1 = cr2 = cr3 = cr4 = 0
                        ar = br = 1
                        rnames2 = []
                        chplr = []
                        chpr = []
                        chplr2 = ""
                        countr1 = 0
                        f = 1
                        f1 = 1
                        f2 = 0
                        break
                    break
                break
            break
        if f==7:
            #Majestic Dijkstra result screen
            fontbig = pygame.font.Font(None, 100)
            font = pygame.font.Font(None, 80)
            fonts = pygame.font.Font(None, 30)
            fontt = pygame.font.Font(None, 50)
            if f2==0:
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                err1 = fontbig.render("Please select atleast two places to visit",10,red)
                err1bt = pygame.draw.rect(screen,white,pygame.Rect(30,200,1350,90))
                screen.blit(err1,(30,200))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 5
                        break
                    break
                break
            if f2==1:
                screen.fill((100,100,100))
                screen.fill(white)
                mappRect = mapp.get_rect()
                size = (w,h) = mapp.get_size()
                x,y = screen.get_size()
                screen.blit(mapp,(0,0))
                disp1 = fontbig.render("You have chosen only one place",10,black)
                screen.blit(disp1,(200,275))
                backk = font.render("BACK",10, white)
                backkbt = pygame.draw.rect(screen, black,pygame.Rect(660,550,160,50))
                screen.blit(backk,backkbt)
                hj1 = hj2 = hj3 = hj4 = 0
                cj1 = cj2 = cj3 = cj4 = 0
                countj1 = 0
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                if backkbt.collidepoint(pos):
                    backk = font.render("BACK", 10, black)
                    backkbt = pygame.draw.rect(screen,turq,pygame.Rect(660,550,160,50))
                    screen.blit(backk,backkbt)
                    if pressed1==1:
                        pygame.display.flip()
                        f = 2
                        f1 = 5
                        f2 = 0
                        break
                    break
                break
            if f2>1:
                screen.fill(brown)
                pl = "Places chosen : "
                srcstr = "Starting point : "
                sh = "Shortest path : "
                d1 = "Distance by bus route : "
                pltxt = fontt.render(pl,10,black)
                srctxt = fontt.render(srcstr,10,black)
                shtxt = fontt.render(sh,10,black)
                d1txt = fontt.render(d1,10,black)
                screen.blit(pltxt,(100,100))
                screen.blit(srctxt,(100,220))
                screen.blit(shtxt,(100,350))
                screen.blit(d1txt,(100,600))
                nextt = font.render("NEXT",10, white)
                nexttbt = pygame.draw.rect(screen, black,pygame.Rect(1000,600,160,50))
                screen.blit(nextt,nexttbt)
                pos = pygame.mouse.get_pos()
                (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
                for i in range(4):
                    j = 0
                    if chj[i]==1:
                        srcs5[i] = j
                        j += 1
                        srcname = jnames[i]
                        break
                src = srcs5[0]
                djmaj = dijkstra(gj,f2,src,f2)
                for i in range(4):
                    if chj[i]==1:
                        chpj.append(i)
                for i in djmaj:
                    if bj==1:
                        a = chpj[i]
                        jnames2.append(jnames[a])
                bj = 0
                hh = 0
                #printing shortest path
                for i in range(len(jnames2)):
                    if i==len(jnames2)-1:
                        screen.blit(fontt.render(jnames2[i],10,black),(400,350+hh))
                    else:
                        screen.blit(fontt.render(jnames2[i]+"->",10,black),(400,350+hh))
                    hh = hh + 50  
                #printing chosen places
                for i in range(4):
                    if chj[i]==1:
                        chplj.append(jnames[i])
                if aj==1:
                    for i in range(len(djmaj)):
                        chplj2 = chplj2 + chplj[i] + ", "
                    aj = 0
                chplj2 = chplj2.rstrip(", ")
                screen.blit(fontt.render(chplj2,10,black),(400,100))
                source1 = fontt.render(srcname,10,black)
                screen.blit(source1,(400,220))
                #printing distance travelled
                dt = distance(gj,djmaj)
                dtt = fontt.render(str(dt) + "kms",10,black)
                screen.blit(dtt,(550,600))
                if nexttbt.collidepoint(pos):
                    nextt = font.render("NEXT", 10, black)
                    nexttbt = pygame.draw.rect(screen,turq,pygame.Rect(1000,600,160,50))
                    screen.blit(nextt,nexttbt)
                    if pressed1==1:
                        pygame.display.flip()
                        hj1 = hj2 = hj3 = hj4 = 0
                        cj1 = cj2 = cj3 = cj4 = 0
                        aj = bj = 1
                        jnames2 = []
                        chplj = []
                        chpj = []
                        chplj2 = ""
                        countj1 = 0
                        f = 1
                        f1 = 1
                        f2 = 0
                        break
                    break
                break
            break
    pygame.display.flip()
pygame.quit()
