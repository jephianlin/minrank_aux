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

def deltaCeiling(gph):
    gph_order=gph.order();
    delta=min(gph.degree());
    if delta==gph_order-1:
        return delta;
    name=gph.canonical_label().graph6_string();
    try:
        return dC_dic[gph_order][name];
    except: 
        pass         
    if gph.is_connected()==False:
        max_dC=delta;
        for com in gph.connected_components_subgraphs():
            max_dC=max(max_dC,deltaCeiling(com));
        return max_dC;
    max_dC=delta;
    for e in gph.edges():
        max_dC=max(max_dC,deltaCeiling(contract_edge(gph,e)));
    return max_dC;
