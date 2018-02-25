print "---sshow, multi_sshow, tuple_generator, minimal_graphs, empty_array, all_one_matrix, elementary_matrix, eigens_multi, sort_dictionary, has_minor, etc."

import random; #If this line is not included, random.choice should be changed to choice.

def sshow(g,stg=None):
    if stg==None:
        stg=g.graph6_string();
    g.show(figsize=[2,2],vertex_labels=False,vertex_size=50,title="%s: %s"%(g.order(),stg));

def multi_sshow(all_graphs,each_row=0,text=None,final_figsize=None):
    """
    Input:
        all_graphs: a list of graph strings
        each_row: how many graphs displayed on each row, default is 0 (all)
        text: a string shown on the output picture, default is to show the strings of all_graphs
        final_figsize: the figsize of the output picture, default is [12,2]
    Output:
        a picture of all graphs in all_graphs in a row, plus text as the title.
    """
    if each_row==0:
        pic=Graph(0).plot();
        shift=0;
        gap=1;
        for stg in all_graphs:
            g=Graph(stg);
            draft=g.plot(save_pos=True);
            xy_range=draft.get_axes_range();
            local_shift=-xy_range["xmin"];
            x_range=xy_range["xmax"]-xy_range["xmin"];
            gpos=g.get_pos();
            for v in g.vertices():
                gpos[v][0]+=shift+local_shift;
            gpic=g.plot(figsize=[2,2],vertex_labels=False,vertex_size=50,pos=gpos);
            pic+=gpic;
            shift+=x_range+gap;
            pic+=line([(shift-0.5*gap,-0.5),(shift-0.5*gap,0.5)],linestyle="--");
        pic.axes(False);
        if text==None:
            text="";
            for stg in all_graphs:
                text+="%s "%stg;
        if final_figsize==None:
            final_figsize=[12,2];
        pic.show(figsize=final_figsize, title=text);
        
    if each_row>0:
        cache=[];
        period=0;
        for stg in all_graphs:
            cache.append(stg);
            period+=1;
            if period==each_row:
                multi_sshow(cache);
                cache=[];
                period=0;
        if cache!=[]:
            multi_sshow(cache);

def tuple_generator(k,n):
    """
    Input:
        k: a positive integer at least ;
        n: a positive integer;
    Output:
        a generator generating [0,...,0], [1,0,...,0], to ,[k-1,...,k-1];
    """
    a=[0]*n;
    yield a;
    counter=1;
    max_counter=k^n;
    while counter<max_counter:
        a[0]+=1;
        for i in range(n):
            if a[i]>=k:
                a[i]-=k;
                a[i+1]+=1;
        yield a;
        counter+=1;

def minimal_graphs(want_n,current_list):
    """
    Input:
        want_n: a list of graph strings;
        current_list: a list of graph strings;
        This function assums g in current_list never has an 
          induced subgraph from want_n;
    Output:
        extra minimal graphs;
        The function finds all the g in want_n that containts 
          no induced subgraph from want_n or current_lsit;
    """
    all_g=copy(want_n);
    all_g.sort(key=lambda k:Graph(k).size());
    min_list=copy(current_list);
    extra_list=[];
    for stg in all_g:
        g=Graph(stg);
        for stg_h in min_list:
            h=Graph(stg_h);
            if g.subgraph_search(h,True)!=None:
                break;
        else:
            min_list.append(stg);
            extra_list.append(stg);
    return extra_list;

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
    return all element in B that appears in A, which is usually the intersection of them.
    """
    inter=[]
    for b in B:
        if b in A:
            inter.append(b);
    return inter;

def list_union(A,B):
    """
    A,B are lists; 
    return A along with all element in B that does not appear in A, which is usually the union of them.
    """
    uni=copy(A);
    for b in B:
        if b not in A:
            uni.append(b);
    return uni;

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

def row_per_matrix(l):
    n=len(l);
    A=matrix(n,[0]*(n^2));
    for i in range(n):
        A[i,l[i]]=1;
    return A;
    
def col_per_matrix(l):
    n=len(l);
    A=matrix(n,[0]*(n^2));
    for i in range(n):
        A[l[i],i]=1;
    return A;

def per_similar(A,l):
    return row_per_matrix(l)*A*col_per_matrix(l);

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
    for i in range(n):
        if egv[i]<0:
            m+=1;
        if egv[i]>0:
            p+=1;
    return [p,m,n-p-m];

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

#######
# Normalized Laplacian & signless Laplacian
#######

def normalize_similar(A):
    n=A.dimensions()[0];
    I=identity_matrix(n);
    dd=[sum(A[i,:][0])for i in range(n)];
    ddinv=[0]*n;
    for i in range(n):
        if dd[i]!=0:
            ddinv[i]=1/dd[i];
        else:
            I[i,i]=0;
    #D=diagonal_matrix(dd);
    Dinv=diagonal_matrix(ddinv);
    return I-Dinv*A;
    
def normalized_Laplacian_similar(g):
    n=g.order();
    A=g.adjacency_matrix();
    return normalize_similar(A);

def nl_spectrum(g):
    return eigens_multi(normalized_Laplacian_similar(g));

def signless_Laplacian(g):
    L=g.laplacian_matrix();
    Q=-L;
    for i in range(g.order()):
        Q[i,i]=L[i,i];
    return Q;
