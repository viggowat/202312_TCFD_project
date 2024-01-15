import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
import cartopy as ctp
import cartopy.feature as cfeature

comps = pd.read_csv('comp_examples.csv')

sns.set(style="whitegrid", font_scale=2)

# Colours and labels for legend
import matplotlib.colors
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#ef476f', '#3a86ff', '#06d6a0'])
label = ('Semiconductor','Pharmaceuticals', 'Real estate development')

## worldmap
fig = plt.figure(figsize=(24, 16))
ax = fig.add_subplot(1,1,1, projection=ccrs.EckertIV())
ax.add_feature(cfeature.COASTLINE, edgecolor='#BDBDBD')
ax.add_feature(cfeature.BORDERS, edgecolor='#BDBDBD')
ax.add_feature(ctp.feature.OCEAN,facecolor='#D7D7D7')
ax.set_global()

## scatter
x = comps['Longitude']
y = comps['Latitude']
z = comps['Company_ID']
scatter = ax.scatter(x, y, s=25, c=z, cmap= cmap, transform=ccrs.PlateCarree())

# Shrink current axis's height by 10% on the bottom (preparation for axis location)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Extract handles for legend
handles = scatter.legend_elements(num=[0,1,2,3,4,5])[0]  # extract the handles from the existing scatter plot

lgnd = ax.legend(title='Protection by habitat',
                 handles=handles,    # pass extracted handles to legend
                 labels=label,    # pass label string
                 loc='upper center',           # Put legend below current axis
                 bbox_to_anchor=(0.5, -0.05),
                 fancybox=True, 
                 ncol=5,
                 markerscale=2)

lgnd.set_title(title='Company example')

# save fig
plt.savefig('comp_examples_map.png',bbox_inches = 'tight')

# show fig
plt.show()
