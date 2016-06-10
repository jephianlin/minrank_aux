print "---sshow, empty_array, all_one_matrix, elementary_matrix, eigens_multi, sort_dictionary, has_minor, etc."

import random; #If this line is not included, random.choice should be changed to choice.

def sshow(g,stg=None):
    if stg==None:
        stg=g.graph6_string();
    g.show(figsize=[2,2],vertex_labels=False,vertex_size=50,title="%s: %s"%(g.order(),stg));

#######
#Predictions
#######

def lagrange_prediction(a,b,trust=3,variable="c"):
    """
    Input: two lists a and b.
    Output: the prediction relation of b as a function of a.
    Description: the algorithm will find f_i as the lagrange_polynomial of the first i pairs. 
    When f_i remains the same as i increase trust times, the algorithm stops and return f_i.
    """
    n=min(len(a),len(b));
    R=PolynomialRing(QQ,variable);
    data=[];
    f=0;
    believe=0;
    for i in range(n):
        data.append((a[i],b[i]));
        new_f=R.lagrange_polynomial(data);
        if f!=new_f:
            f=new_f;
        else:
            believe+=1;
        if believe>=trust:
            return f;
    verbose("Not enough data or un-polynomial-related data.",level=2); ##use set_verbose(2) to see this line.
    return f;

#######
#List Operations
#######

def list_intersection(A,B):
    """
    A,B are lists; 
    return all element in B that is appeared in A, which is usually the intersection of them.
    """
    inter=[]
    for b in B:
        if b in A:
            inter.append(b);
    return inter;

#######
#Matrices
#######
    
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

def var_matrix(g):
    """
    Input:
        g: a simple graph
    Output:
        a matrix with variable a1_j on ij-entry if ij is an edge, and a variable di on diagonal.
    
    """
    n=g.order()
    A=matrix(n,[var("x")]*(n^2));
    E=g.edges(labels=False);
    Ebar=g.complement().edges(labels=False);
    V=g.vertices();
    for v in V:
        A[v,v]=var("d%s"%v);
    for e in E:
        i=min(e);
        j=max(e);
        A[i,j]=var("a%s_%s"%(i,j));
        A[j,i]=var("a%s_%s"%(i,j));
    for e in Ebar:
        i,j=e;
        A[i,j]=0;
        A[j,i]=0; 
    return A;

def latex_matrix(A):
    m,n=A.dimensions();
    print "\\begin{bmatrix}"
    for i in range(m):
        for j in range(n-1):
            print A[i][j], "&",;
        print A[i][n-1], "\\\\";
    print "\\end{bmatrix}"

def distinct_eigens(A,dgable=True):
    if dgable==True:
        return A.minimal_polynomial().degree();
    if dgable==False:
        return len(set(g.distance_matrix().eigenvalues()));

def inertia(D):
    egv=D.eigenvalues();
    n=len(egv);
    p=0;
    m=0;
    z=0;
    for i in range(n):
        if egv[i]<0:
            m+=1;
        if egv[i]>0:
            p+=1;
    return [p,m,z];

def list_to_multi(l):
    """
    Input: list l;
    Output: the dictionary of {values: number of occurrence};
    """
    newdict={};
    for i in l:
        newdict[i]=0;
    for i in l:
        newdict[i]+=1;
    return newdict;
    
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

def distance_decom(g):
    n=g.order();
    diam=g.diameter();
    D=g.distance_matrix();
    DD={};
    for i in range(0,diam+1):
        DD[i]=[];
        for j in range(n):
            DD[i].append([0]*n);
    for i in range(n):
        for j in range(n):
            dist=D[i][j];
            DD[dist][i][j]=1;
    decom=[];
    for i in range(0,diam+1):
        decom.append(matrix(DD[i]));
    return decom;
    
def commutative_family(mtxs):
    ## import as list;
    n=len(mtxs);
    commu=True;
    for pair in Combinations(range(n),2):
        if mtxs[pair[0]]*mtxs[pair[1]]!=mtxs[pair[1]]*mtxs[pair[0]]:
            commu=False;
            break;
    return commu;    
    
def similar(A,Q):
    ## input A, Q and output Q^-1AQ
    return Q.inverse()*A*Q;

#######
#Minor
#######

