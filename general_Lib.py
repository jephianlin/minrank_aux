def canonical_label( g6 ):
    import subprocess;
    sp=subprocess.Popen("nauty-labelg", shell=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, close_fds=True)
    return sp.communicate(input='{0}\n'.format(g6))[0][:-1]
def canonical_copy( G ):
    return Graph( canonical_label( G.graph6_string()))
