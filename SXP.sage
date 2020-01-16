print("This code contains extra copy of Z_game, Zell_game, Zplus_game, for the completeness of Zsap_game program.")

###extra copy of Z_game, Zell_game, Zplus_game.
def Z_game(g,B,ban=[]):
    """
    Input:
        g: a simple graph
        B: a set of initial blue vertices
        ban: a set of banned vertices
    Output:
        return the derived set under the regular CCR-Z.
        Note: vertices in ban cannot make a force, but are still white neighbors if white.
    """    
    V=g.vertices();
    white_neighbors={}; #a dictionary with the structure {v: list of white neighbors}
    white_numbers={}; #a dictionary with the structure {v: number of white neighbors}
    for v in V:
        nbh=g.neighbors(v);
        for b in B:
            try:
                nbh.remove(b);
            except ValueError:
                pass;
        white_neighbors[v]=nbh;
        white_numbers[v]=len(nbh);
    queue=copy(B); #queue stores list of vertices that can possibly make a force
    derived_set=copy(B); #derived_set stores the set of blue vertices
    whole_loop=True;
    while whole_loop: #keep searching if queue!=[]
        try:
            v=queue[0];
            queue.remove(v);
            if v not in ban and white_numbers[v]==1:
                u=white_neighbors[v][0]; #the only white neighbor
                derived_set.append(u); #make the force
                #update white_numbers, white_neighbors, and queue
                if white_numbers[u]==1: 
                    queue.append(u);
                u_nbr=g.neighbors(u);
                for w in u_nbr:
                    white_neighbors[w].remove(u);
                    white_numbers[w]+=-1;
                    if w in derived_set and white_numbers[w]==1:
                        queue.append(w);
        except IndexError:
            whole_loop=False;
    return derived_set;
    
def Zell_game(g,B,ban=[]): ##every non-isolated vertex can force itself if no other white neighbors.
    """
    Input:
        g: a simple graph
        B: a set of initial blue vertices
        ban: a set of banned vertices
    Output:
        return the derived set under the CCR-Zell.  
        That is, in addition to CCR-Z, every non-isolated vertex can force itself if 
        no other white neighbors.
        Note: vertices in ban cannot make a force, but are still white neighbors if white.
    """    
    #Build h from g by deleting all isolated vertices,
    # since they are not going to change the outcome. 
    h=g.copy();
    for v in g.vertices():
        if h.degree(v)==0:
            h.delete_vertex(v);
    V=h.vertices();
    white_neighbors={}; #a dictionary with the structure {v: list of white closed neighbors}
    white_numbers={}; #a dictionary with the structure {v: number of white closed neighbors}
    for v in V:
        nbh=h.neighbors(v);
        nbh.append(v);
        for b in B:
            try:
                nbh.remove(b);
            except ValueError:
                pass;
        white_neighbors[v]=nbh;
        white_numbers[v]=len(nbh);
    queue=copy(V); #queue stores list of vertices that can possibly make a force
    derived_set=copy(B); #derived_set stores the set of blue vertices
    whole_loop=True;
    while whole_loop: #keep searching if queue!=[]
        try:
            v=queue[0];
            queue.remove(v);
            if v not in ban and white_numbers[v]==1:
                u=white_neighbors[v][0]; #the only white neighbor
                derived_set.append(u); #make the force
                #update white_numbers, white_neighbors, and queue
                u_nbr=h.neighbors(u);
                u_nbr.append(u);
                for w in u_nbr:
                    white_neighbors[w].remove(u);
                    white_numbers[w]+=-1;
                    if white_numbers[w]==1:
                        queue.append(w);
        except IndexError:
            whole_loop=False;
    return derived_set;

def Zplus_game(g,B):
    """
    Input:
        g: a simple graph
        B: a set of initial blue vertices
    Output:
        return the derived set under the CCR-Zplus.  
        That is, apply CCR-Z to each white branch.
        Note: the banned set is not implemented, since Zvcoc has no Zplus version.
    """   
    white_graph=g.copy(); #recording the induced subgraph on white
    derived_set=copy(B); #derived_set stores the set of blue vertices
    for b in derived_set:
        white_graph.delete_vertex(b);
    whole_loop=True;
    while whole_loop: 
        whole_loop=False; #open again only when something found.
        whole_extra_B=[]; #extra blue vertices found in this round
        partition=white_graph.connected_components();
        for com in partition:
            considered_set=copy(com);
            for v in derived_set:
                considered_set.append(v);
            considered_graph=g.subgraph(considered_set); #this is a white branch
            extra_B=Z_game(considered_graph,derived_set); #apply Z_game to this white branch
            for v in derived_set:
                extra_B.remove(v);
            for v in extra_B:
                whole_loop=True; #something found, open whole_loop
                whole_extra_B.append(v);
        #update new derived_set and new white_graph.
        for v in whole_extra_B:
            derived_set.append(v);
            white_graph.delete_vertex(v);
    return derived_set;

