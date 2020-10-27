import pandas as pd
from thot.thot import ThotProject

# intialize thot
thot = ThotProject()

# prepare data
recipe_stats = thot.find_assets( { 'type': 'recipe-stats' } )

df = []
for stat in recipe_stats:
    # read data for each recipe
    tdf = pd.read_pickle( stat.file )
    tdf.rename( { 0: stat.metadata[ 'recipe' ] }, axis = 1, inplace = True  )
    
    df.append( tdf )

# combine into one dataframe
df = pd.concat( df, axis = 1 )

# export data as csv for reading
comparison_properites = {
	'name': 'Recipe Comparison',
	'type': 'recipe-comparison',
	'file': 'recipe_comparison.csv' 
}

comparison_path = thot.add_asset( comparison_properites, 'recipe_comparison' )
df.to_csv( comparison_path )

# create bar char and export
means = df.loc[ 'mean' ]
errs = df.loc[ 'std' ]

ax = means.plot( kind = 'bar', yerr = errs )

bar_properties = {
	'name': 'Recipe Comparison',
	'type': 'recipe-bar-chart',
	'tags': [ 'chart', 'image' ],
	'file': 'recipe_comparison.png'
}

bar_path = thot.add_asset( bar_properties, 'recipe_bar' )
ax.get_figure().savefig( bar_path, format = 'png' )