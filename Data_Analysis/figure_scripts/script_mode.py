from math import e
from matplotlib import ticker
import numpy as np
from numpy import sqrt, sin, cos, pi, exp
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import h5py  
from scipy.optimize import curve_fit
import scipy.integrate as integrate
from xpcs_viewer import XpcsFile as xf
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
#import matplotlib.colors as mcolors



def plot_g2_ROI6_before_normalization(a,num_rows,num_cols, g2_fit_line):
    

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(18, 12))
    plt.setp(axs, xticks=[1e-5,1e-3,1e-1], yticks=[1,1.05,1.1,1.15])
    for rows in range(num_rows):
        for colums in range(num_cols):
            dim = rows*num_cols+colums  
            ax = axs[rows,colums]
            ax.set_xscale('log')
            # ax.set_ylim(0.98, 1.3)
            ax.errorbar(a.t_el, a.g2[:,dim], yerr=a.g2_err[:,dim], 
                fmt='ro', markersize=9, markerfacecolor='none')
            ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %a.ql_dyn[dim]), horizontalalignment='center',
                    verticalalignment='center', transform=ax.transAxes)
            ax.plot(g2_fit_line[dim]["fit_x"][10:-10],g2_fit_line[dim]["fit_y"][10:-10], 'b-')
    plt.savefig('/Users/dozgulbas/Desktop/g2.pdf')


def plot_g2_ROI6_after_normalization(a,num_rows,num_cols, g2_fit_line):

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(25, 12))
    plt.setp(axs, xticks=[1e-5,1e-3,1e-1], yticks=[0,0.05,0.1,0.15])
    for rows in range(num_rows):
        for colums in range(num_cols):
            dim = rows*num_cols+colums  
            ax = axs[rows,colums]
            ax.set_xscale('log')
            ax.set_ylim(-0.02, 0.15)
            ax.errorbar(a.t_el, a.g2[:,dim]-g2_fit_coeff[dim,0,3], yerr=a.g2_err[:,dim], 
                fmt='ro', markersize=9, markerfacecolor='none')
            ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %a.ql_dyn[dim]), horizontalalignment='center',
                    verticalalignment='center', transform=ax.transAxes)
            ax.plot(g2_fit_line[dim]["fit_x"][10:-10],g2_fit_line[dim]["fit_y"][10:-10], 'b-')
    plt.savefig('/Users/dozgulbas/Desktop/delta_g2.pdf')

