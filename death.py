import os
import sys
from matplotlib.pyplot import axis
import pandas as pd
import warnings
import networkx as nx
from pyvis.network import Network

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))


def murder_graph(df):
    # Classify the data
    sources, targets, status, cause = df['Killer'], df['Victim'], df['Status'], df['Cause']

    # Create an empty network
    net = Network(height="100%", width="100%", bgcolor="#111111", font_color="pink", directed=True)

    # Compile edge data
    edge_data = zip(sources, targets, status, cause)

    # Create nodes and edges
    for src, dst, status, cause in edge_data:

        # Change color of nodes based on status
        if status == 'Alive':
            color = 'green'
        if status == 'Deceased':
            color = 'crimson'

        new_dst = dst

        # Check for numbered characters
        if any(char.isdigit() for char in dst):
            number = [char for char in dst if char.isdigit()]
            number = int(''.join(map(str,number)))
            if number == 1:
                new_dst = str(number)+' person'
            else:
                new_dst = str(number)+' people'
        
        # Add nodes and edges
        net.add_node(src, src, title=src, color=color)
        net.add_node(dst, new_dst, title=dst, color='crimson')
        net.add_edge(src, dst, title=cause, color='purple')
    
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