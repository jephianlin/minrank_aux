def eigens_multi(A):
    l=A.eigenvalues();
    eigens={};
    for i in l:
        eigens[i]=0;
    for i in l:
        eigens[i]+=1;
    return eigens;
    
def sort_dictionary(d):
    l=d.keys();
    l.sort();
    #print l;
    for key in l:
        print "%s:%s"%(key,d[key]);
    #print " ";

def canonical_label( g6 ):
    import subprocess;
    sp=subprocess.Popen("nauty-labelg", shell=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, close_fds=True)
    return sp.communicate(input='{0}\n'.format(g6))[0][:-1]
def canonical_copy( G ):
    return Graph( canonical_label( G.graph6_string()))
