import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    ''' Plot the data in 'Score.csv' with a horizontal stacked bar chart. 
        Use different colors to distinguish different teams and 
        put the leader’s name in the middle of the bar.
    '''
    # Load the data in as panda data frame. Group them by teams.
    score_df = pd.read_csv('Score.csv')
    TeamD = score_df.loc[score_df.Team=='D']
    TeamK = score_df.loc[score_df.Team=='K']
    TeamP = score_df.loc[score_df.Team=='P']


    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 5))


    # Plot data of Team D with a horizontal bar.
    barD = ax.barh(TeamD.Round, TeamD.Score, 
                   height=0.6, 
                   color=['yellowgreen'], 
                   edgecolor='white', 
                   label='Team D', 
                   zorder=2  # for bars to appear before the grid
                  )
    # Label the leaders' names at the center of each bar.
    ax.bar_label(barD, labels=TeamD.Leader, 
                 label_type='center', 
                 fontsize='large'
                )


    # Plot data of Team K with a horizontal bar.
    barK = ax.barh(TeamK.Round, TeamK.Score, 
                   left=TeamD.Score, 
                   height=0.6, 
                   color=['cornflowerblue'], 
                   edgecolor='white', 
                   label='Team K', 
                   zorder=2
                  )
    # Label the leaders' names at the center of each bar.
    ax.bar_label(barK, labels=TeamK.Leader, 
                 label_type='center', 
                 fontsize='large'
                )


    # Plot data of Team P with a horizontal bar.
    barP = ax.barh(TeamP.Round, TeamP.Score, 
                   left= TeamD.Score[:3].to_numpy() + TeamK.Score[:3].to_numpy(), 
                   height=0.6, 
                   color=['orange'],
                   edgecolor='white', 
                   label='Team P', 
                   zorder=2
                  )
    # Label the leaders' names at the center of each bar.              
    ax.bar_label(barP, labels=TeamP.Leader, 
                 label_type='center', 
                 fontsize='large'
                )


    # Set the appearance of the figure.
    ax.spines['top'].set_visible(False)  # Hide top spine.
    ax.spines['right'].set_visible(False)  # Hide right spine.
    ax.spines['bottom'].set_visible(False)  # Hide bottom spine.

    ax.xaxis.set_ticks_position('top')
    ax.tick_params(top=False, left=False)  # Hide ticks
    # Set tick params of x axis to color gray
    ax.tick_params(colors='gray', axis='x', labelsize='large')


    # Set the title, plot boundary, and legend appearance
    ax.set_title('Points', fontsize='x-large')
    ax.set_xlim(right=165)
    plt.grid(axis='x')
    plt.legend(loc='lower right', handlelength=0.7, 
               borderpad=1, labelspacing=1.2)


    # Save and show the figure.
    plt.savefig('Lab05_C.jpg', dpi=150)
    plt.show()


if __name__=='__main__':
    main()