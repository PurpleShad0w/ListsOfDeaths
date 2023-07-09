import os
import pandas as pd

kills = pd.DataFrame(columns=['universe', 'culprit', 'count', 'victims'])
deaths = pd.DataFrame(columns=['universe', 'victim', 'culprits', 'observer dependent', 'final'])


for path, subdirs, files in os.walk('Lists'):
    for name in files:
        file = path + '\\' + name
        universe = file.split('\\')[1::2][0]
        
        with open(file, 'r') as f:
            lines = f.read().split('\n')
        
        for line in lines:
            victim = line.split('**')[1::2][0]
            culprits = line.split('_')[1::2]

            if '(observer dependent)' in line:
                observer = True
            else:
                observer = False
            
            if '(later revived)' in line or '(later resurrected)' in line:
                final = False
            else:
                final = True

            for i in range(len(culprits)):
                if culprits[i] == 'suicide':
                    culprits[i] = victim

                row = [universe, culprits[i], 1, victim]
                kills.loc[len(kills)] = row

            row = [universe, victim, culprits, observer, final]
            deaths.loc[len(deaths)] = row


kills = kills.groupby(by=['universe', 'culprit']).aggregate({'count':sum, 'victims':', '.join}).reset_index().sort_values(by='count', ascending=False)