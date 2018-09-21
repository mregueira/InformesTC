import transferencias
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from math import *

r5_values = np.logspace(1,10,11)

np.logspace(1, 7, 10)

fig, ax = plt.subplots()


def computar_polos():

    data = []
    data_label = []


    for i in range(4):
        data_v = []
        label = []
        for r5 in r5_values:
            h1, h2, h3, h4 = transferencias.get_out(1, -1, r5)
            H = signal.lti(h4[0], h4[1])
            #print(len(H.poles))
            data_v.append((H.poles[i].real , H.poles[i].imag))
            label.append( "r5= "+str(int(r5)) )
        data_label.append(label)
        data.append(data_v)

    # dash_style =
    #     direction, length, (text)rotation, dashrotation, push
    # (The parameters are varied to show their effects, not for visual appeal).
    # dash_style = (
    #     (0, 20, -15, 30, 10),
    #     (1, 30, 0, 15, 10),
    #     (0, 40, 15, 15, 10),
    #     (1, 20, 30, 60, 10))
    for j in range(len(data)):
        ww = data[j]
        label = data_label[j]
        print(ww)
        (x, y) = zip(*ww)
        ax.plot(x, y, marker='o',linewidth=1)
        for i in range(len(ww)):
            (x, y) = ww[i]
            #(dd, dl, r, dr, dp) = dash_style[i]
            t = ax.text(x, y, label[i], withdash=False,
                        # dashdirection=dd,
                        # dashlength=dl,
                        # rotation=r,
                        # dashrotation=dr,
                        # dashpush=dp,
                        )

    #ax.set_xlim((0, 5))
    #ax.set_ylim((0, 5))

    plt.show()

computar_polos()