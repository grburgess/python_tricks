import numpy as np
import matplotlib.pyplot as plt

from python_tricks.camp_cycle import cmap_intervals

def stack_plot(x_values,*y_values,**kwargs):
    """
    Creates a stack plot of histograms


    :param x_values: the x range
    :param y_values: the y values of each plots
    :param scale: (optional) the scale * max y to separate the plots (default 0.5)
    :param x_scale: (optional) the x scaling 
    :param x_label: (optional) the x label
    :param cmap: (optional) the cmap for the scales
    :param line_color: (optional) the line color above the plot

    """
    
    _default_kwargs={'scale':0.5,
                     'x_scale':'linear',
                     'x_label':'x',
                     'cmap': 'viridis',
                     'line_color':None,
                    
                    }
    
    
    for k,v in _default_kwargs.iteritems():
        
        
        if k in kwargs:
            
            _default_kwargs[k] = kwargs.pop(k)
    
    
    
    fig, ax = plt.subplots()
    
    n_lines = len(y_values)
    
    
    colors = cmap_intervals(n_lines, _default_kwargs['cmap'])
    
    max_y = np.max(map(np.max,y_values))
    
    delta_y = _default_kwargs['scale'] * max_y
    
    y_addition = 0.
    
    zorder = -10.
    
    for i,y in enumerate(y_values):
        
        idx = y>0.
        
        
        ax.fill_between(x_values[idx],
                        y_addition,
                        y_addition + y[idx],
                        zorder=zorder,
                        color=colors[i],
                        **kwargs)
        
        if _default_kwargs['line_color'] is None:
            
            color = colors[i]
            
        else:
            
            color = _default_kwargs['line_color']
            
        ax.plot(x_values[idx],y_addition + y[idx],
                color=color,
                lw=1.2,
                zorder=zorder)
            
        
        y_addition += delta_y
        zorder-=1
        
    ax.set_xscale(_default_kwargs['x_scale'])
    ax.set_xlabel(_default_kwargs['x_label'])
    
    ax.set_yticks([])
    
    return fig
