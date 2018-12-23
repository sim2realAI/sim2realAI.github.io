import numpy as np
import matplotlib.pyplot as plt

dataset_dict = {'NIST': 30,
                'PrincetonSB': 6670,
                'Thingi10K': 10000,
                'ModelNet': 151128,
                # 'ShapeNetSem': 12000,
                # 'ShapeNetCore': 51300,
                'ABC': 1000000,
                'ShapeNet': 3000000,
                }


dataset_name, datasets_size = list(dataset_dict.keys()), list(dataset_dict.values())
fig, ax = plt.subplots()

ind = np.arange(len(dataset_name))

ax.bar(ind, np.log10(datasets_size), width=0.35,
       color='aquamarine', label='datasets')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(dataset_name)
ax.legend()

plt.xticks(rotation=22)


plt.show()