def Zsap_game(g,B,rule="CCRZ",oc_rule=True,banned_dict={}): 
    """
    Input:
        g: a simple graph
        B: a set of initial blue non-edges
        rule: rule that appplies - "CCRZ", "CCRZell", or "CCRZplus"
        oc_rule: if the odd cycle rule applies - True or False
        banned_dict: a dictionary with structure {v: banned vertices in the local game l(g,v,rule)}
            **Usually called by find_Zsap when get_value="vertex".
    Output:
        return the derived set of the SAP zero forcing game through the CCRZsap^rule.  
    """   
    active={}; 
    #for each vertex i, assign a value of 1,0. 
    #1 means l(g,i) can possibly make a force, while 0 means that is impossible.
    V=g.vertices();
    for v in V:
        active[v]=1;
    #complete banned_dict by empty sets
    for v in V:  
        if v not in banned_dict.keys(): 
            banned_dict[v]=[];
    queue=[v for v in V] #vertices i such that its local game is still active
    derived_set=copy(B); #derived_set stores the set of blue non-edges
    #######
    #the whole_loop contains two sub-loops: regular_loop and oc_loop
    # regular_loop go make all possible forces without the odd cycle rule
    # oc_rule make all possible forces with only the odd cycle rule
    #whole_loop stops when nothing is found in both sub-loops
    #if oc_rule=False, then whole_loop will run only once.
    #######
    whole_loop=True;        
    while whole_loop: 
        whole_loop=False; #open again only when something found, either in regular_loop or oc_loop.
        regular_loop=True; 
        while regular_loop: 
            try:
                u=queue[0]; #starting from the second whloe loop, queue is given by oc loop.
                queue.remove(u);
                if active[u]==1:
                    #consider the local game l(g,u,rule)
                    #local_B contains all the neighbors of u, u itself, and all blue non-neighbor of u
                    #make all possible forces in this local game
                    local_B=g.neighbors(u);
                    local_B.append(u);
                    for v in V:
                        if (u,v) in derived_set or (v,u) in derived_set:
                            local_B.append(v);
                    if rule=="CCRZ":
                        extra_B=list(Z_game(g,local_B,banned_dict[u]));
                    if rule=="CCRZell":
                        extra_B=list(Zell_game(g,local_B,banned_dict[u]));
                    if rule=="CCRZplus":
                        extra_B=list(Zplus_game(g,local_B));
                    for v in local_B:
                        extra_B.remove(v);
                    for v in extra_B:
                        derived_set.append((u,v));
                        active[v]=1;
                        queue.append(v);
                        whole_loop=True; #something found, open whole_loop
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
                        whole_loop=True; #something found, open whole_loop
                        for e in C.edges(labels=False):
                            derived_set.append(e);
                            white_graph.delete_edge(e);
                        for v in C.vertices():
                            queue.append(v);
                            active[v]=1;    
        else:
            whole_loop=False;
    return derived_set;

