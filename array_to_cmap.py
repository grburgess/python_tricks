import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def array_to_cmap(values,cmap,use_log=False):
    
    if use_log:
        
        norm = mpl.colors.LogNorm(vmin=min(values),vmax=max(values))
        
    else:
        
        norm = mpl.colors.Normalize(vmin=min(values),vmax=max(values))
        
        
    cmap = plt.cm.ScalarMappable(norm=norm,cmap=cmap)
    
    rgb_colors = map(cmap.to_rgba,values)
    
    return cmap, rgb_colors

    
