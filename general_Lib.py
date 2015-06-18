def empty_array(m,n):
    """
    Input: int m,n;
    Output: the two-dimension array contains m copies of [0]*n;
    """
    a=[];
    for i in range(m):
        a.append([0]*n);
    return a;
    
def all_one_matrix(m,n):
    """
    Input: int m,n;
    Output: the all one matrix of size m x n;
    """
    return matrix(m,[1]*(m*n));  

def elementary_matrix(i,j,m,n=None):
    """
    Input: int i,j,m,n; if n is not assigned, then n=m;
    Output: an m x n elementary matrix whose i,j-entry is 1 while all others are 0;
    ## starting from 0th column and 0th row;
    """
    if n==None:
        n=m;
    a=[0]*(m*n);
    a[i*n+j]=1;
    return matrix(m,a);

def eigens_multi(A):
    """
    Input: matrix A;
    Output: the dictionary of {eigenvalues: multiplicity};
    """
    l=A.eigenvalues();
    eigens={};
    for i in l:
        eigens[i]=0;
    for i in l:
        eigens[i]+=1;
    return eigens;
    
def sort_dictionary(d):
    """
    Input: dict d;
    Output: print key: value following the order of keys;
    """
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