# ------------ Noisy vs succesfull ----------------
def plot_noisy_vs_normal(g2_fit_line, a,a2,a3,a4,a5,a6,a7,a8,a9,a10,d2,d3,d4,d5,d6,d7,d8,d9,d10):
    scale = 1
    width = 3.6*scale
    font_size = 8*scale
    line_width = 0.5*scale
    marker_size = 1*scale
    tick_length_major = 4*scale
    tick_length_minor = 2*scale
    dim=1

    fig, (axt,axa) = plt.subplots(1, 2, figsize=(width, 0.8*width))
    # plt.setp((axt,axa), xticks=[1e-5,1e-3,1e-1], yticks=[1,1.05,1.1,1.15])
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['axes.linewidth'] = line_width
    # plt.minorticks_on()

    # minor_locator = AutoMinorLocator(2)


    # ax = axk[1]
    axa.set_xscale('log')
    # axa.set_ylim(0.99, 1.15)

    axa.set_xlim(1.1e1 ,1e4)
    # axa.set_xticks([1e-4, 1e-3, 1e-2])
    # axa.set_xticklabels(["10$^2$", "10$^3$", "10$^4$"],fontsize = font_size)

    # axa.xaxis.set_minor_locator(AutoMinorLocator())

    axa.errorbar(a.t_el[0:30]*1000000, a.g2[:,2][0:30], yerr=a.g2_err[:,2][0:30], color = 'tab:blue' ,fmt = 's',  markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a2.t_el[0:30]*1000000, a2.g2[:,2][0:30], yerr=a2.g2_err[:,2][0:30], color = 'tab:orange' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a3.t_el[0:30]*1000000, a3.g2[:,2][0:30], yerr=a3.g2_err[:,2][0:30], color = 'tab:green' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a4.t_el[0:30]*1000000, a4.g2[:,2][0:30], yerr=a4.g2_err[:,2][0:30], color = 'tab:red' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a5.t_el[0:30]*1000000, a5.g2[:,2][0:30], yerr=a5.g2_err[:,2][0:30], color = 'tab:purple' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a6.t_el[0:30]*1000000, a6.g2[:,2][0:30], yerr=a6.g2_err[:,2][0:30], color = 'tab:brown' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a7.t_el[0:30]*1000000, a7.g2[:,2][0:30], yerr=a7.g2_err[:,2][0:30], color = 'tab:pink' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a8.t_el[0:30]*1000000, a8.g2[:,2][0:30], yerr=a8.g2_err[:,2][0:30], color = 'tab:gray' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a9.t_el[0:30]*1000000, a.g2[:,2][0:30], yerr=a9.g2_err[:,2][0:30], color = 'tab:olive' ,fmt = 's', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axa.errorbar(a10.t_el[0:30]*1000000, a10.g2[:,2][0:30], yerr=a10.g2_err[:,2][0:30], color = 'tab:cyan' ,fmt = 's',markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')
    axa.plot(g2_fit_line[2]["fit_x"][10:-10]*1000000,g2_fit_line[2]["fit_y"][10:-10], 'k-', markersize=marker_size, linewidth=2*line_width)
    # axa.xaxis.grid(True, which='minor')
    # ax.legend()
    # axa.set_xlabel('Delay Time $\mathdefault{\u03C4}$ ($\mathdefault{\mu}$s)', 
    #           fontsize=font_size, labelpad=0.2*font_size)
    # axa.set_ylabel('$\mathdefault{\Delta}$g$\mathdefault{_2}$', 
    #           fontsize=font_size, labelpad=0.05*font_size)
    axa.grid( color='k', linestyle=':', linewidth=line_width, alpha=0.1, which='both')
    axa.tick_params('both', length=tick_length_major, width=line_width, which='major', labelsize=font_size)
    axa.tick_params('x', length=tick_length_minor, width=0.5*line_width, which='minor',
                labelleft=False, labelbottom=False)
    axa.tick_params(which='major' ,top=False, bottom=True, left=False, right=False,
                    labelleft=False, labelbottom=True)
 
    for axis in ['top','bottom','left','right']:
        axa.spines[axis].set_linewidth(line_width)

    # axt = axk[0]

    axt.set_xscale('log')
    # # axt.set_yscale('log')
    # # axt.set_ylim(0.99, 1.15)

    axt.set_xlim(1.1e1 ,1e4)
    # axt.set_xticks([1e-4, 1e-3, 1e-2])
    # axt.set_xticklabels(["10$^2$", "10$^3$", "10$^4$"],fontsize = font_size)
    # axt.minorticks_on()

    # axa.minorticks_on()

    axt.errorbar(d.t_el[0:30]*1000000, d.g2[:,2][0:30], yerr=d.g2_err[:,2][0:30], color = 'tab:blue' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d2.t_el[0:30]*1000000, d2.g2[:,2][0:30], yerr=d2.g2_err[:,2][0:30],color = 'tab:orange' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d3.t_el[0:30]*1000000, d3.g2[:,2][0:30], yerr=d3.g2_err[:,2][0:30], color = 'tab:green' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d4.t_el[0:30]*1000000, d4.g2[:,2][0:30], yerr=d4.g2_err[:,2][0:30], color = 'tab:red' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d5.t_el[0:30]*1000000, d5.g2[:,2][0:30], yerr=d5.g2_err[:,2][0:30], color = 'tab:purple' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d6.t_el[0:30]*1000000, d6.g2[:,2][0:30], yerr=d6.g2_err[:,2][0:30], color = 'tab:brown' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d7.t_el[0:30]*1000000, d7.g2[:,2][0:30], yerr=d7.g2_err[:,2][0:30], color = 'tab:pink' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d8.t_el[0:30]*1000000, d8.g2[:,2][0:30], yerr=d8.g2_err[:,2][0:30],color = 'tab:gray' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d9.t_el[0:30]*1000000, d9.g2[:,2][0:30], yerr=d9.g2_err[:,2][0:30],  color = 'tab:olive' ,fmt = 'v', markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')

    axt.errorbar(d10.t_el[0:30]*1000000, d10.g2[:,2][0:30], yerr=d10.g2_err[:,2][0:30], color = 'tab:cyan' ,fmt = 'v',markersize=marker_size, linewidth=line_width, markeredgewidth=line_width, markerfacecolor='none')
    axt.plot(g2_fit_line[2]["fit_x"][10:-10]*1000000,g2_fit_line[2]["fit_y"][10:-10], 'k-', markersize=marker_size, linewidth=2*line_width)
    
    fig.supxlabel('Delay Time $\mathdefault{\u03C4}$ ($\mathdefault{\mu}$s)', fontsize=font_size, y = -0.01)
    fig.supylabel('g$\mathdefault{_2}$', fontsize=font_size, x = - 0.02)
    
    # axt.set_xlabel('Delay Time $\mathdefault{\u03C4}$ ($\mathdefault{\mu}$s)', 
    #           fontsize=font_size, labelpad=0.2*font_size, loc = "right")
    # axt.set_ylabel('$\mathdefault{\Delta}$g$\mathdefault{_2}$', 
    #           fontsize=font_size, labelpad=0.05*font_size)
    axt.grid(color='k', linestyle=':', linewidth=line_width, alpha=0.1, which='both')
    axt.tick_params('both', length=tick_length_major, width=line_width, which='major', labelsize=font_size)
    axt.tick_params('x', length=tick_length_minor, width=0.5*line_width, which='minor',
                labelleft=False, labelbottom=False)
    # axt.xaxis.grid(True, which='minor')
    
    for axis in ['top','bottom','left','right']:
        axt.spines[axis].set_linewidth(line_width)

    # axt.legend()
    plt.savefig('/Users/dozgulbas/Desktop/delta_g2_airflow_comparison.pdf', dpi=600, format='pdf', 
            facecolor='w', edgecolor='w', transparent=False, bbox_inches='tight')





# COMPARISON OF THE DROPLET/CAP/CELLS before normalization and baseline subtraction
def plot_g2_before_normalization(a,b,c,e,g2_fit_line,g2_fit_line_b,g2_fit_line_c):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    plt.setp(ax, xticks=[10e-5, 10e-4, 10e-3, 10e-2, 10e-1, 10e0], yticks=[1,1.02,1.04,1.06,1.08,1.1,1.12,1.14,1.16])

    ax.set_xscale('log')
    ax.set_ylim(0.99, 1.16)
    ax.set_xlim(1e-5, 3)

    ax.errorbar(a.t_el, a.g2[:,2], yerr=(a.g2_err[:,2]), fmt='rs', label = 'Pendant Drop', linewidth=1, markersize=10, markerfacecolor='none')
    ax.plot(g2_fit_line[2]["fit_x"][10:-10],g2_fit_line[2]["fit_y"][10:-10], 'k-')


    ax.errorbar(b.t_el, b.g2[:,2], yerr=b.g2_err[:,2], fmt='gv',label = 'CapCell', linewidth=1,markersize=10, markerfacecolor='none')
    ax.plot(g2_fit_line_b[2]["fit_x"][10:-10],g2_fit_line_b[2]["fit_y"][10:-10], 'k-')

    ax.errorbar(e.t_el, e.g2[:,8], yerr=e.g2_err[:,8], fmt='cx',label = 'Glass', linewidth=1,markersize=10, markerfacecolor='none')
    #ax.plot(g2_fit_line_e[2]["fit_x"][10:-10],g2_fit_line_e[2]["fit_y"][10:-10], 'k-')

    ax.errorbar(c.t_el, c.g2[:,2], yerr=c.g2_err[:,2], fmt='bo', label = 'Capillary', linewidth=1, markersize=10, markerfacecolor='none')
    ax.plot(g2_fit_line_c[2]["fit_x"][10:-10],g2_fit_line_c[2]["fit_y"][10:-10], 'k',label = 'Fitting', linewidth=2, markersize=10, markerfacecolor='none')

    # ax.errorbar(d.t_el, d.g2[:,2], yerr=d.g2_err[:,2], fmt='gv', label = 'Pendant Drop Witout Air Flow Isolation',linewidth=1, markersize=10, markerfacecolor='none')
    # ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %d.ql_dyn[2]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    # ax.plot(g2_fit_line_d[2]["fit_x"],g2_fit_line_d[2]["fit_y"], 'k-')

    ax.set_xlabel('tau (s)')
    ax.set_ylabel('g2')
    ax.legend()

    plt.savefig('/Users/dozgulbas/Desktop/delta_g2_all_glass_comparison.pdf')


# COMPARISON OF THE DROPLET/CAP/CELLS After normalization and baselinesubtraction
def plot_g2_after_normalization(a,b,c,g2_fit_line,g2_fit_coeff,g2_fit_coeff_b,g2_fit_coeff_c,contrast_drop,contrast_cell,contrast_cap):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    plt.setp(ax, xticks=[10e-5, 10e-4, 10e-3, 10e-2, 10e-1, 10e0], yticks=[0,0.2,0.4,0.6,0.8,1])

    ax.set_xscale('log')
    ax.set_ylim(-0.1, 1.1)
    ax.set_xlim(1e-5, 3)

    ax.errorbar(a.t_el, (a.g2[:,2]-g2_fit_coeff[2,0,3])/contrast_drop, yerr=(a.g2_err[:,2])/contrast_drop, fmt='rs', label = 'Pendant Drop', linewidth=1, markersize=10, markerfacecolor='none')
    ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %a.ql_dyn[2]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    ax.plot(g2_fit_line[2]["fit_x"][10:-10],(g2_fit_line[2]["fit_y"][10:-10]-g2_fit_coeff[2,0,3])/contrast_drop, 'k-',label = 'Fitting', linewidth=1, markersize=10, markerfacecolor='none')

    ax.errorbar(b.t_el, (b.g2[:,2]-g2_fit_coeff_b[2,0,3])/contrast_cell, yerr=(b.g2_err[:,2])/contrast_cell, fmt='gv',label = 'CapCell', linewidth=1,markersize=10, markerfacecolor='none')
    ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %b.ql_dyn[2]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    # ax.plot(g2_fit_line_b[2]["fit_x"],(g2_fit_line_b[2]["fit_y"]-g2_fit_coeff_b[2,0,3])/contrast_cell, 'k-')

    ax.errorbar(c.t_el, (c.g2[:,2]-g2_fit_coeff_c[2,0,3])/contrast_cap, yerr=(c.g2_err[:,2])/contrast_cap, fmt='bo', label = 'Capillary', linewidth=1, markersize=10, markerfacecolor='none')
    ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %c.ql_dyn[2]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    # ax.plot(g2_fit_line_c[2]["fit_x"],(g2_fit_line_c[2]["fit_y"]-g2_fit_coeff_c[2,0,3])/contrast_cap, 'k',label = 'Fitting', linewidth=2, markersize=10, markerfacecolor='none')

    ax.set_xlabel('tau (s)')
    ax.set_ylabel('g2')
    ax.legend()
    # ax.errorbar(d.t_el, d.g2[:,2]-g2_fit_coeff_d[1,0,3], yerr=d.g2_err[:,2], fmt='ro', markersize=9, markerfacecolor='none')
    # ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %d.ql_dyn[2]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    # ax.plot(g2_fit_line_d[2]["fit_x"],g2_fit_line_d[2]["fit_y"], 'b-')
    plt.savefig('/Users/dozgulbas/Desktop/delta_g2_comparison.pdf')

# COMPARISON OF THE DROPLET/CAP/CELLS After normalization and baselinesubtraction up to ROI10
def plot_g2_for_10_ROI(a,b,c,g2_fit_line,g2_fit_coeff,g2_fit_coeff_b,g2_fit_coeff_c,contrast_drop,contrast_cell,contrast_cap):
    num_rows, num_cols = 3,4
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(25, 10))
    plt.setp(axs, xticks=[1e-5,1e-3,2], yticks=[0,0.2,0.4,0.6,0.8,1])
    for rows in range(num_rows):
        for colums in range(num_cols):
            dim = rows*num_cols+colums 
            if dim >9 :
                break
            else: 
                ax = axs[rows,colums]

                ax.errorbar(a.t_el, (a.g2[:,dim]-g2_fit_coeff[dim,0,3])/contrast_drop, yerr=(a.g2_err[:,dim])/contrast_drop, fmt='rs', label = 'Pendant Drop', linewidth=1, markersize=10, markerfacecolor='none')
                ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %a.ql_dyn[dim]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
                ax.plot(g2_fit_line[dim]["fit_x"][10:-10],(g2_fit_line[dim]["fit_y"][10:-10]-g2_fit_coeff[dim,0,3])/contrast_drop, 'k-')

                ax.errorbar(b.t_el, (b.g2[:,dim]-g2_fit_coeff_b[dim,0,3])/contrast_cell, yerr=(b.g2_err[:,dim])/contrast_cell, fmt='gv',label = 'CapCell', linewidth=1,markersize=10, markerfacecolor='none')
                ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %b.ql_dyn[dim]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
                # ax.plot(g2_fit_line_b[2]["fit_x"][10:-10],(g2_fit_line_b[2]["fit_y"][10:-10]-g2_fit_coeff_b[dim,0,3])/contrast_cell, 'k-')

                ax.errorbar(c.t_el, (c.g2[:,dim]-g2_fit_coeff_c[dim,0,3])/contrast_cap, yerr=(c.g2_err[:,dim])/contrast_cap, fmt='bo', label = 'Capillary', linewidth=1, markersize=10, markerfacecolor='none')
                ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %c.ql_dyn[dim]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
                # ax.plot(g2_fit_line_c[2]["fit_x"][10:-10],(g2_fit_line_c[2]["fit_y"][10:-10]-g2_fit_coeff_c[dim,0,3])/contrast_cap, 'k',label = 'Fitting', linewidth=2, markersize=10, markerfacecolor='none')

                # ax.set_xlabel('tau (s)')
                # ax.set_ylabel('g2')
                ax.set_xscale('log')
                # ax.set_ylim(-0.02, 0.15)

                # ax.errorbar(a.t_el, a.g2[:,dim]-g2_fit_coeff[dim,0,3], yerr=a.g2_err[:,dim], 
                #     fmt='ro', markersize=9, markerfacecolor='none')
                # ax.text(0.6, 0.8, ('Q = %5.4f $\AA^{-1}$' %a.ql_dyn[dim]), horizontalalignment='center',
                #         verticalalignment='center', transform=ax.transAxes)
                # ax.plot(g2_fit_line[dim]["fit_x"],g2_fit_line[dim]["fit_y"], 'b-')
    plt.savefig('/Users/dozgulbas/Desktop/delta_g2_comparison_up_to_ROI10.pdf')

#Plotting Tau vs q

def plot_tau_vs_q(a,b,c):
        
    tauq_power = - 2
    LB_list = [1e-12, tauq_power]
    UB_list = [1e-3, tauq_power]
    tau_fit = a.fit_tauq(q_range=[0.002, 0.008], bounds=[LB_list, UB_list], fit_flag=[True, False])

    tauq_fit_val = tau_fit["tauq_fit_val"]
    tauq_fit_line = tau_fit["tauq_fit_line"]
    tauq_q = tau_fit["tauq_q"]
    tauq_tau = tau_fit["tauq_tau"]
    tauq_tau_err = tau_fit["tauq_tau_err"]

    tau_fit_b = b.fit_tauq(q_range=[0.002, 0.008], bounds=[LB_list, UB_list], fit_flag=[True, False])

    tauq_fit_val_b = tau_fit_b["tauq_fit_val"]
    tauq_fit_line_b = tau_fit_b["tauq_fit_line"]
    tauq_q_b = tau_fit_b["tauq_q"]
    tauq_tau_b = tau_fit_b["tauq_tau"]
    tauq_tau_err_b = tau_fit_b["tauq_tau_err"]

    tau_fit_c = c.fit_tauq(q_range=[0.002, 0.008], bounds=[LB_list, UB_list], fit_flag=[True, False])

    tauq_fit_val_c = tau_fit_c["tauq_fit_val"]
    tauq_fit_line_c = tau_fit_c["tauq_fit_line"]
    tauq_q_c = tau_fit_c["tauq_q"]
    tauq_tau_c = tau_fit_c["tauq_tau"]
    tauq_tau_err_c = tau_fit_c["tauq_tau_err"]

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    ax.errorbar(tauq_q,tauq_tau,tauq_tau_err,fmt='rs', markersize=9, markerfacecolor='none')

    ax.set_xscale('log')
    ax.set_yscale('log')
    # ax.set_xlabel('tau (s)')
    # ax.set_ylabel('g2')
    ax.plot(tauq_fit_line["fit_x"],tauq_fit_line["fit_y"],'k--',linewidth=4)
    ax.errorbar(tauq_q_b,tauq_tau_b,tauq_tau_err_b,fmt='gv', markersize=9, markerfacecolor='none')
    ax.plot(tauq_fit_line_b["fit_x"],tauq_fit_line_b["fit_y"],'k--',linewidth=4)
    ax.errorbar(tauq_q_c,tauq_tau_c,tauq_tau_err_c,fmt='bo', markersize=9, markerfacecolor='none')
    ax.plot(tauq_fit_line_c["fit_x"],tauq_fit_line_c["fit_y"],'k--',linewidth=4)

    plt.savefig('/Users/dozgulbas/Desktop/tauq.pdf')

def resize_sax_1d(data):
        
    sax_1d_q = np.zeros(91)
    sax1d_Iq = np.zeros((1,91))
    sax_1d_q[0] = data.saxs_1d['q'][0]
    sax1d_Iq[0,0] = data.saxs_1d['Iq'][0,0]
    i=1

    for item in range(2,270,3):
        sax_1d_q[i] = data.saxs_1d['q'][item]
        sax1d_Iq[0,i] = data.saxs_1d['Iq'][0,item] 
        i += 1

    return sax_1d_q, sax1d_Iq

def plot_saxs_1d(a,b,c):

    saxs_1d_q, saxs1d_Iq = resize_sax_1d(a)

    plota_x = np.squeeze(saxs_1d_q)
    plota_y = np.squeeze(saxs1d_Iq)
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    #plt.setp(ax, xticks=[3e-2,1e-2,15e-1], yticks=[1,1.05,1.1,1.15])
    plt.setp(ax, xticks=[5e-3, 1e-2, 3e-2], yticks=[0.5e-5,1e-5,1e-4,1e-3,1e-2,1e-1])

    #ax.set_xscale('log')
    ax.set_ylim(0.5e-5, 1.5e-1)
    ax.set_xlim(2.2e-3, 7.5e-2)



    saxs_1d_q, saxs1d_Iq = resize_sax_1d(b)
    plotb_x = np.squeeze(saxs_1d_q)
    plotb_y = np.squeeze(saxs1d_Iq)

    saxs_1d_q, saxs1d_Iq = resize_sax_1d(c)
    plotc_x = np.squeeze(saxs_1d_q)
    plotc_y = np.squeeze(saxs1d_Iq)

    ax.plot(plota_x, plota_y, 'rs', label='Pendant Drop', markersize = 10, markerfacecolor='none')
    ax.plot(plotb_x, plotb_y, 'gv', label='CapCell', markersize = 10, markerfacecolor='none')
    ax.plot(plotc_x, plotc_y,'bo', label='Capillary', markersize = 10, markerfacecolor='none')
    #ax.plot(plotb_x, plotb_y, color = 'blue', label = 'CapCell', marker='.', markersize = 10)
    #ax.plot(plotc_x, plotc_y, color = 'yellow', label = 'Capillary', marker='d', markersize = 10)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ek = 1e-1
    ax.set_xlabel("q(Å"+str(ek)+")")
    ax.set_ylabel('Intensity')
    #plt.xticks(np.arange(min(saxs_1d_q), max(saxs_1d_q)+0.01, 0.02))
    #plt.xlim(1e-3, 7e-2, 2e-3)
    # plt.xticks([ 0.9e-2,1e-2, 2e-2])
    #plt.xlabel('', fontsize=5)
    plt.legend()
    #plt.show()


    plt.savefig('/Users/dozgulbas/Desktop/saxs1d.pdf')



def set_g2_fit(a, contrast):
    exp_arg = 1
    LB_list = [contrast, 1e-6, exp_arg, 0.95] 
    UB_list = [contrast, 1, exp_arg, 1.05]
    g2_fit = a.fit_g2(q_range=[0, 0.0092],t_range=[1e-8, 1e1], bounds=[LB_list,UB_list], fit_flag=[False, True, False, True])
    g2_fit_line = g2_fit["fit_line"]
    g2_fit_coeff = g2_fit["fit_val"]
    g2_tau = g2_fit_coeff[:,0,1]
    g2_tau_err = g2_fit_coeff[:,1,1]

    return g2_fit_line, g2_fit_coeff


if __name__ == "__main__":

    """Succsesful data files

    E0025_D100_CapCell_022C_att00_Rq0_00002_0001-100000.hdf
    D0024_D100_Capillary_022C_att00_Rq0_00048_0001-100000.hdf
    I0106_D100_Capillary_022C_att00_Rq0_00001_0001-100000.hdf

    """


    fn_path = "/Users/dozgulbas/APS_Data/"
    noisy_droplet = "F082_Pendant_NoCase_att01_Lq0_Rq0_00001_0001-100000.hdf"
    droplet = "F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00001_0001-100000.hdf"
    CapCell = "AvgE0025_D100_CapCell_022C_att00_Rq0_00001_0001-100000.hdf"
    capillary = "AvgD0024_D100_Capillary_022C_att00_Rq0_00001_0001-100000.hdf"
    glass = "AvgF0145_10nm_Glass_006C_att00_Rq0_00001_0001-100000.hdf"

    a = xf(droplet, cwd = fn_path)
    b = xf(CapCell, cwd = fn_path)
    c = xf(capillary, cwd = fn_path)
    d = xf(noisy_droplet, cwd = fn_path)
    e = xf(glass, cwd = fn_path)
    a2 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00002_0001-100000.hdf", cwd = fn_path)
    a3 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00003_0001-100000.hdf", cwd = fn_path)
    a4 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00004_0001-100000.hdf", cwd = fn_path)
    a5 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00005_0001-100000.hdf", cwd = fn_path)
    a6 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00006_0001-100000.hdf", cwd = fn_path)
    a7 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00007_0001-100000.hdf", cwd = fn_path)
    a8 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00008_0001-100000.hdf", cwd = fn_path)
    a9 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00009_0001-100000.hdf", cwd = fn_path)
    a10 = xf("F084_Pendant_WithCase_Cen_att00_Lq0_Rq0_00010_0001-100000.hdf", cwd = fn_path)

    d2 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00002_0001-100000.hdf", cwd = fn_path)
    d3 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00003_0001-100000.hdf", cwd = fn_path)
    d4 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00004_0001-100000.hdf", cwd = fn_path)
    d5 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00005_0001-100000.hdf", cwd = fn_path)
    d6 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00006_0001-100000.hdf", cwd = fn_path)
    d7 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00007_0001-100000.hdf", cwd = fn_path)
    d8 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00008_0001-100000.hdf", cwd = fn_path)
    d9 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00009_0001-100000.hdf", cwd = fn_path)
    d10 = xf("F082_Pendant_NoCase_att01_Lq0_Rq0_00010_0001-100000.hdf", cwd = fn_path)


    contrast_drop = 0.18 
    contrast_cell = 0.121
    contrast_cap = 0.121
    contrast_noisy_drop = 0.172
    contrast_glass = 0.14

    """Best contrast values for each setup
    Droplet: 0.1475
    CapCell: 0.121
    Capilarry: 0.121
    """
    
    num_rows = 3
    num_cols = 3

    cv_dim = num_rows*num_cols

    matplotlib.rc('font', size=20)  

    g2_fit_line, g2_fit_coeff = set_g2_fit(a,contrast_drop)
    g2_fit_line_b, g2_fit_coeff_b = set_g2_fit(b,contrast_cell)
    g2_fit_line_c, g2_fit_coeff_c = set_g2_fit(c,contrast_cap)
    g2_fit_line_d, g2_fit_coeff_d = set_g2_fit(d,contrast_noisy_drop)
    g2_fit_line_e,g2_fit_coeff_e = set_g2_fit(e,contrast_glass)

    # plot_g2_ROI6_before_normalization(a,num_rows,num_cols, g2_fit_line)
    # plot_g2_ROI6_after_normalization(a,num_rows,num_cols, g2_fit_line)
    plot_noisy_vs_normal(g2_fit_line, a,a2,a3,a4,a5,a6,a7,a8,a9,a10,d2,d3,d4,d5,d6,d7,d8,d9,d10)
    # plot_g2_before_normalization(a,b,c,e,g2_fit_line,g2_fit_line_b,g2_fit_line_c)
    # plot_g2_after_normalization(a,b,c,g2_fit_line,g2_fit_coeff,g2_fit_coeff_b,g2_fit_coeff_c,contrast_drop,contrast_cell,contrast_cap)
    # plot_g2_for_10_ROI(a,b,c,g2_fit_line,g2_fit_coeff,g2_fit_coeff_b,g2_fit_coeff_c,contrast_drop,contrast_cell,contrast_cap)
    # plot_tau_vs_q(a,b,c)
    # plot_saxs_1d(a,b,c)


    
