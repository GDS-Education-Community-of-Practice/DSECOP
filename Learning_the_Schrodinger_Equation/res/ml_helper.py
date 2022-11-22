import numpy as np
# import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F

import torch.optim as optim

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

from ipywidgets import interact

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
from matplotlib.lines import Line2D
import matplotlib.image as img
import copy
#gif from plots using imagemagick
#convert -fuzz 1% -delay 1x8 *.png  -coalesce -layers OptimizeTransparency animation.gif

def viz_colour_rgb(c):
    labels = ['r','g','b','','col']
    
    w = [1,1,1]
    cb = np.zeros((1,5,3))
    cb[0,0,0] = c[0]
    cb[0,1,1] = c[1]
    cb[0,2,2] = c[2]
    cb[0,3,:] = w
    cb[0,4,:] = c

   
    fig = plt.figure(figsize = (5,10))
    ax = fig.add_axes([0,0, 1, 1])  # span the whole figure
    #ax.set_axis_off()
    
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
#    ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=0, ha="left",
             rotation_mode="anchor")


    ax.tick_params(left = False, right = False , labelleft = False ,
                    labelbottom = True, bottom = False)
    #ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))
    #ax.set_xticklabels(labels, rotation=0, ha='left', minor=False)
 
    ax.imshow(cb)
    plt.show()
    print(f"r = {float(c[0]):.2}, g = {float(c[1]):.2}, b = {float(c[2]):.2}")

def viz_colour_predicted_rgb(t,p):
    print("Input RGB:")
    viz_colour_rgb(t)
    print("\nOutput Prediction RGB:")
    viz_colour_rgb(p)
    print("##############################")

# def viz_colour_predicted(t,p):
#     labels = ['r','g','b','','t','','p']
    
#     w = [1,1,1]
#     cb = np.zeros((1,7,3))
#     cb[0,0,0] = t[0]
#     cb[0,1,1] = t[1]
#     cb[0,2,2] = t[2]
#     cb[0,3,:] = w
#     cb[0,4,:] = t
#     cb[0,5,:] = w
#     cb[0,6,:] = p

   
#     fig = plt.figure(figsize = (5,10))
#     ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
#     #ax.set_axis_off()
    
#     ax.set_xticks(np.arange(len(labels)), labels=labels)
# #    ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

#     # Rotate the tick labels and set their alignment.
#     plt.setp(ax.get_xticklabels(), rotation=0, ha="left",
#              rotation_mode="anchor")


#     ax.tick_params(left = False, right = False , labelleft = False ,
#                     labelbottom = True, bottom = False)
#     #ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))
#     #ax.set_xticklabels(labels, rotation=0, ha='left', minor=False)
#     ax.imshow(cb)
#     plt.show()
#     print(f"True: r = {t[0]:.2}, g = {t[1]:.2}, b = {t[2]:.2}")
#     print(f"Predited: r = {p[0]:.2}, g = {p[1]:.2}, b = {p[2]:.2}")

rgb_scale = 1.0
cmyk_scale = 1.0

def rgb_to_cmyk(col):
    r,g,b = col
    if (r == 0) and (g == 0) and (b == 0):
        # black
        return 0, 0, 0, cmyk_scale

    # rgb [0,1] -> cmy [0,1]
    c = 1 - r 
    m = 1 - g
    y = 1 - b

    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) 
    m = (m - min_cmy) 
    y = (y - min_cmy) 
    k = min_cmy

    # rescale to the range [0,cmyk_scale]
    return c*cmyk_scale, m*cmyk_scale, y*cmyk_scale, k*cmyk_scale

def cmyk_to_rgb(col):
    """
    """
    c,m,y,k = col
    r = max(1.0-(c+k),0.0)
    g = max(1.0-(m+k),0.0)
    b = max(1.0-(y+k),0.0)
    return r,g,b