def find_Zsap(g,rule="CCRZ",oc_rule=True,get_value=False):
    """
    Input:
        g: a simple graph
        rule: rule that appplies - "CCRZ", "CCRZell", or "CCRZplus"
        oc_rule: if the odd cycle rule applies - True or False
        get_value: False, "edge", or "vertex".  
    Output:
        Return Zsap according the choice of get_value.
        Here oc_rule can be equipped or not, and the rule also varies.
        If get_value=False, then return True or False depending on Zsap=0 or not. (polynomial-time).
        If get_value="edge", then return Zsap.
        If get_value="vertex", then return Zoc.
        ** rule="CCRZplus" and get_value="vertex" is not compatable, since Zvc-oc^plus is not defined.
    """  
    mbar=g.complement().size(); #number of non-edges
    if get_value==False: #only check if [] a Zsap zero forcing set
        derived_set=Zsap_game(g,[],rule,oc_rule);
        if mbar==len(derived_set):
            return True;
        else:
            return False;
    if get_value=="edge": #number of non-edges grows up rapidly
        Ebar=g.complement().edges(labels=False);
        mbar=len(Ebar);
        lbd=-1;
        ubd=mbar;
        while ubd-lbd>=2: #apply random algorithm;
            guess=random.choice(range(lbd+1,ubd)); #take an interior point in [lbd,ubd];
            found=False;
            for B in Combinations(Ebar,guess):
                if mbar==len(Zsap_game(g,B,rule,oc_rule)):
                    found=True;
                    break;
            if found:
                ubd=guess;
            else:
                lbd=guess;
        return ubd;
    if get_value=="vertex":
        gbar=g.complement();
        Ebar=gbar.edges(labels=False);
        V=g.vertices();
        mbar=len(Ebar);
        n=g.order();
        lbd=-1;
        ubd=n;
        while ubd-lbd>=2: #apply random algorithm;
            guess=random.choice(range(lbd+1,ubd)); #take an interior point in [lbd,ubd];
            found=False;
            for sub in Combinations(V,guess):
                #build initial blue nonedges B;
                B=[];
                for ebar in Ebar:
                    i,j=ebar;
                    if i in sub or j in sub:
                        B.append(ebar);
                #build banned_dict;
                banned_dict={v:[] for v in V};
                for j in sub: ##(i:j -> k) is banned if j is in sub and {i,j} is nonedge.
                    for i in gbar.neighbors(j):
                        banned_dict[i].append(j);
                if mbar==len(Zsap_game(g,B,rule,oc_rule,banned_dict)):
                       found=True;
                       break;
            if found:
                ubd=guess;
            else:
                lbd=guess;
        return ubd;     

def Zsap_test(g,rule="buy_vertex"): #This is an old code, without Zsap^+, but with nonsingular_E, one_coin_edge, buy_edge.
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

