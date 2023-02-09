import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig= plt.figure()
ax = plt.axes(projection='3d')
ln = plt.plot([], [], [], alpha=0.8, linewidth = 0.8)[0]
ax.view_init(5, 75)


pos = [0.63, 0.47, -0.54]
plotrange = [[0, 0], [0, 0], [0, 0]]
a, b, c = 2.07, 1.79, 0
timestep = 0.0025
trajectory = [[], [], []]


def differential(t, pos) :
    dx_dt = t*(pos[1] + a*pos[0]*pos[1] + pos[0]*pos[2])
    dy_dt = t*(1 - b*pos[0]*pos[0] + pos[1]*pos[2])
    dz_dt = t*(pos[0] - pos[0]*pos[0] - pos[1]*pos[1])
    return [dx_dt, dy_dt, dz_dt]


def update(frame):

    global timestep, a, b, c, pos, plotrange

    ax.view_init(ax.elev + 0.05, ax.azim - 0.1)

    for loop in range(250) :

        for i, diff in zip(range(3), differential(timestep,pos)): pos[i] += diff

        for val, lim, i in zip(pos, plotrange, range(3)):
            if   val < lim[0] : plotrange[i][0] = val
            elif val > lim[1] : plotrange[i][1] = val
            else : continue
            if   i==0 : ax.set_xlim(plotrange[0])
            elif i==1 : ax.set_ylim(plotrange[1])
            else      : ax.set_zlim(plotrange[2])

        if not loop%5 : 
            for i in range(3): trajectory[i].append(pos[i])

    ln.set_data_3d(trajectory)
    return ln

ani = FuncAnimation(fig, update, interval=1000/25)
#plt.show()
ani.save("anim.gif", writer='imagemagick', fps=25)