def viz_colour_cmyk(c):
    labels = ['c','m','y','k','','col']
    c = np.asarray(c)
    
    cyan = np.asarray([0,1.0,1.0])
    magenta = np.asarray([1.0,0.0,1.0])
    yellow = np.asarray([1.0,1.0,0.0])
    w = np.asarray([1,1,1])
    
    cyan = np.asarray([1.0,0,0,0])
    magenta = np.asarray([0,1,0,0])
    yellow = np.asarray([0,0,1,0])
    w = np.asarray([1,1,1])
    
    
    rgb_c = cmyk_to_rgb(c)
    cb = np.zeros((1,6,3))
    cb[0,0,:] = cmyk_to_rgb(c[0] * cyan)
    cb[0,1,:] = cmyk_to_rgb(c[1] * magenta)
    cb[0,2,:] = cmyk_to_rgb(c[2] * yellow)
    cb[0,3,:] = (1 - c[3]) * w
    cb[0,4,:] = w
    cb[0,5,:] = rgb_c

   
    fig = plt.figure(figsize = (5,10))
    ax = fig.add_axes([0,0, 1, 1])  # span the whole figure
    #ax.set_axis_off()
    
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
#    ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=0, ha="left",
             rotation_mode="anchor")


    ax.tick_params(left = False, right = False , labelleft = False ,
                    labelbottom = True, bottom = False)
    #ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))
    #ax.set_xticklabels(labels, rotation=0, ha='left', minor=False)
 
    ax.imshow(cb)
    plt.show()
    #print(f"r = {float(rgb_c[0]):.2}, g = {float(rgb_c[1]):.2}, b = {float(rgb_c[2]):.2}")
    print(f"c = {float(c[0]):.2}, m = {float(c[1]):.2}, y = {float(c[2]):.2}, k = {float(c[3]):.2}")

def viz_colour_predicted_cmyk(t,p):
    print("Input RGB:")
    viz_colour_rgb(t)
    print("\nOutput Prediction:")
    viz_colour_cmyk(p)
    print("##############################")

class ColourDataset(Dataset):

    def __init__(self, input_data, output_data, transform=None):
        
        self.input_data = input_data
        self.output_data = output_data
        self.transform = transform

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        
        sample = [self.input_data[idx], self.output_data[idx]]


        return sample
debug = False

def get_plots_norm_colorbar(y_true,y_pred, n_x, n_t, x_dom, t_dom, plot_fname):
    labels = ["Predicted", "True", "Abs Err"]
    
    u,v,dens = get_density(y_true.detach().cpu().numpy())
    u_pred, v_pred, dens_pred = get_density(y_pred.detach().cpu().numpy())
    
    

    plot_name = 'TD SE Results' #remove 'network_checkpoint_'
    fig = plt.figure(figsize=(7,8),dpi=100)
    
    mse_u = 0.0
    mse_v = 0.0
    show_cb = False
    cmap = plt.get_cmap('viridis')
    
    x_min = 0
    x_max = 0
    t_min = 0
    t_max = 0
    
    
    u_max = -99.
    u_min = 99.
    v_max = -99.
    v_min = 99.
    d_max = -99.
    d_min = 99.
    
    u_max = np.max((np.max(u),np.max(u_pred)))
    u_min = np.min((np.min(u),np.min(u_pred)))
    v_max = np.max((np.max(v),np.max(v_pred)))
    v_min = np.min((np.min(v),np.min(v_pred)))
    d_max = np.max((np.max(dens),np.max(dens_pred)))
    d_min = np.min((np.min(dens),np.min(dens_pred)))
        
    extent = [x_dom[0] , x_dom[1], t_dom[0] ,t_dom[1]]
    
    u_plot = np.zeros((n_x,n_t))
    v_plot = np.zeros_like((n_x,n_t))
    d_plot = np.zeros_like((n_x,n_t))
    
    reshape_to_grid = lambda x: np.reshape(x,  (n_x, n_t))
    
    for i in np.arange(3):
        if i==0:
            u_plot = reshape_to_grid(u_pred)
            v_plot = reshape_to_grid(v_pred)
            d_plot = reshape_to_grid(dens_pred)
            show_cb = False
        if i==1:
            u_plot = reshape_to_grid(u)
            v_plot = reshape_to_grid(v)
            d_plot = reshape_to_grid(dens)
        if i == 2:
            u_plot = np.abs(reshape_to_grid(u - u_pred))
            v_plot = np.abs(reshape_to_grid(v - v_pred))
            d_plot = np.abs(reshape_to_grid(dens_pred - dens))
            show_cb = True


        ax1 = fig.add_subplot(3,3,i+1)
        ims = ax1.imshow(u_plot, extent=extent,vmin=u_min, vmax=u_max)
        ax1.set_title(fr"{labels[i]} Re($\psi$)")
        ax1.set_xlabel(r'$x$')
        ax1.set_ylabel(r'$t$')
        if show_cb:
            divider = make_axes_locatable(ax1)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            norm = mpl.colors.Normalize(vmin=u_min, vmax=u_max)
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            fig.colorbar(sm, cax=cax)
            
        ax1 = fig.add_subplot(3,3,i+4)
        ax1.set_title(fr"{labels[i]} Im($\psi$)")
        ims = ax1.imshow(v_plot, extent=extent,vmin=v_min, vmax=v_max)
        ax1.set_xlabel(r'$x$')
        ax1.set_ylabel(r'$t$')
        if show_cb:
            divider = make_axes_locatable(ax1)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            norm = mpl.colors.Normalize(vmin=v_min, vmax=v_max)
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            fig.colorbar(sm, cax=cax)
            
        ax1 = fig.add_subplot(3,3,i+7)
        ax1.set_title(fr"{labels[i]} $|\psi|^2$")
        ims = ax1.imshow(d_plot, extent=extent,vmin=d_min, vmax=d_max)
        ax1.set_xlabel(r'$x$')
        ax1.set_ylabel(r'$t$')
        if show_cb:
            divider = make_axes_locatable(ax1)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            norm = mpl.colors.Normalize(vmin=d_min, vmax=d_max)
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            fig.colorbar(sm, cax=cax)
        
        if i==2:
            mse_u = np.mean(u_plot**2)
            mse_v = np.mean(v_plot**2)
            
        print(f"{i} finished")
            
    plot_title = plot_name
    plt.suptitle(fr"{plot_title}",y=0.92)
    plt.savefig(f'res/plots/{plot_fname}')
    plt.show()
    print(f"mse: u: {mse_u}, v:{mse_v}")
    return mse_u,mse_v

