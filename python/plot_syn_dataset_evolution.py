import numpy as np
import matplotlib.pyplot as plt
import operator
from collections import OrderedDict

dataset_dict = {'NIST': 30,
                'IKEA': 219,
                'PrincetonSB': 6670,
                'Thingi10K': 10000,
                'ObjectNet3D': 44161,
                'ModelNet': 151128,
                # 'ShapeNetSem': 12000,
                # 'ShapeNetCore': 51300,
                'ABC': 1000000,
                'ShapeNet': 3000000,
                }

dataset_dict = OrderedDict(sorted(dataset_dict.items(), key=lambda x: x[1]))

# print(dataset_dict)

dataset_name, datasets_size = list(dataset_dict.keys()), list(dataset_dict.values())
fig, ax = plt.subplots()

ind = np.arange(len(dataset_name))

ax.bar(ind[:-1], np.log10(datasets_size[:-1]), width=0.35,
       color='aquamarine', #label='datasets'
       )

ax.bar(ind[-1], np.log10(datasets_size[-1]), width=0.35,
       color='aquamarine', alpha=0.4)

ax.set_ylabel('Dataset size (in logarithmic scale)')
ax.set_title('Object datasets')
ax.set_xticks(ind)
ax.set_xticklabels(dataset_name)
ax.legend()

plt.xticks(rotation=22)


plt.show()