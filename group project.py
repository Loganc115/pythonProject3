import matplotlib.pyplot as plot
import numpy as np
#our names are Logan Clementi Quinn o'Brien
colors=["red",'white','purple','pink','yellow','orange']



y=np.array([8,10,8,14,11,8])
ppppp=([8,10])
x=len(ppppp)
plot.pie(y, labels=colors, colors=colors, frame=10,radius=2300, explode=(x))
plot.legend(title='four fruits')
plot.legend(colors, bbox_to_anchor=(0.85,1.025),   loc="upper left")
plot.show()










