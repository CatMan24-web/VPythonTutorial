"""
 VPython教學: 3.等速度直線運動
 Ver. 1: 2018/2/18
 Ver. 2: 2019/9/5
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.05   # side length of wood block
l = 1        # floor length
v = 0.03     # Block speed
t = 4        # time
dt = 0.01    # Time interval

"""
 2. Screen settings

"""
scene = canvas(title="1D Motion", width=800, height=600, x=0, y=0, center=vec(0, 0.1, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, 0, 0), size=vec(l, 0.1*size, 0.5*l), color=color.blue)
cube = box(pos=vec(-0.5*L + 0.5*size, 0.55*size, 0), size=vec(size, size, size), color=color.custom, v=vec(v, 0, 0))
gd = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
gd2 = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
xt = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.red)

"""
3. In the moving part of the object, execution stops when the wooden block reaches the edge of the floor.
"""
while(cube.pos.x <= 0.5*l- 0.5*size):
    rate(1000)
    cube.pos.x += v*dt
    xt.plot(pos = (t, cube.pos.x))
    vt.plot(pos = (t, cube.v.x))
    t += dt

print("t = ", t)
