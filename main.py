import os
import sys
import pandas as pd
import warnings
from death import murder_graph
from death import kill_count
from death import kill_count_total
from death import cause_count
from death import cause_count_total
from death import death_count
from death import death_list_combiner

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Create the required folders
if not os.path.isdir('graphs'):
    os.mkdir('graphs')

# Load data
attack_on_titan = pd.read_csv('death_lists/attack_on_titan.csv')
deadman_wonderland = pd.read_csv('death_lists/deadman_wonderland.csv')
demon_slayer = pd.read_csv('death_lists/demon_slayer.csv')
jojos_bizarre_adventure = pd.read_csv('death_lists/jojos_bizarre_adventure.csv')
just_cause = pd.read_csv('death_lists/just_cause.csv',encoding='ANSI')
my_hero_academia = pd.read_csv('death_lists/my_hero_academia.csv')
the_world_ends_with_you = pd.read_csv('death_lists/the_world_ends_with_you.csv')

# Create graphs
murder_graph(attack_on_titan).write_html('graphs/attack_on_titan_who_killed_who.html')
murder_graph(deadman_wonderland).write_html('graphs/deadman_wonderland_who_killed_who.html')
murder_graph(demon_slayer).write_html('graphs/demon_slayer_who_killed_who.html')
murder_graph(jojos_bizarre_adventure).write_html('graphs/jojos_bizarre_adventure_who_killed_who.html')
murder_graph(just_cause).write_html('graphs/just_cause_who_killed_who.html')
murder_graph(my_hero_academia).write_html('graphs/my_hero_academia_who_killed_who.html')
murder_graph(the_world_ends_with_you).write_html('graphs/the_world_ends_with_you_who_killed_who.html')

# Create kill counts
kill_count(attack_on_titan).to_csv('counts/attack_on_titan_top_killers.csv')
kill_count(deadman_wonderland).to_csv('counts/deadman_wonderland_top_killers.csv')
kill_count(demon_slayer).to_csv('counts/demon_slayer_top_killers.csv')
kill_count(jojos_bizarre_adventure).to_csv('counts/jojos_bizarre_adventure_top_killers.csv')
kill_count(just_cause).to_csv('counts/just_cause_top_killers.csv')
kill_count(my_hero_academia).to_csv('counts/my_hero_academia_top_killers.csv')
kill_count(the_world_ends_with_you).to_csv('counts/the_world_ends_with_you_top_killers.csv')

# Create kill counts total
kill_count_total([attack_on_titan,deadman_wonderland,demon_slayer,jojos_bizarre_adventure,just_cause,my_hero_academia,the_world_ends_with_you],
    ['attack_on_titan','deadman_wonderland','demon_slayer','jojos_bizarre_adventure','just_cause','my_hero_academia','the_world_ends_with_you']).to_csv('counts/killers.csv')

# Create cause counts
cause_count(attack_on_titan).to_csv('counts/attack_on_titan_top_causes.csv')
cause_count(deadman_wonderland).to_csv('counts/deadman_wonderland_top_causes.csv')
cause_count(demon_slayer).to_csv('counts/demon_slayer_top_causes.csv')
cause_count(jojos_bizarre_adventure).to_csv('counts/jojos_bizarre_adventure_top_causes.csv')
cause_count(just_cause).to_csv('counts/just_cause_top_causes.csv')
cause_count(my_hero_academia).to_csv('counts/my_hero_academia_top_causes.csv')
cause_count(the_world_ends_with_you).to_csv('counts/the_world_ends_with_you_top_causes.csv')

# Create cause counts total
cause_count_total([attack_on_titan,deadman_wonderland,demon_slayer,jojos_bizarre_adventure,just_cause,my_hero_academia,the_world_ends_with_you]).to_csv('counts/causes.csv')

# Create total death count
death_count([attack_on_titan,deadman_wonderland,demon_slayer,jojos_bizarre_adventure,just_cause,my_hero_academia,the_world_ends_with_you],
    ['attack_on_titan','deadman_wonderland','demon_slayer','jojos_bizarre_adventure','just_cause','my_hero_academia','the_world_ends_with_you']).to_csv('counts/death_count.csv')

# Combine death lists
death_list_combiner([attack_on_titan,deadman_wonderland,demon_slayer,jojos_bizarre_adventure,just_cause,my_hero_academia,the_world_ends_with_you],
    ['attack_on_titan','deadman_wonderland','demon_slayer','jojos_bizarre_adventure','just_cause','my_hero_academia','the_world_ends_with_you']).to_csv('death_lists/death_list.csv')