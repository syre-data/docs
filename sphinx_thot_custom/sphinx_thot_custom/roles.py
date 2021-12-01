from docutils import nodes

def headers( name, rawtext, text, lineno, inliner, options = {}, content = [] ):
    """
    Basic headers role.


    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role.
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    
    :returns: Two part tuple containing list of nodes to insert into the
    	document and a list of system messages.  Both are allowed to be
    	empty.
    """
    header = nodes.container( f'<{name}>{text}</{name}>' )

    return ( [ header ], [] )