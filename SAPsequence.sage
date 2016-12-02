def fixed_sum_list(l,k):
    """
    Input:
        l: a list
        k: a value
    Output:
        return a modified list with the same support as l
        but sum k
        If len(support)=1 and k=0, support vanishes.
        If len(support)=0 and k!=0, return False.
    """
    n=len(l);
    supp=[];
    for i in range(n):
        if l[i]!=0:
            supp.append(i);
    if len(supp)==0:
        if k==0:
            return l;
        if k==0:
            return False;
    s=sum(l);
    i_max=max(supp);
    i_min=min(supp);
    if len(supp)==1 and k==0:
        l[i_max]=0;
        verbose("The support changes.", level=1);
        return l;
    l[i_max]+=k-s;
    if l[i_max]!=0:
        return l;
    else:
        a=l[i_min];
        l[i_min]+=a;
        l[i_max]-=a;
        return l;

def zero_sum_matrix(diG):
    """
    Input:
        diG: a strongly connected graph on vertices range(n)
    Output:
        an n by n matrix with zero row/column sums and non-positive off-diagonal entries
        the function will assume every vertex has a regardless the input of diG
    """
    n=diG.order();
    A=zero_matrix(n,n);
    for e in diG.edges(labels=False):
        a,b=e;
        if a!=b and A[a,b]==0:
            p=diG.shortest_path(b,a);
            for v in p:
                A[v,v]+=1;
            k=len(p);
            p.append(b);
            for i in range(k):
                A[p[i],p[i+1]]-=1;
    return A;

