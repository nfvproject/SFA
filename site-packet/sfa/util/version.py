### updated by the toplevel Makefile
version_tag="-"
scm_url="should-be-redefined-by-specfile"
import socket
 
def version_core (more=None):
    if more is None: more={}
    core = { 'code_tag' : version_tag,
             'code_url' : scm_url,
             'hostname' : socket.gethostname(),
             }
    core.update(more)
    return core