def get_density(y_pred):
# Helper function to split data into real, imag, density
    u = y_pred[:,0]
    v = y_pred[:,1]
    dens = u**2 + v**2
    
    return u,v,dens

def get_waveforms(analytical_solution_function):
    
    L = float(np.pi)
    omega = 1
    delta_T = 0.1
    delta_X = 0.1
    x_dom = [-L,L]
    t_dom = [0, 2*L]
    #analytical_solution_function = get_analytical_solution_base

    x = np.arange(x_dom[0], x_dom[1], delta_X).astype(float)
    t = np.arange(t_dom[0], t_dom[1], delta_T).astype(float)
    X, T = np.meshgrid(x, t)
    
    
#     X = np.expand_dims(X.flatten(), axis=-1)
#     T = np.expand_dims(T.flatten(), axis=-1)

    psi_val = analytical_solution_function(X,T,omega)
    u = np.real(psi_val)
    v = np.imag(psi_val)
    
    dens = u**2 + v**2
    max_d = np.max(dens)+0.02
    
    
    
    for t_step in range(len(t)):
        curr_u = u[t_step,:]
        curr_v = v[t_step,:]
        curr_d = dens[t_step,:]
        
        fig, ax = plt.subplots()
        plt.ylim(0.0,max_d)
        ax.plot(x, curr_d)
        
        ax.set(xlabel='x (au)', ylabel=r'Probability Density $|\psi(x)|^2$',
               title=fr'$|\psi(x)|^2$ at t={t[t_step]:.2f} au')
        ax.grid()

        fig.savefig(f"res/plots/waveform/t_{str(t_step).zfill(2)}.png")
        plt.show()

#     train_input = np.hstack((X,T))
#     train_output = np.hstack((u,v))

#     train_x = torch.tensor(train_input)
#     train_y = torch.tensor(train_output)
    return None

def live_waveform():
    L = float(np.pi)
    omega = 1
    delta_T = 0.1
    delta_X = 0.2
    x_dom = [-L,L]
    t_dom = [0, 2*L]
    analytical_solution_function = get_analytical_solution_base

    x = np.arange(x_dom[0], x_dom[1], delta_X).astype(float)
    t = np.arange(t_dom[0], t_dom[1], delta_T).astype(float)
    X, T = np.meshgrid(x, t)


    #     X = np.expand_dims(X.flatten(), axis=-1)
    #     T = np.expand_dims(T.flatten(), axis=-1)

    psi_val = analytical_solution_function(X,T,omega)
    u = np.real(psi_val)
    v = np.imag(psi_val)

    dens = u**2 + v**2
    max_d = np.max(dens)+0.02


    @interact(t_step=widgets.IntSlider(min=0, max=62, step=1, value=0,continuous_update=True))
    def interactive_viz_colour(t_step):

        curr_d = dens[t_step,:]
        fig, ax = plt.subplots()
        plt.ylim(0.0,max_d)
        ax.plot(x, curr_d)

        ax.set(xlabel='x (au)', ylabel=r'Probability Density $|\psi(x)|^2$',
               title=fr'$|\psi(x)|^2$ at t={t[t_step]:.2f} au')
        ax.grid()

        #fig.savefig(f"res/plots/waveform/t_{t_step}.png")
        plt.show()


