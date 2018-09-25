
from mpldatacursor import datacursor


def make_datacursor(my_mode, filename, my_plt , my_fig):
    if my_mode == "mag":
        datacursor(display='multiple', tolerance=10, formatter="Freq: {x:.3e}  Hz \nAmp:{y:.1f} Db".format,
                   draggable=True)
    else:
        datacursor(display='multiple', tolerance=10, formatter="Freq: {x:.3e}  Hz \nFase:{y:.1f} grados".format,
                   draggable=True)

    my_plt.show()
    input("Press Enter ")

    my_fig.savefig(filename, dpi=300)
    my_plt.cla()
    my_plt.close()

