from . import roles

def setup( app ):
	"""
	Initialize Sphinx roles.

	:param app: Sphinx.
	"""
	app.add_role( 'h2', roles.headers )