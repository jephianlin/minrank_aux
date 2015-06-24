def SAPmatrix(A):
    """
    Input: a symmetric matrix A
    Output: The matrix for checking if A has SAP
    """
    if A.is_symmetric()==False:
        raise ValueError, "Input matrix is not symmetric."
    AA=[];
    n=A.dimensions()[0];
    row_num=0;
    for i in range(n):
        for j in range(n):
            AA.append([0]*(n*n));
            if A[i][j]!=0 or i==j:
                AA[row_num][i*n+j]=1;
            if A[i][j]==0 and i!=j:
                AA[row_num][i*n+j]=1;
                AA[row_num][j*n+i]=-1;
            row_num+=1;        
    BB=identity_matrix(n).tensor_product(A);
    for row in BB.rows():
        AA.append(row);
    return matrix(AA);
    
def SAPreduced_matrix(A):
    """
    Input: a symmetric matrix A
    Output: the reduced matrix for checking if A has SAP
    """
    if A.is_symmetric()==False:
        raise ValueError, "Input matrix is not symmetric."
    AA=[];
    n=A.dimensions()[0];
    nonedge=0;
    for i in range(n):
        for j in range(i+1,n):
            if A[i][j]==0:
                AA.append([0]*(n*n));
                i_start=i*n;
                j_start=j*n;
                for k in range(n):
                    AA[nonedge][i_start+k]=A[j][k];
                    AA[nonedge][j_start+k]=A[i][k];
                nonedge+=1;                    
    return matrix(AA).transpose();

def has_SAP(A):
    """
    Input: a symmetric matrix A
    Output: True if A has Strong Arnold Property; False if A does not.
    """
    ##SAPreduced_matrix is faster than SAPmatrix
    ##AA=SAPmatrix(A);
    ##if AA.rank()==AA.dimensions()[1]:
    AA=SAPreduced_matrix(A);
    if AA.rank()==AA.dimensions()[1]:
        return True;
    else:
        return False;
        
def ful_annihilator(A):
    """
    Input: a symmetric matrix A
    Output: 0 if A has SAP; otherwise return the basis of ful_annihilators of A;
    """
    n=A.dimensions()[0];
    AA=SAPmatrix(A);
    ker=AA.right_kernel();
    if ker.dimension()==0:
        return 0;
    else:
        basis=[];
        for v in ker.basis():
            list_v=list(v);
            basis.append(matrix(n,n,list_v));
        return basis;
    
def ZFloor_game(g,done,act,token,chron=False):
    """
    g: considered graph
    done: list of blue vertices that can no longer move (token are taken)
    act: list of active blue vertices
    token: integer of available tokens
    
    Output True if it is a Zfloor forcing set; False if not. To see chron list, set chron=True.
    """
    ##for graphs and lists, we need to make a copy.
    h=g.copy() 
    this_done=[];
    this_act=[];
    for v in done:
        h.delete_vertex(v);
        this_done.append(v);
    for v in act:
        this_act.append(v);        
    ##Do conventional CRC as possible, and collect tokens.
    ##delete every edges between this_act.
    for u,w in Combinations(this_act,2):
        h.delete_edge(u,w);
    again=True;
    while again:
        again=False;
        for v in this_act:
            if h.degree(v)==1:
                u=h.neighbors(v)[0];
                this_act.append(u);
                this_act.remove(v);
                this_done.append(v);
                h.delete_vertex(v);
                for w in this_act:
                    h.delete_edge(u,w);
                again=True;
                break;                    
            if h.degree(v)==0:
                token+=1;
                this_act.remove(v);
                this_done.append(v);
                h.delete_vertex(v);
                again=True;
    if h.order()==0:
        return True;
    if h.order()!=0 and token==0:
        return False;
    ##Find white set
    white=h.vertices();
    for v in this_act:
        white.remove(v);
    ##Do recursion.
    if token>=len(white):
        return True;
    else:
        for new_act in Combinations(white,token):
            if ZFloor_game(g,this_done,this_act+new_act,0)==True:
                return True;
        return False;
        
def find_ZFloor(g):
    """
    Input: a simple graph g
    Output: the ZFloor of g
    """
    ZF=g.order()-1;
    if ZF<0:
        return ZF+1;
    try_lower=True;
    while try_lower:
        try_lower=False;
        if ZFloor_game(g,[],[],ZF)==True:
            try_lower=True;
            ZF+=-1;     
    return ZF+1;
    
def xi_ubd(g):
    C=g.connected_components_subgraphs();
    if len(C)==1:
        ubd=find_ZFloor(g);
        e=g.size();
        if g.is_bipartite():
            #print "bipartite"
            ubd=min(ubd,int(-0.5+sqrt(2.25+2*e)));
        else:
            #print "not bipartite"
            ubd=min(ubd,int(-0.5+sqrt(0.25+2*e)));
        if g.is_tree():
            #print "tree"
            ubd=min(ubd,2);
        return ubd;            
    else:
        ubd=0;
        for com in C:
            ubd=max(ubd,xi_ubd(com));
        return ubd;
        