def SSPmatrix(A, return_index=False):
    """
    Input: 
        A: a symmetric matrix;
        return_index: if True, also return two dictionaries
                    row_index={pair: row index}
                    column_index={nonedge: col index}
    Output: 
        the linear system given by SSP conditions;
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
    if return_index:
        keys=column_index.keys();
        for a,b in keys:
            if a>b:
                c=column_index.pop((a,b));
        return SSP_sys,row_index,column_index;
    else:
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
    
def nonedge_index(g,reverse=False):
    """
    Input:
        g: a graph
    Output:
        a dictionary {the k-th non-edge: k}; the order of non-edges is i,j<k,l if i<k or i=k with j<l. 
    """
    n=g.order()
    column_index={}; #|E(Gbar)| variables
    var_counter=0;
    for i in range(0,n):
        for j in range(i+1,n):
            if g.has_edge(i,j)==False:
                column_index[i,j]=var_counter;
                column_index[j,i]=var_counter; 
                var_counter+=1;
    if reverse==False:
        return column_index;
    if reverse==False:
        new_index={};
        for key in column_index.keys():
            new_index[column_index[key]]=key;
        return new_index;

def find_Zssp(g,F_col=[],k=0,rule="nonsingular"):
    """
    Input:
        g: a simple graph
        rule: can be "nonsingular" or "ZFS" or "Zsspk" so far
        F_col: only compatable with rule=="ZFS", a set of non-edges
        k: only compatable with rule=="Zsspk", an integer
    Output:
        When "nonsingular", return True iff Zssp=0.
        When "ZFS", return True iff F_col is a ZFS. 
        When "Zsspk", return the list of k-subset of nonedges that is a ZFS.
        (so find_Zssp(g,rule="nonsingular")=find_Zssp(g,f_col=[],rule="ZFS"),)
        (while find_Zssp(g,k=0,rule="Zsspk")=[[]])
    """
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
    if rule=="nonsingular":
        return h.order()==len(gzerosgame(h,F,B));
    if rule=="ZFS":
        col_index=nonedge_index(g);
        try_F=copy(F);
        for e in F_col:
            try_F.append(-col_index[e]-1);
        return h.order()==len(gzerosgame(h,try_F,B));
    if rule=="Zsspk":
        col_index=nonedge_index(g);
        Ebar=g.complement().edges(labels=False);
        one_nonedge=[];
        for com in Combinations(Ebar,k):
            try_F=copy(F);
            for e in com:
                try_F.append(-col_index[e]-1);
            if h.order()==len(gzerosgame(h,try_F,B)):
                one_nonedge.append(com);
        return one_nonedge;

def ZplusFloor_game(g,done,act,token):
    """
    Input:
        g: a simple graph
        done: list of blue vertices that made their force (they shouldn't have white neighbors)
        act: list of blue vertices that make no force yet
        token: number of "free" blue vertices that can make a hop
    Output:
        if "act" together with "token" number of free blue vertices is a zero forcing set,
         then return True. Otherwise, return False.
        **ZplusFloor_game(g,[],[],k) is returning if ZFloor(g)<=k or not.
    """
    #recursive algorithm is implemented, so each graph and each list should be copied
    h=g.copy() 
    this_done=[];
    this_act=[];
    for v in done:
        h.delete_vertex(v);
        this_done.append(v);
    for v in act:
        this_act.append(v);        
    #delete every edges between this_act.
    for u,w in Combinations(this_act,2):
        h.delete_edge(u,w);
    #Do one round of propagation according to CCR-Z
    #The CCR-Zplus is implement at the recursive step
    again=True;
    while again:
        again=False;
        for v in this_act:
            if h.degree(v)==1: #this vertex can make CCR-Z. After that it is done, and cannot make a hope.
                u=h.neighbors(v)[0];
                this_act.append(u);
                this_act.remove(v);
                this_done.append(v);
                h.delete_vertex(v);
                for w in this_act:
                    h.delete_edge(u,w);
                again=True;
                break;                    
            if h.degree(v)==0: #this vertex can make a hop. token+1, delete it from h, and add it to done.
                token+=1;
                this_act.remove(v);
                this_done.append(v);
                h.delete_vertex(v);
                again=True;
    #When the while loop is done, all token are collected, and all vertices in act cannot make a force.
    if h.order()==0:
        return True;
    if h.order()!=0 and token==0:
        return False;
    #Find white set. And do recursion.
    white_graph=h.copy();
    for v in this_act:
        white_graph.delete_vertex(v);
    white=white_graph.vertices();
    if token>=white_graph.order():
        return True;
    else:
        components=white_graph.connected_components();
        k=len(components);
        new_graphs=[];
        for i in range(k):
            new_graphs.append(h.subgraph(components[i]+this_act));
        for new_act in Combinations(white,token): #try all possible way to put the tokens
            good_choice=True;
            for i in range(k):
                if good_choice:
                    if ZplusFloor_game(new_graphs[i],[],this_act+list_intersection(components[i],new_act),0)==False:
                        good_choice=False;
            if good_choice==True:
                return True;
        return False;
        
def find_ZplusFloor(g):
    """
    Input:
        g: a simple graph
    Output:
        return the value of ZplusFloor(g).
    """
    ZplusF=g.order()-1;
    if ZplusF<0: #define ZFloor(null graph)=0
        return ZplusF+1;
    try_lower=True;
    while try_lower:
        try_lower=False;
        if ZplusFloor_game(g,[],[],ZplusF)==True:
            try_lower=True;
            ZplusF+=-1;     
    return ZplusF+1;

def SMPmatrix(A):
    """
    Input: a symmetric matrix A
    Output: the linear system given by SMP conditions
    """
    n=A.dimensions()[0];
    R=A.base_ring();
    row_index={}; #{n+1 choose 2}+(n-2) restrictions
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
    for q in range(2,n):
        row_index[q]=res_counter;
        res_counter+=1;
    SMP_sys=matrix(R,res_counter,var_counter);
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(n):
                if k!=j and A[k,j]==0:
                    SMP_sys[row_index[i,j],column_index[k,j]]+=A[i,k];
                if i!=k and A[i,k]==0:
                    SMP_sys[row_index[i,j],column_index[i,k]]-=A[k,j];
    Aq=A^2;
    for q in range(2,n):
        for i in range(0,n):
            for j in range(i+1,n):
                if A[i,j]==0:
                    SMP_sys[row_index[q],column_index[i,j]]+=Aq[i,j];
        Aq=Aq*A;
    return SMP_sys;
    
def has_SMP(A):
    """
    Input: a symmetric matrix A (described by some graph G)
    Output: return if A has SMP or not. 
    SMP means if for symmetric matrix B with 
        AB-BA=0, 
        (A^qB).trace()=0 for any q,
        A.Hadamard_product(B)=0, and 
        I.Hadamard_product(B)=0, 
    then B=0.
    
    Example:
        g=graphs.PathGraph(5);
        A=g.adjacency_matrix();
        has_SMP(A);
        ->True
    """
    SMP_sys=SMPmatrix(A);
    return rank(SMP_sys)==SMP_sys.dimensions()[1];