def Gb_find_Si(g,S,Xhats):
    """
    Input:
        g: a bipartite graph indicates the adjacency between S and union of Xhats
        S: one part of g
        Xhats: a partition of the other part of g
    Output:
        Return Ss=[Si for i in len(Xhats)] such that
         g induced on Ss[i] to Xhats[i] is a tight bipartite graph;
        Return -1 if no such Ss;
    """
    if Xhats==[]:
        return [];
    Xhat=Xhats[len(Xhats)-1];
    k=len(Xhat);
    for Si in Combinations(S,k-1):
        for x in Xhat:
            #Build SuX a list containing Si and Xhat but not x
            SuX=copy(Si);
            for y in Xhat:
                if y!=x:
                    SuX.append(y);
            induced_g=g.subgraph(SuX);
            matching_num=len(induced_g.matching());
            if matching_num!=k-1:
                break;
        else: #Si found
            new_S=copy(S);
            for s in Si:
                new_S.remove(s);
            new_Xhats=copy(Xhats);
            new_Xhats.remove(Xhat);
            certificate=Gb_find_Si(g,new_S,new_Xhats);
            if certificate!=False:
                certificate.append(Si);
                return certificate;
    return False; #no Si found
    
 def is_null_k_partition(g,partition,tight=False,return_matrix=False,return_certificate=False):
    """
    Input:
        g: a simple graph
        partition: a partition of the form of (S,[X_1,X_2,...,X_k])
        tight: checking tight or not
        return_matrix: return a matrix or not in the case of True
        epsilon: the coefficient for finding the matrix will nullity k
    Output:
        k is set as len(partition[1]).  
        Return True or False if partition is a (tight) null-k partition of g or not.
        In the case of returning True,
        if return_matrix==True, then return a matrix of g with nullity >=k,
        (where the equality holds if tight==True)
    """
    S=partition[0];
    V=g.vertices();
    Sbar=[];
    for v in V:
        if v not in S:
            Sbar.append(v);
    all_X=partition[1];
    k=len(all_X);
    ###Check if X_i's are empty
    for X in all_X:
        if len(X)==0:
            verbose("There shouldn't be any empty set in partition[1].",level=1);
            return False;
    ###Check if partition is a partition of V
    Z=zero_matrix(len(V),len(V));
    Z[S,S]+=identity_matrix(len(S));
    for X in all_X:
        Z[X,X]+=identity_matrix(len(X));
    #print "Z",Z;
    if Z!=identity_matrix(len(V)):
        verbose("Please make sure the given partition is a partition of [n].",level=1);
        return False;
    A=g.adjacency_matrix();
    A1=copy(A);
    for X in all_X:
        A1[X,X]=zero_matrix(len(X),len(X));
    #print "A1",A1;
    ###Check if X_i's are separate
    if A1[Sbar,Sbar]!=zero_matrix(len(Sbar),len(Sbar)):
        verbose("X_i's not separate.",level=1);
        return False;
    ###Check |N(s)\cap X|!=1
    for X in all_X:
            vec=A[S,X]*all_one_matrix(len(X),1);
            for i in range(len(S)):
                if vec[i,0]==1:
                    verbose("|N(s)\cap X|!=1.",level=1);
                    return False;
    if return_matrix==False and tight==False:
        return True;
    
    gms=g.copy();
    for s in S:
        gms.delete_vertex(s);
    cpnts=gms.connected_components()
    
    if return_matrix==True:
        untight_A=zero_matrix(len(V),len(V));
        for s in S:
            for X in all_X:
                l_buffer=list(A[[s],X][0]);
                fixed_sum_list(l_buffer,0);
                untight_A[[s],X]=matrix(l_buffer);
                untight_A[X,[s]]=matrix(l_buffer).transpose();
        untight_A[S,S]=-A[S,S]
        untight_A[Sbar,Sbar]=-A[Sbar,Sbar]
        for cpnt in cpnts:
            for v in cpnt:
                untight_A[v,v]=sum(list(A[[v],cpnt][0]));

    if return_matrix==True and tight==False:
        return untight_A;

    ###Below runs only in the case tight==True
    #For each component in gms, pick a representative
    rep_to_cpnt={}; #{representative: its component in list form}
    vtx_to_rep={}; #{vertex: the representative of the component it belong to}
    for cpnt in cpnts:
        u=cpnt[0];
        rep_to_cpnt[u]=cpnt;
        for v in cpnt:
            vtx_to_rep[v]=u;
    #print rep_to_cpnt;
    #print vtx_to_rep;
    
    #Build the bipartite graph Gb with all edges {s,rep}
    # if s in S has at least one edge going to the component of rep
    Gb=Graph(0);
    reps=rep_to_cpnt.keys();
    Gb.add_vertices(S);
    Gb.add_vertices(reps);
    for s in S:
        for rep in reps:
            if sum(A[[s],rep_to_cpnt[rep]][0])!=0:
                Gb.add_edge(s,rep);
    #Gb.show();
    
    #Partition reps by Xhats
    Xhats=[];
    for i in range(k):
        Xhats.append([]);
    for rep in reps:
        for i in range(k):
            if rep in all_X[i]:
                Xhats[i].append(rep);
    #print Xhats;
    certificate=Gb_find_Si(Gb,S,Xhats);
    
    if certificate==False:
        return certificate;
    
    ###Below runs only in the case tight partition exists
    if return_matrix==False:
        if return_certificate==True:
            return certificate;
        else:
            return True;
    
    ###Below runs only in the case tight==True and return_matrix==True
    #Start building the tight_A matrix:
    #  for each partite and its corresponding Si
    #  build a digraph DiG and use that to produce a zero sum matrix
    #  then modify tight_A accordingly.
    tight_A=zero_matrix(len(V),len(V));
    for p in range(k):
        Si=certificate[p];
        Xhat=Xhats[p];
        DiG_n=len(Xhat);
        if DiG_n>1:
            induced_Gb=Gb.subgraph(list_union(Si,Xhat));
            mtch=induced_Gb.matching()
            #align two sets by the matching
            Si_order=[-1];
            Xhat_order=[-1];
            for i in range(DiG_n-1):
                u,v,w=mtch[i];
                if u in Si:
                    Si_order.append(u);
                    Xhat_order.append(v);
                else:
                    Si_order.append(v);
                    Xhat_order.append(u);
            for v in Xhat:
                if v not in Xhat_order:
                    Xhat_order[0]=v;
            #print Si_order,Xhat_order;
            DiG=DiGraph(DiG_n,loops=True);
            for j in range(DiG_n):
                DiG.add_edge(0,j);
            for i in range(1,DiG_n):
                for j in range(DiG_n):
                    if induced_Gb.has_edge(Si_order[i],Xhat_order[j]):
                        DiG.add_edge(i,j);
            #DiG.show();
            quotient_matrix=zero_sum_matrix(DiG);
            for i in range(1,DiG_n):
                for j in range(DiG_n):
                    s=Si_order[i];
                    cpnt=rep_to_cpnt[Xhat_order[j]];
                    l_buffer=list(A[[s],cpnt][0]);
                    fixed_sum_list(l_buffer,quotient_matrix[i,j]);
                    tight_A[[s],cpnt]=matrix(l_buffer);
                    tight_A[cpnt,[s]]=matrix(l_buffer).transpose();
    #Find S0, those vertices in S that is not matched with any component
    S0=copy(S);
    for Si in certificate:
        for s in Si:
            S0.remove(s);
    for s in S0:
        tight_A[s,s]=1;
        
    #Fill in Laplacian matrices
    tight_A[Sbar,Sbar]=untight_A[Sbar,Sbar];
        
    #Last check about tight_A
    #should have nullity k!!!
    if tight_A.nullity()!=k:
        print "Something is wrong!!!";
    
    #Find a large L such that L*tight_A+untight_A has nullity k
    # epsilon=1/L
    L=max([abs(untight_A[i,j]) for i in range(len(V)) for j in range(len(V))])+1;
    while True:
        #print "L",L;
        final_A=L*tight_A+untight_A;
        if final_A.nullity()==k:
            ##print "L found";
            if return_certificate==True:
                return [certificate,final_A];
            else:
                return final_A;            
        else:
            L*=10;
            
 def has_null_k_partition(g,k,tight=False,return_matrix=False):
    """
    Input:
        g: a simple graph
        k: k as in null-k partition
        tight: checking tight or not
    Output:
        Return a (tight) null-k partition if there is one, otherwise return False.
    """
    V=g.vertices();
    for S in Combinations(V):
        Sbar=[];
        for v in V:
            if v not in S:
                Sbar.append(v);
        if len(Sbar)>=k:
            for setpar in SetPartitions(Sbar,k):
                nullpartition=(S,[list(X) for X in setpar]);
                k_matrix=is_null_k_partition(g,nullpartition,tight,return_matrix);
                if k_matrix!=False:
                    if return_matrix:
                        return [nullpartition,k_matrix];
                    else:
                        return nullpartition;
    return False;
