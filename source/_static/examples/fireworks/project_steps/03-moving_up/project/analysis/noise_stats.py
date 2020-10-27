# import packages
import pandas as pd
from thot.thot import LocalProject

# initialize thot project
thot = LocalProject()

# get noise data from asset
noise_data = thot.find_asset( { 'type': 'noise-data' } )

# import noise data into a pandas data frame
df = pd.read_csv( noise_data.file, header = 0, index_col = 0, names = [ 'trial', 'volume' ] )

# compute statistics
stats = df.describe()

# create a new asset for the statistics
stats_properties = {
	'name': 'Noise Statistics',
	'type': 'noise-stats',
	'file': 'noise-stats.csv'
}

stats_path = thot.add_asset( stats_properties, 'noise_stats' )

# export the statistics to the new asset
stats.to_csv( stats_path ) 