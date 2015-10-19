def Zsap_game(g,B,rule="CCRZ",oc_rule="False"):
    active={}; 
    #for each vertex i, assign a value of 1,0. 
    #1 means l(g,i) can possibly make a force, while 0 means that is impossible.
    V=g.vertices();
    for v in V:
        active[v]=1;
    queue=[v for v in V] #the queue for checking local games.
    derived_set=copy(B); #if not use copy, B will be changed
    whole_loop=True;        
    while whole_loop:
        whole_loop=False; #open again only when something found.
        regular_loop=True;
        while regular_loop:
            try:
                u=queue[0]; #starting from the second whloe loop, queue is given by oc loop.
                queue.remove(u);
                if active[u]==1:
                    #local_B contains all the neighbors of u, u itself, and all blue non-neighbor of u;
                    local_B=g.neighbors(u);
                    local_B.append(u);
                    for v in V:
                        if (u,v) in derived_set or (v,u) in derived_set:
                            local_B.append(v);
                    if rule=="CCRZ":
                        extra_B=list(Z_game(g,local_B));
                    if rule=="CCRZell":
                        extra_B=list(Zell_game(g,local_B));
                    if rule=="CCRZplus":
                        extra_B=list(Zplus_game(g,local_B));
                    for v in local_B:
                        extra_B.remove(v);
                    for v in extra_B:
                        derived_set.append((u,v));
                        active[v]=1;
                        queue.append(v);
                        whole_loop=True; #if regular_loop found something, open whole_loop;
                active[u]=0;
            except IndexError:
                regular_loop=False;
        if oc_rule:
            oc_loop=True;
            white_graph=g.complement().copy();
            for e in derived_set:
                white_graph.delete_edge(e);
            for v in V:
                GNv=white_graph.subgraph(g.neighbors(v)); #The induced subgraph on N(v) of white_graph
                for C in GNv.connected_components_subgraphs():
                    deg=C.degree_sequence();
                    if min(deg)==2 and max(deg)==2 and C.order()%2==1: #That is, if C is an odd cycle
                        whole_loop=True;
                        for e in C.edges(labels=False):
                            derived_set.append(e);
                            white_graph.delete_edge(e);
                        for v in C.vertices():
                            queue.append(v);
                            active[v]=1;    
        else:
            whole_loop=False; #if oc_rule doesn't apply, then just run one whole loop.
    return derived_set;

def find_Zsap(g,rule="CCRZ",oc_rule=False,get_value=False):
    mbar=g.complement().size();
    if get_value==False:
        derived_set=Zsap_game(g,[],rule,oc_rule);
        if mbar==len(derived_set):
            return True;
        else:
            return False;
    if get_value==True:
        print "Not yet programmed";

def Zsap(g,rule="buy_vertex"):
    """
    Input:
        g simple graph; ##should be relabeled by 0,1, ..., n-1
        rule "nonsingular" only test if Zsap(g,rule="one_coin_edge")==0 or not;
             "nonsingular_ell" is checking if Zsap^\ell=0 or not;
             "nonsingular_E" is checking if Zhat_sap=0 or not;
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
    if rule=="nonsingular_ell":
        return len(gzerosgame(h,all_pairs,[]))==nh;   
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
    if rule=="nonsingular_E":
        B_sort={};
        for i in range(n):
            B_sort[i]=[];
        for nonyee in nonedges:
            i,j=nonyee;
            B_sort[i].append(("%s;%s"%(j,i),nonyee));
            B_sort[j].append(("%s;%s"%(i,j),nonyee));
        for coms in Combinations(range(n)): #make coms zero <-> delete edges of coms from h
            Eh=h.copy();
            for i in coms:
                Eh.delete_edges(B_sort[i]);
            #if coms==[1,2]:
            #    Eh.show(vertex_size=50,figsize=[8,8])
            #    print all_pairs;
            if len(gzerosgame(Eh,all_pairs,[]))!=nh:
                #print coms;
                return False;
        return True;
                    
def SSPmatrix(A):
    """
    Input: a symmetric matrix A
    Output: the linear system given by SSP conditions
    """
    n=A.dimensions()[0];
    R=A.base_ring();
    row_index={}; #{n+1 choose 2} restrictions
    column_index={}; #|E(Gbar)| variables
    res_counter=0;
    var_counter=0;
    for i in range(0,n):
        for j in range(i+1,n):
            row_index[i,j]=res_counter;
            res_counter+=1
            if A[i,j]==0:
                column_index[i,j]=var_counter;
                column_index[j,i]=var_counter; 
                var_counter+=1;
    SSP_sys=matrix(R,res_counter,var_counter);
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(n):
                if k!=j and A[k,j]==0:
                    SSP_sys[row_index[i,j],column_index[k,j]]+=A[i,k];
                if i!=k and A[i,k]==0:
                    SSP_sys[row_index[i,j],column_index[i,k]]-=A[k,j];
    return SSP_sys;
    
def has_SSP(A):
    """
    Input: a symmetric matrix A (described by some graph G)
    Output: return if A has SSP or not. 
    SSP means if for symmetric matrix B with 
        AB-BA=0, 
        A.Hadamard_product(B)=0, and 
        I.Hadamard_product(B)=0, 
    then B=0.
    
    Example:
        g=graphs.PathGraph(5);
        A=g.adjacency_matrix();
        has_SSP(A);
        ->True
    """
    SSP_sys=SSPmatrix(A);
    return rank(SSP_sys)==SSP_sys.dimensions()[1];
    
def Zssp(g,rule="nonsingular"):
    n=g.order();
    A=g.adjacency_matrix()-diagonal_matrix([2*i for i in range(1,n+1)]);
    C=SSPmatrix(A);
    row_num,col_num=C.dimensions();
    h=Graph(0); #build the base graph
    F=[]; #build the forcing set
    for i in range(1,row_num+1):
        h.add_vertex(i);
        F.append(i);
    for j in range(1,col_num+1):
        h.add_vertex(-j);
    B=[]; #build banned set
    for i in range(row_num):
        for j in range(col_num):
            if C[i,j]!=0:
                h.add_edge(i+1,-j-1);
                if C[i,j]%2==0:
                    B.append((i+1,-j-1));
    return h.order()==len(gzerosgame(h,F,B));
