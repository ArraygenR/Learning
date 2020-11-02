import pandas as pd
left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key1': ['K0', 'K1', 'K2'],
                     'C': ['C0', 'C1', 'C3'],
                    'D': ['D0', 'D1', 'D3']})

result = pd.merge(left, right, how='outer', on=['key1'])
print(result)