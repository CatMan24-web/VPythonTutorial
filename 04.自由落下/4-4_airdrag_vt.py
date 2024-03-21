"""
 VPython教學: 4-4.自由落下, 有空氣阻力, 求終端速度
 Ver. 1: 2018/3/8
 Ver. 2: 2019/2/2
 Ver. 3: 2019/9/6
 Ver. 4: 2024/3/21 修改 while 迴圈的停止條件，修改參數減少程式運作時間
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
r = 1        # 小球半徑
m = 0.1      # 小球質量
h = 0        # 小球離地高度
g = 9.8      # 重力加速度 9.8 m/s^2
b = 0.1      # 空氣阻力 f=-bv
c1, c2 = color.red, color.green
t = 0        # 時間
dt = 0.001   # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title="Terminal Velocity", width=400, height=400, x=0, y=0, center=vec(0, h/2, 0), background=vec(0, 0.6, 0.6))

# b1 with air drag, b2 without air drag 
b1 = sphere(pos=vec(2*r, h, 0), radius=r, color=c1, v=vec(0, 0, 0), a=vec(0, -g, 0))
b2 = sphere(pos=vec(-2*r, h, 0), radius=r, color=c2, v=vec(0, 0, 0), a=vec(0, -g, 0))

gd = graph(title="<i>y</i> - <i>t</i> plot", width=600, height=450, x=0, y=400,
           xtitle="<i>t</i> (s)", ytitle="<i>y</i> (m)", fast=False)
gd2 = graph(title="<i>v</i> - <i>t</i> plot", width=600, height=450, x=0, y=700,
            xtitle="<i>t</i> (s)", ytitle="<i>v</i> (m/s)", fast=False)
gd3 = graph(title="<i>a</i> - <i>t</i> plot", width=600, height=450, x=0, y=1000,
            xtitle="<i>t</i> (s)", ytitle="<i>a</i> (m/s<sup>2</sup>)", fast=False)
yt1 = gcurve(graph=gd, color=c1)
yt2 = gcurve(graph=gd, color=c2)
vt1 = gcurve(graph=gd2, color=c1)
vt2 = gcurve(graph=gd2, color=c2)
at1 = gcurve(graph=gd3, color=c1)
at2 = gcurve(graph=gd3, color=c2)

# 開啟檔案 data.csv, 屬性為寫入, 先寫入欄位的標題
file = open("data.csv", "w", encoding="UTF-8")
file.write("t(s), y1(m), y2(m), v1(m/s), v2(m/s), a1(m/s^2), a2(m/s^2)\n")
tp = 0

# 設定計算終端速度用的變數
eps = 1E-6
v1 = 0
v2 = -1E6
"""
 3. 物體運動部分, 小球速度變化大於 eps 時繼續運作
"""
while abs(v2 - v1) > eps:
    rate(1000)
# 更新小球受力、加速度、速度、位置，畫 y-t 及 v-t 圖
    f = -b*b1.v
    b1.a = vec(0, -g, 0) + f/m
    b1.v += b1.a*dt
    b1.pos += b1.v*dt
    b2.v += b2.a*dt
    b2.pos += b2.v*dt
    yt1.plot(pos=(t, b1.pos.y))
    vt1.plot(pos=(t, b1.v.y))
    at1.plot(pos=(t, b1.a.y))
    yt2.plot(pos=(t, b2.pos.y))
    vt2.plot(pos=(t, b2.v.y))
    at2.plot(pos=(t, b2.a.y))
# 每隔 0.1 秒將資料轉成字串後寫入檔案
    tc = t
    if tc == 0 or tc - tp >= 0.1:
        file.write(str(t) + "," + str(b1.pos.y) + "," + str(b2.pos.y) + \
                   "," + str(b1.v.y) + "," + str(b2.v.y) + "," + str(b1.a.y) + \
                   "," + str(b2.a.y) + "\n")
        tp = tc
# 更新 v1 為 v2 目前的值，更新 v2 為 b1.v.y
    v1, v2 = v2, b1.v.y
# 更新時間
    t += dt

print("t =", t, "vt =", v2)
file.close() # 關閉檔案
