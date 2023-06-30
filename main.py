import os
import pandas as pd

deaths = pd.DataFrame(columns=['universe', 'victim', 'culprit', 'observer dependent', 'final'])


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

            for culprit in culprits:
                if culprit == 'suicide':
                    culprit = victim
                
                row = [universe, victim, culprit, observer, final]
                deaths.loc[len(deaths)] = row

deaths.groupby(by=['universe', 'culprit']).count().sort_values(by='victim', ascending=False)