## This paragraph comes from http://ask.sagemath.org/question/
## 8112/graph-minor-code-too-slow-in-certain-situations-sage-46/
def has_minor(G, H):
    try:
        m = G.minor(H)
        return True
    except ValueError: 
        return False

#######
#Label
#######

def naughy_label( g6 ):
    ## Return the canonical label given by naughty instead of Sage.
    ## Input should be a string.
    import subprocess;
    sp=subprocess.Popen("nauty-labelg", shell=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, close_fds=True)
    return sp.communicate(input='{0}\n'.format(g6))[0][:-1]
def canonical_copy( G ):
    return Graph( naughy_label( G.graph6_string()))

#######
#Building Graphs
#######

def contract_edge(gph,e):
    if gph.has_edge(e)==False:
        raise ValueError, "not an edge";
    ngh1=gph.neighbors(e[0]);
    ngh2=gph.neighbors(e[1]);
    h=gph.copy();
    h.delete_vertices([e[0],e[1]]);
    try_again=True;
    i=0;
    while try_again:
        i+=1;
        if h.has_vertex(i)==False:
            h.add_vertex(i);
            try_again=False;
    h.add_edges([(i,j) for j in set(ngh1).union(set(ngh2)).difference(set([e[0],e[1]]))]);
    return h;

def Lollipop(k,l):
    g=graphs.CompleteGraph(k);
    for i in range(l):
        g.add_vertex(k+i);
        g.add_edge(k+i,k+i-1);
    return g;

def ttt(n):
    l=[2]*n;
    l[0]=3;
    l[n-1]=3;
    return l;

def caterpillar(n,l):
    g=graphs.PathGraph(n);
    for i in range(n):
        for j in range(l[i]):
            g.add_vertex((i,j));
            g.add_edge(i,(i,j));
    return g;
    
#######
#Testing Graphs
#######

def is_CompleteGraph(g):
    if min(g.degree_sequence())==g.order()-1:
        return True;
    return False;

def is_CompleteBipartite(g):
    h=g.complement();
    com_sub=h.connected_components_subgraphs();
    if len(com_sub)!=2:
        return False;
    for com in com_sub:
        if min(com.degree())<com.order()-1:
            return False;
    return True;

def is_kStar(g):
    gbar=g.complement();
    V=copy(gbar.vertices());
    for v in V:
        if gbar.degree(v)==0:
            gbar.delete_vertex(v);
    return is_CompleteGraph(gbar);

def delta(g):
    return min(g.degree_sequence());
    
def Delta(g):
    return max(g.degree_sequence());
    
#######
#Not in good condition
#######

def eta(g): 
    """
    return the Hadwiger number of g.
    """
    n=g.order();
    w=g.clique_number();
    eta=w;
    for i in range(w+1,n):
        if has_minor(g,graphs.CompleteGraph(i)):
            eta=i;
        else:
            break;
    return eta;
    
def cover_matrix(m_cover,m,m_vec=None,n_cover=None,n=None,n_vec=None):
    """
    return a mxn matrix with m_vec*n_vec^T embedded in the m_cover*n_cover positions.
    m_vec is the all one list by default.
    n-related variables are by default symmetric to m-related variables.
    """
    if n_cover==None:
        n_cover=m_cover;
    if n==None:
        n=m;
    if m_vec==None:
        m_vec=[1]*len(m_cover)        
    if n_vec==None:
        n_vec=m_vec;
    if len(n_cover)!=len(n_vec):
        print "Need to specify n_vec."
    A=matrix(m,[0]*(m*n));
    for i in range(len(m_cover)):
        for j in range(len(n_cover)):
            A[m_cover[i],n_cover[j]]=m_vec[i]*n_vec[j];
    return A;
    
def calG(A,type="simple",loop=False):
    """
    return the corresponding graph. 
    type can be "simple", "digraph", or "bipartite". 
    loops will be ignored by default, unless loop is set to be True.
    """
    m,n=A.dimensions();
    if m!=n:
        print "input matrix is not square";
        return 0;
    new_A=copy(A);
    for i in range(n):
        for j in range(m):
            if A[i,j]!=0:
                new_A[i,j]=1;
    if loop==False:
        for i in range(n):
            new_A[i,i]=0;
    if type=="simple":
        return Graph(new_A);
    if type=="digraph":
        return DiGraph(new_A);
    if type=="bipartite":
        return BipartiteGraph(new_A);
