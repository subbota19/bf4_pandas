from bs import main_table
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(16, 16)

census_2011 = [int(''.join(x.split(','))) for x in main_table['census_2011']]
census_2015 = [int(''.join(x.split(','))) for x in main_table['census_2015']]
land_area = [int(float(x[:-3])) for x in main_table['land_area']]
ax.set(xlabel='area', ylabel='populations', title='Ratio between population and square area city in Germany')
ax.scatter(land_area, census_2011, marker='o').set_label('census_2011')
ax.scatter(land_area, census_2015, marker='o').set_label('census_2015')

ax.legend()

for i, text in enumerate(main_table['cities']):
    ax.annotate(text, (land_area[i], census_2011[i]))
    if census_2011[i] < 500_000:
        break
plt.grid(True)
plt.savefig(fname='graphic.png')
plt.show()
