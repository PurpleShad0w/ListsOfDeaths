import os
import pandas as pd

deaths = pd.DataFrame(columns=['universe', 'victim', 'culprit'])


for path, subdirs, files in os.walk('Lists'):
    for name in files:
        file = path + '\\' + name
        universe = file.split('\\')[1::2][0]
        
        with open(file, 'r') as f:
            lines = f.read().split('\n')
        
        for line in lines:
            victim = line.split('**')[1::2][0]
            culprits = line.split('_')[1::2]

            for culprit in culprits:
                if culprit == 'suicide':
                    culprit = victim
                
                row = [universe, victim, culprit]
                deaths.loc[len(deaths)] = row

print(deaths)
print(deaths.groupby(by=['universe', 'culprit']).count())