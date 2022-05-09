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

# Load Attack on Titan data
aot = pd.read_csv('death_lists/attack_on_titan.csv')
aot_filtered = aot[(aot['Type'] == 'Individual') | (aot['Type'] == 'Group')]

# Create graph and kill count
murder_graph(aot_filtered).write_html('graphs/aot_who_killed_who_graph.html')
kill_count(aot).to_csv('kill_counts/aot_top_killers.csv')