##This function requires gzerosgame and find_gzfs functions in oc_diag_analysis.sage
def SAPreduced_mr(g,non_singular=False):
    n=g.order();
    A=g.adjacency_matrix()-identity_matrix(n);
    AA=SAPreduced_matrix(A);
    ##rows should be n^2; cols should be number of nonedges
    rows,cols=AA.dimensions();
    ##Set X as -1~-rows and Y as 1~cols
    X=[];
    for i in range(1,rows+1):
        X.append(-i);
    Y=[];
    for i in range(1,cols+1):
        Y.append(i);
    ##NOTE: the labeling of graphs start at 1 and -1, but not 0
    ##      but the labeling of the matrix start at 0 for both rows and columns
    SAP_g=Graph(0);
    SAP_g.add_vertices(X);
    SAP_g.add_vertices(Y);
    ##setting edges and banned set
    B=[];
    for i in range(rows):
        for j in range(cols):
            if AA[i][j]!=0:
                SAP_g.add_edge(-i-1,j+1);
            if AA[i][j]==-1:
                B.append((-i-1,j+1));
    ##For debug
    #show(AA);
    #show(SAP_g);
    #print B;
    if non_singular==False:
        return rows+cols-find_gZ(SAP_g, X, B);
    if non_singular==True:
        #print gzerosgame(SAP_g, X, B);
        return len(gzerosgame(SAP_g, X, B))==rows+cols;

def Zsap(g,rule="buy_vertex"):
    """
    Input:
        g simple graph;
        rule "nonsingular" only test if Zsap(g,rule="one_coin_edge")==0 or not;
             "one_coin_edge" means doing regular zero forcing on the aux graph;
             "buy_vertex" means using 1 coin to buy all edges incident to a certain vertex;
             "buy_edge" means using 2 coins to buy all edges incident to a certain edge;
    Output:
        the zero forcing number;
    """
    ##Temporarily only one of the three rules can be true at the same time;
    #build the auxiliary graph h;
    gbar=g.complement();
    h=Graph(0);
    n=g.order();
    all_pairs=[];
    for i in range(n):
        for j in range(n):
            all_pairs.append("%s;%s"%(i,j));
    nonedges=g.complement().edges(labels=False);
    h.add_vertices(all_pairs);
    h.add_vertices(nonedges);
    #build the edges and banned set;
    B=[];
    for nonyee in nonedges:
        i,j=nonyee;
        B.append(("%s;%s"%(i,j),nonyee));
        B.append(("%s;%s"%(j,i),nonyee));
        h.add_edge("%s;%s"%(i,j),nonyee);
        h.add_edge("%s;%s"%(j,i),nonyee);
        for k in g.neighbors(i):
            h.add_edge("%s;%s"%(j,k),nonyee);
        for k in g.neighbors(j):
            h.add_edge("%s;%s"%(i,k),nonyee);    
    nh=h.order();
    #show(h,figsize=[10,10],vertex_size=50);
    if rule=="nonsingular":
        return len(gzerosgame(h,all_pairs,B))==nh;            
    if rule=="one_coin_edge":
        return find_gZ(h,all_pairs,B)-n^2;
    if rule=="buy_vertex":
        for z in range(n+1):
            ##going from zero to n
            for blue in Combinations(g.vertices(),z):
                F=copy(all_pairs);
                newB=copy(B);
                for v in blue:
                    for nonyee in nonedges: ##build new zero forcing set F
                        if nonyee[0]==v or nonyee[1]==v:
                            if nonyee not in F:
                                F.append(nonyee);
                    for u in gbar.neighbors(v): 
                        ##all edges incident to the forbidden pair
                        ## should be banned
                        forbidden_pair="%s;%s"%(u,v);
                        for nonyee in h.neighbors(forbidden_pair):
                            #print v,u,forbidden_pair,nonyee;
                            if (forbidden_pair,nonyee) not in newB:
                                newB.append((forbidden_pair,nonyee));
                ##For debug
                #print z,blue;
                #print F;
                #print newB;
                if len(gzerosgame(h,F,newB))==nh:
                    #return z;
                    return z,blue;
    if rule=="buy_vertex_no_ban":
        for z in range(n+1):
            ##going from zero to n
            for blue in Combinations(g.vertices(),z):
                F=copy(all_pairs);
                newB=copy(B);
                for v in blue:
                    for nonyee in nonedges: ##build new zero forcing set F
                        if nonyee[0]==v or nonyee[1]==v:
                            if nonyee not in F:
                                F.append(nonyee);
                    for u in gbar.neighbors(v): 
                        ##all edges incident to the forbidden pair
                        ## should be banned
                        forbidden_pair="%s;%s"%(u,v);
                        for nonyee in h.neighbors(forbidden_pair):
                            #print v,u,forbidden_pair,nonyee;
                            if (forbidden_pair,nonyee) not in newB:
                                newB.append((forbidden_pair,nonyee));
                ##For debug
                #print z,blue;
                #print F;
                #print newB;
                if len(gzerosgame(h,F,B))==nh:
                    #return z;
                    return z,blue;
