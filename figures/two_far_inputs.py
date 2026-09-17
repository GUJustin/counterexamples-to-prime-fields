"""Schematic of the exact distance profile; no numerical data are inferred."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib as mpl
BASE=Path(__file__).resolve().parent
mpl.rcParams.update({'font.family':'serif','font.size':10,'mathtext.fontset':'cm','pdf.fonttype':42})
fig,ax=plt.subplots(figsize=(6.25,2.35))
fig.subplots_adjust(left=.19,right=.90,bottom=.22,top=.93)
r=10;level=r/(2*r+1)
ax.axhline(1,color='.55',lw=.8,ls=(0,(3,3)))
ax.axhline(0,color='.55',lw=.8)
ax.plot([0,1],[level,level],ls='',marker='s',ms=6,color='#993E2B',zorder=3)
ax.vlines([0,1],0,level,color='.7',lw=.7,linestyles='dotted')
ax.plot([2,3,4,5,7,8],[0]*6,ls='',marker='o',ms=5,color='#245B7C',zorder=3)
ax.text(6,0,r'$\cdots$',ha='center',va='center',color='#245B7C',bbox={'facecolor':'white','edgecolor':'none','pad':1})
for x,label in [(0,r'$u$'),(1,r'$v$')]:ax.text(x,level+.065,label,ha='center',va='bottom',fontsize=12)
ax.text(5,.22,r'all $p-2$ other parameters',ha='center',va='center')
ax.text(5,.105,r'distance exactly $\theta$',ha='center',va='center')
ax.annotate('',xy=(8.6,1),xytext=(8.6,0),arrowprops={'arrowstyle':'<->','lw':.85,'color':'.35'})
ax.text(8.77,.5,r'$\eta$',ha='left',va='center',fontsize=12)
ax.set_yticks([0,level,1],[r'$\theta$',r'$\theta+r/n$',r'$1-\rho$'])
ax.set_xticks([0,1,2,3,4,5,7,8],[r'$0$',r'$1$',r'$2$',r'$3$','', '',r'$p-2$',r'$p-1$'])
ax.set_xlabel(r'field parameter $z$ in $(1-z)u+zv$ (schematic)',labelpad=7)
ax.set_xlim(-.4,9);ax.set_ylim(-.12,1.1)
ax.spines[['right','top','left']].set_visible(False)
ax.spines['bottom'].set_position(('data',-.10));ax.spines['bottom'].set_color('.65')
ax.tick_params(axis='y',length=0,pad=8);ax.tick_params(axis='x',length=0,pad=5)
fig.savefig(BASE/'two_far_inputs.pdf')
fig.savefig(BASE/'two_far_inputs.png',dpi=180)
plt.close(fig)
