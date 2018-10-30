# coding=utf-8
# coding=utf-8
from computar_maximos import computar_notch
from read_spice_montecarlo import read_file_spice
import seaborn as sns
import matplotlib.pyplot as plt
from datacursor_easy import make_datacursor_general


def make_histogram(variable, unidad, data, filename, bar_width):
    fig = sns.distplot(data, norm_hist=True)

    y_vals = fig.get_yticks()

    fig.set_yticklabels(['{:3.0f}%'.format(x * 100 * bar_width) for x in y_vals])

    plt.xlabel(variable+" ("+unidad+")")
    plt.ylabel("Casos")
    make_datacursor_general(
        x1= variable,
        u1= unidad,
        filename="histogramas/output/"+filename,
        my_plt=plt,
        fig=fig)
