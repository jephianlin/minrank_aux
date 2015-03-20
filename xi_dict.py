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
    
def has_SAP(A):
    """
    Input: a symmetric matrix A
    Output: True if A has Strong Arnold Property; False if A does not.
    """
    AA=SAPmatrix(A);
    if AA.rank()==AA.dimensions()[1]:
        return True;
    else:
        return False;
        
def eigens(A):
    """
    Input: a matrix A
    Output: a dictionary with eigenvalue: algebraic multiplicity.
    """
    all_values=A.eigenvalues()
    eigens={};
    while all_values!=[]:
        lam=all_values.pop();
        if lam in eigens.keys():
            eigens[lam]+=1;
        else:
            eigens[lam]=1;
    return eigens
    
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
