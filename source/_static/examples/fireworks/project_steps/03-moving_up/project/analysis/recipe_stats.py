# include packages
import pandas as pd
from thot import ThotProject

# initialize thot
db = ThotProject()

# get recipe container
recipe = db.find_container( { '_id': db.root } )

# get noise statistics data
noise_stats = db.find_assets( { 'type': 'noise-stats' } )

# create combined dataframe 
df = []
for stat in noise_stats:
	# read data for each batch
	tdf = pd.read_csv( 
		stat.file, 
		names = [ stat.metadata[ 'batch' ] ], 
		index_col = 0, 
		header = 0 
	)
	
	df.append( tdf )

df = pd.concat( df, axis = 1 )

# compute recipe statistics
mean = df.loc[ 'mean' ].mean() 
std = df.loc[ 'std' ].pow( 2 ).sum()/ 4 

stats = pd.DataFrame( [ mean, std ], index = ( 'mean', 'std' ) )

# export recipe statistics
stat_properties = {
	'name': '{} Statistics'.format( recipe.name ),
	'type': 'recipe-stats',
	'file': 'recipe-stats.pkl'
}

stats_path = db.add_asset( stat_properties, 'recipe_stats' )
stats.to_pickle( stats_path )