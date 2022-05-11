import os
import sys
import pandas as pd
import warnings
from death import murder_graph
from death import kill_count

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Create the required folders
if not os.path.isdir('graphs'):
    os.mkdir('graphs')

# Load data
aot = pd.read_csv('death_lists/attack_on_titan.csv')
aot_filtered = aot[(aot['Type'] == 'Individual') | (aot['Type'] == 'Group')]
jojo = pd.read_csv('death_lists/jojo.csv')
jojo_filtered = jojo[(jojo['Type'] == 'Individual') | (jojo['Type'] == 'Group')]

# Create graphs
murder_graph(aot_filtered).write_html('graphs/aot_who_killed_who_graph.html')
murder_graph(jojo_filtered).write_html('graphs/jojo_who_killed_who_graph.html')

# Create kill counts
kill_count(aot).to_csv('kill_counts/aot_top_killers.csv')
kill_count(jojo).to_csv('kill_counts/jojo_top_killers.csv')