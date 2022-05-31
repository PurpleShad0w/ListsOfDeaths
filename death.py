import os
import sys
import pandas as pd
import warnings
from pyvis.network import Network

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))


def murder_graph(df):
    # Classify the data
    sources, targets, cause = df['Killer'], df['Victim'], df['Cause']

    # Create an empty network
    net = Network(height="100%", width="100%", bgcolor="#111111", font_color="#e8ac87", directed=True)

    # Compile edge data
    edge_data = zip(sources, targets, cause)

    # Create nodes and edges
    for src, dst, cause in edge_data:

        # Change color of nodes based on status
        if targets.eq(src).any():
            color = 'crimson'
        else:
            color = 'green'

        new_dst = dst
        new_src = src

        # Check for numbered characters in victims
        if any(char.isdigit() for char in dst):
            number = [char for char in dst if char.isdigit()]
            number = int(''.join(map(str,number)))
            if number == 1:
                new_dst = str(number)+' person'
            else:
                new_dst = str(number)+' people'
        
        # Check for numbered characters in killers
        if any(char.isdigit() for char in src):
            number = [char for char in src if char.isdigit()]
            number = int(''.join(map(str,number)))
            if number == 1:
                new_src = str(number)+' person'
            else:
                new_src = str(number)+' people'

        # Add nodes and edges
        net.add_node(src, label=new_src, title=src, color=color)
        net.add_node(dst, label=new_dst, title=dst, color='crimson')
        net.add_edge(src, dst, title=cause, color='#eb73b7')
    
    # Prevent edge color overlap
    net.inherit_edge_colors(False)

    # Set smooth edges
    net.set_edge_smooth('dynamic')

    # Output the graph
    return(net)


def kill_count(df):
    # Initiate dataframe
    kills = pd.DataFrame({'Killer':0,'Kills':0},index=(0,1))

    # Attribute kills to each killer
    for i in range(len(df)):
        victim = df.loc[i,'Victim']
        if any(char.isdigit() for char in victim):
            number = [char for char in victim if char.isdigit()]
            number = int(''.join(map(str,number)))
        else:
            number = 1
        s = {'Killer':df.loc[i,'Killer'],'Kills':number}
        kills = kills.append(s,ignore_index=True)
    
    # Clean and sort dataframe
    kills = kills[kills['Kills'] != 0]
    kills = kills.groupby('Killer').sum()
    kills = kills.sort_values(by='Kills',ascending=False)

    # Output the data
    return(kills)