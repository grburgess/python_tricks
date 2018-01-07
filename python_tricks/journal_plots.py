import matplotlib.pyplot as plt
import numpy as np


def set_journal(fig_width=245.26653, height_factor=1.):
    """
    Sets the matplotlib rc params to generate plots that are the proper
    size for two column journals. Simple specify the column width

    :param fig_width: Get this from LaTeX using \showthe\columnwidth

    """
    

    fig_width_pt =fig_width 
    inches_per_pt = 1.0/72.27               # Convert pt to inch
    golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean * height_factor      # height in inches
    fig_size =  [fig_width,fig_height]
    params = {'backend': 'ps',
              'axes.labelsize': 10,
              'font.size': 10,
              'legend.fontsize': 10,
              'xtick.labelsize': 8,
              'ytick.labelsize': 8,
              'text.usetex': True,
              'figure.figsize': fig_size,
              'font.family': 'serif'}
    plt.rcParams.update(params)
    
def reset():
    """
    Reset the plotting settings
    """
    
    plt.rcdefaults()

    #optional for notebook

    #%matplotlib inline
    #%matplotlib notebook


