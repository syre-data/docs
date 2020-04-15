# include packages
import pandas as pd
from thot.thot import LocalProject

# initialize thot
thot = LocalProject()

# get recipe container
recipe = thot.find_container( { '_id': thot.root } )

# get noise statistice data
noise_stats = thot.find_assets( { 'type': 'noise-stats' } )

df = []
for stat in noise_stats:
	# read data for each batch
	tdf = pd.read_csv( 
		stat.file, 
		names = ( stat.metadata[ 'batch' ] ), 
		index_col = 0, 
		header = 0 
	)
	
	df.append( tdf )

# combine into one dataframe
df = pd.concat( df, axis = 1 )

# plot the data

# export the plot


# compute recipe statistics
stats = df

# export recipe statistics
stat_properties = {
	'name': '{} Statistics'.format( recipe.name ),
	'type': 'recipe-stats',
	'file': 'recipe-stats.csv'
}

stats_path = thot.add_asset( stat_properties, 'recipe_stats' )
stats.to_csv( stats_path )