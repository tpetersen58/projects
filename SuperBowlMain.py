import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

initial = pd.read_excel('SuperBowlData.xlsx', sheet_name = 'Sheet1', skiprows = 0)

def get_data(table,rownum,title):
    data = pd.DataFrame(table.loc[rownum][1:].astype(float))
    data.columns = {title}
    return data

title = 'Cost (millions of dollars)'

d = get_data(initial,3,title)
x = np.array(d.index)
y = np.array(d[title]/1000000)

frame = pd.DataFrame(y, x)
frame.columns = {title}

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\taylorp.DUTRO\\Downloads\\FFmpeg\\FFmpeg\\bin\\ffmpeg.exe'

Writer = animation.writers['ffmpeg']
writer = Writer(fps=12, metadata=dict(artist='Me'), bitrate=1800)

fig = plt.figure(figsize=(12,6))
fig.patch.set_facecolor('lightgray')
ax = fig.add_subplot(1, 1, 1)
#plt.xlim(1, 54)
#plt.ylim(np.min(frame)[0], np.max(frame)[0])
ax.set_xlim(1, 54)
ax.set_ylim(0, 5)
plt.grid(linestyle=':')
plt.xlabel('Super Bowl', fontsize=20)
plt.ylabel('30 Sec Ad Cost in Dollars', fontsize=20)
plt.title('Super Bowl 30 Second Ad Cost', fontsize=20)
plt.xticks(range(1, 54, 2))
plt.yticks(np.arange(6, step=.5))

def animate(i):
    data = frame.iloc[:int(i+1)]
    p = sns.lineplot(x=data.index, y=data[title], data=data, color ='b')
    p.tick_params(labelsize=12)
    plt.setp(p.lines, linewidth=4)

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=54, repeat=True)
#plt.show()
ani.save('SuperBowl.mp4', writer=writer)