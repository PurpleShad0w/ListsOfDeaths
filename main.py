import os
import sys
import pandas as pd
import warnings
from death import murder_graph
from death import kill_count
from death import kill_count_total
from death import cause_count
from death import cause_count_total

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Create the required folders
if not os.path.isdir('graphs'):
    os.mkdir('graphs')

# Load data
aot = pd.read_csv('death_lists/attack_on_titan.csv')
jojo = pd.read_csv('death_lists/jojo.csv')
ds = pd.read_csv('death_lists/demon_slayer.csv')

# Create graphs
murder_graph(aot).write_html('graphs/aot_who_killed_who_graph.html')
murder_graph(jojo).write_html('graphs/jojo_who_killed_who_graph.html')
murder_graph(ds).write_html('graphs/ds_who_killed_who_graph.html')

# Create kill counts
kill_count(aot).to_csv('kill_counts/aot_top_killers.csv')
kill_count(jojo).to_csv('kill_counts/jojo_top_killers.csv')
kill_count(ds).to_csv('kill_counts/ds_top_killers.csv')

# Create kill counts total
kill_count_total([aot,jojo,ds]).to_csv('kill_counts/top_killers.csv')

# Create cause counts
cause_count(aot).to_csv('cause_counts/aot_top_causes.csv')
cause_count(jojo).to_csv('cause_counts/jojo_top_causes.csv')
cause_count(ds).to_csv('cause_counts/ds_top_causes.csv')

# Create cause counts total
cause_count_total([aot,jojo,ds]).to_csv('cause_counts/top_causes.csv')