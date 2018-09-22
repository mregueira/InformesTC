
from mpldatacursor import datacursor


def make_datacursor(mode, filename, plt):
    if mode == "mag":
        datacursor(display='multiple', tolerance=10, formatter="Freq: {x:.3e}  Hz \nAmp:{y:.1f} Db".format,
                   draggable=True)
    else:
        datacursor(display='multiple', tolerance=10, formatter="Freq: {x:.3e}  Hz \nFase:{y:.1f} grados".format,
                   draggable=True)

    plt.show()
    input("Press Enter ")

    plt.savefig(filename, dpi=300)
    plt.cla()
    plt.close()

