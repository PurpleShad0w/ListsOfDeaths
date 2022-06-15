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

        # Check for multiple killers
        if '&' in src:
            src = src.split(' & ')
            for s in src:
                net.add_node(s, label=s, color=color)
                net.add_node(dst, label=new_dst, title=dst, color='crimson')
                net.add_edge(s, dst, title=cause, color='#eb73b7')
        else:
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

        # Check for number of victims
        victim = df.loc[i,'Victim']
        if any(char.isdigit() for char in victim):
            number = [char for char in victim if char.isdigit()]
            number = int(''.join(map(str,number)))
        else:
            number = 1
        
        # Check for multiple killers
        killer = df.loc[i,'Killer']
        if '&' in killer:
            killer = killer.split(' & ')
            for k in killer:
                s = {'Killer':k,'Kills':number}
                kills = kills.append(s,ignore_index=True)
        else:
            s = {'Killer':killer,'Kills':number}
            kills = kills.append(s,ignore_index=True)
    
    # Clean and sort dataframe
    kills = kills[kills['Kills'] != 0]
    kills = kills.groupby('Killer').sum()
    kills = kills.sort_values(by='Kills',ascending=False)

    # Output the data
    return(kills)


def kill_count_total(arr,names):
    # Initiate dataframe
    kills = pd.DataFrame({'Killer':0,'Kills':0,'Universe':0},index=(0,1))
    n = 0

    # Attribute kills to each killer
    for df in arr:

        # Set universe
        universe = names[n]
        universe = universe.replace('_',' ')
        universe = universe.title()
        n+=1

        for i in range(len(df)):

            # Check for number of victims
            victim = df.loc[i,'Victim']
            if any(char.isdigit() for char in victim):
                number = [char for char in victim if char.isdigit()]
                number = int(''.join(map(str,number)))
            else:
                number = 1

            # Check for multiple killers
            killer = df.loc[i,'Killer']
            if '&' in killer:
                killer = killer.split(' & ')
                for k in killer:
                    s = {'Killer':k,'Kills':number,'Universe':universe}
                    kills = kills.append(s,ignore_index=True)
            else:
                s = {'Killer':killer,'Kills':number,'Universe':universe}
                kills = kills.append(s,ignore_index=True)
    
    # Clean and sort dataframe
    kills = kills[kills['Kills'] != 0]
    kills = kills.groupby([kills['Killer'],kills['Universe']]).sum()
    # kills = kills.sort_values(by='Kills',ascending=False)

    # Output the data
    return(kills)


def cause_count(df):
    # Initiate dataframe
    causes = pd.DataFrame({'Cause':0,'Deaths':0},index=(0,1))

    # Attribute deaths to each cause
    for i in range(len(df)):

        # Check for number of victims
        victim = df.loc[i,'Victim']
        if any(char.isdigit() for char in victim):
            number = [char for char in victim if char.isdigit()]
            number = int(''.join(map(str,number)))
        else:
            number = 1

        s = {'Cause':df.loc[i,'Cause'],'Deaths':number}
        causes = causes.append(s,ignore_index=True)
    
    # Clean and sort dataframe
    causes = causes[causes['Deaths'] != 0]
    causes = causes.groupby('Cause').sum()
    causes = causes.sort_values(by='Deaths',ascending=False)

    # Output the data
    return(causes)


def cause_count_total(arr):
    # Initiate dataframe
    causes = pd.DataFrame({'Cause':0,'Deaths':0},index=(0,1))

    # Attribute deaths to each cause
    for df in arr:
        for i in range(len(df)):

            # Check for number of victims
            victim = df.loc[i,'Victim']
            if any(char.isdigit() for char in victim):
                number = [char for char in victim if char.isdigit()]
                number = int(''.join(map(str,number)))
            else:
                number = 1

            s = {'Cause':df.loc[i,'Cause'],'Deaths':number}
            causes = causes.append(s,ignore_index=True)
    
    # Clean and sort dataframe
    causes = causes[causes['Deaths'] != 0]
    causes = causes.groupby('Cause').sum()
    # causes = causes.sort_values(by='Deaths',ascending=False)

    # Output the data
    return(causes)

def death_count(arr,names):
    # Initiate dataframe
    deaths = pd.DataFrame({'Universe':0,'Deaths':0},index=(0,1))
    n = 0

    # Count deaths
    for df in arr:

        # Set universe
        universe = names[n]
        universe = universe.replace('_',' ')
        universe = universe.title()
        n+=1

        for i in range(len(df)):

            # Check for number of victims
            victim = df.loc[i,'Victim']
            if any(char.isdigit() for char in victim):
                number = [char for char in victim if char.isdigit()]
                number = int(''.join(map(str,number)))
            else:
                number = 1

            s = {'Universe':universe,'Deaths':number}
            deaths = deaths.append(s,ignore_index=True)
    
    # Create a total
    total = deaths['Deaths'].sum()
    s = {'Universe':'total','Deaths':total}
    deaths = deaths.append(s,ignore_index=True)

    # Clean and sort dataframe
    deaths = deaths[deaths['Deaths'] != 0]
    deaths = deaths.groupby('Universe').sum()
    # deaths = deaths.sort_values(by='Deaths',ascending=False)

    # Output the data
    return(deaths)

def death_list_combiner(arr,names):
    # Initiate dataframe
    deaths = pd.DataFrame({'Victim':0,'Killer':0,'Cause':0,'Universe':0},index=(0,1))
    n = 0

    # Gather deaths
    for df in arr:

        # Set universe
        universe = names[n]
        universe = universe.replace('_',' ')
        universe = universe.title()
        n+=1

        for i in range(len(df)):
            s = {'Victim':df.loc[i,'Victim'],'Killer':df.loc[i,'Killer'],'Cause':df.loc[i,'Cause'],'Universe':universe}
            deaths = deaths.append(s,ignore_index=True)
    
    # Clean and sort dataframe
    deaths = deaths[deaths['Victim'] != 0]
    deaths = deaths.groupby([deaths['Victim'],deaths['Killer'],deaths['Cause'],deaths['Universe']]).count()
    deaths = deaths.astype(str).sort_values(by='Victim')

    # Output the data
    return(deaths)