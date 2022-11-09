import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    '''Load the dataset in “Scatter.xslx”. Make a figure composed of 3 subplots: 
       (a) PC1-PC2 scatter plot, (b) PC1 histogram, and (c) PC2 histogram. Use 
       different colors to distinguish different genotypes. Provide the legend at 
       the bottom-left corner.
    '''
    # Load the dataset and group them into 3 by Genotype.
    scatter_df = pd.read_excel('D:\python projects\data_science_lab05\Scatter.xlsx')
    cc = scatter_df.loc[scatter_df.Genotype == 0]
    Cc = scatter_df.loc[scatter_df.Genotype == 1]
    CC = scatter_df.loc[scatter_df.Genotype == 2]


    # Make 3 subplots with grid. Share x axis for center and bottom
    # subplots, and share y axis for center and left subplot.
    fig = plt.figure(figsize=(6, 5.5))
    grid = plt.GridSpec(3, 3, hspace=1, wspace=1)
    center_ax = plt.subplot(grid[:2, 1:])
    left_ax = plt.subplot(grid[:2, 0], sharey=center_ax)
    bottom_ax = plt.subplot(grid[2, 1:], sharex=center_ax)


    # Make the PC1-PC2 scatter plot in the center subplot.
    # For datas of which Genotypes is 0, use triangle makers with 'lightcoral' facecolor.
    # For datas of which Genotypes is 1, use round makers with 'yellow' facecolor.
    # For datas of which Genotypes is 2, use square makers with 'lightskyblue' facecolor. 
    center_ax.scatter(cc.PC1, cc.PC2, c='lightcoral', marker='^', 
                      edgecolors='k', 
                      lw=0.8, 
                      label='c/c', 
                      clip_on=False
                     ) 
    center_ax.scatter(Cc.PC1, Cc.PC2, c='yellow', marker='o', 
                      edgecolors='k',
                      lw=0.8,  
                      label='C/c'
                     )
    center_ax.scatter(CC.PC1, CC.PC2, c='lightskyblue', marker='s', 
                      edgecolors='k', 
                      lw=0.8, 
                      label='C/C', 
                      clip_on=False
                     )
    center_ax.set(xticks=np.arange(-400, 401, 200), 
                  yticks=np.arange(-400, 401, 200), 
                  xlim=(-400,400), 
                  title='Scatter Plot', 
                  xlabel='PC1', 
                  ylabel='PC2', 
                  clip_on=False
                 )
    # Ticks facing inwards. Show ticks on top and right sides
    center_ax.tick_params(direction='in', top=True, right=True)


    # Make the PC1 stacked histogram in the bottom subplot. Use same color as in the scatter 
    # plot to distinguish different genotypes. 
    bottom_ax.hist([cc.PC1,Cc.PC1,CC.PC1], 
                   color=['lightcoral','yellow','lightskyblue'], 
                   stacked=True, 
                   rwidth=0.85, 
                   edgecolor='k'
                 )
    bottom_ax.set(yticks=[0, 5, 10], xlabel='PC1', ylabel='Frequency')
    # Ticks facing inwards. Show ticks on top and right sides.
    bottom_ax.tick_params(direction='in', top=True, right=True)  



    # Make the PC2 stacked histogram in the left subplot. Use same color as in the scatter 
    # plot to distinguish different genotypes. 
    left_ax.hist([cc.PC2,Cc.PC2,CC.PC2], 
                 color=['lightcoral','yellow','lightskyblue'], 
                 stacked=True, 
                 rwidth=0.8, 
                 edgecolor='k', 
                 orientation='horizontal'
                )
    left_ax.set(xticks=[0, 5, 10], 
                yticks=np.arange(-400, 401, 200), 
                xlabel='Frequency', 
                ylabel='PC2'
               )
    # Ticks facing inwards. Show ticks on top and right sides.
    left_ax.tick_params(direction='in', top=True, right=True)  


    # Adjust for the location and appearance of the legend.
    center_ax.legend(bbox_to_anchor=(-0.5,-0.5), 
                     loc='center', 
                     fontsize='large', 
                     markerscale=2.7, 
                     fancybox=False,  # Disable rounded corners.
                     borderpad=0.6, 
                     edgecolor='k'
                    )
    
    # Save and show the figure.
    plt.savefig('Lab05_B.jpg', dpi=150)
    plt.show()
    


if __name__ == '__main__':
    main()