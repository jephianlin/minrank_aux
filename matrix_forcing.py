def one_nonzero_term(p, avoid=[]):
    """
    Input:
        p: a symbolic expression;
           make sure do p=simplify(expand(p)) first;
        avoid: a list of variables that can possibly be zero;
    Output:
        return True if p has only one term
        and the variables in p are not in avoid;
    """
    if p==0:
        return False;
    ghost_var,phantom_var=var("ghost_var,phantom_var"); 
    # Just to avoid the variable names in p;
    if p.operator()==(ghost_var+phantom_var).operator():
        return False;
    p_vars=p.variables();
    for avoid_var in avoid:
        if avoid_var in p_vars:
            return False;
    return True;

def find_next_force(base_matrix,r_ind=None,c_ind=None,in_rows=None,in_columns=None,avoid=[],find_all=False):
    """
    Input:
        base_matrix: a variable matrix;
        r_ind,c_ind: dictionaries mapping indices to row/col numbers;
        in_rows,in_cols: the considered submatrix;
        avoid: a list of variables that can possibly be zero;
        find_all: whether to return all possible forces or not;
    Output:
        a force is a pair [out_rows], [out_columns] such that
        all nonzero entries of base_matrix[out_rows,in_columns]
        are in T=base_matrix[out_rows,out_columns]
        and the determinant of T is nonzero.
        That is, one_nonzero_term(simplify(expand(T.determinant()))) is True;
        return a force or all forces.
    """
    ### init
    Psi=base_matrix;
    m,n=Psi.dimensions();
    if r_ind==None:
        r_ind={k:k for k in range(m)};
    if c_ind==None:
        c_ind={k:k for k in range(n)};
    if in_rows==None:
        in_rows=r_ind.keys();
    if in_columns==None:
        in_columns=c_ind.keys();
    # start searching
    forces_found=[];
    for k in range(1,len(in_rows)+1):
        for out_rows in Combinations(in_rows,k):
            zero_column=matrix(k,[0]*k);
            out_rows_repr=[r_ind[r] for r in out_rows];
            out_columns=[c for c in in_columns if Psi[out_rows_repr,[c_ind[c]]]!=zero_column];
            if len(out_rows)==len(out_columns):
                out_columns_repr=[c_ind[c] for c in out_columns];
                p=simplify(expand(Psi[out_rows_repr,out_columns_repr].determinant()));
                if one_nonzero_term(p,avoid):
                    forces_found.append([out_rows,out_columns]);
                    if find_all==False and len(forces_found)==1:
                        return forces_found[0];
    return forces_found;
    
def effective_rows(base_matrix,r_ind=None,c_ind=None,in_rows=None,in_columns=None,avoid=[]):
    """
    Input:
        base_matrix: a variable matrix;
        r_ind,c_ind: dictionaries mapping indices to row/col numbers;
        in_rows,in_cols: the considered submatrix;
        avoid: a list of variables that can possibly be zero;
    Output:
        return the nonzero rows r such that 
        base_matrix[[r],in_columns] contains no variables in avoid;
    """
    ### init
    Psi=base_matrix;
    m,n=Psi.dimensions();
    if r_ind==None:
        r_ind={k:k for k in range(m)};
    if c_ind==None:
        c_ind={k:k for k in range(n)};
    if in_rows==None:
        in_rows=r_ind.keys();
    if in_columns==None:
        in_columns=c_ind.keys();
    zero_row=matrix(1,[0]*len(in_columns));
    in_columns_repr=[c_ind[c] for c in in_columns];
    nonzero_rows=[r for r in in_rows if Psi[[r_ind[r]],in_columns_repr]!=zero_row];
    wanted_rows=[];
    for in_row in nonzero_rows:
        want=True;
        for in_column in in_columns:
            p=Psi[r_ind[in_row],c_ind[in_column]];
            p_vars=p.variables();
            for avoid_var in avoid:
                if avoid_var in p_vars:
                    want=False;
        if want:
            wanted_rows.append(in_row);
    return wanted_rows;
    
def increasing_order(l):
    """
    Input:
        a list of pairs;
    Ouput:
        replace (a,b) in l with (b,a) if a>b;
    """
    l_len=len(l);
    for k in range(l_len):
        a,b=l[k];
        if a>b:
            l[k]=(b,a);
            
def matrix_zero_forcing(base_matrix,r_ind=None,c_ind=None,in_rows=None,in_columns=None,avoid=[],return_chain=False,return_invertible_block=False):
    """
    Input:
        base_matrix: a variable matrix;
        r_ind,c_ind: dictionaries mapping indices to row/col numbers;
        in_rows,in_cols: the considered submatrix;
        avoid: a list of variables that can possibly be zero;
        return_chain,return_invertible_block: boolean;
    Output:
        return the remaining unknown columns;
        if return [], then the matrix is always full rank;
        if return_chain==True, print the process;
        if return_invertible_block==True, print the invertible block (only work when return_chain==True);
    """
    ### init
    Psi=base_matrix;
    m,n=Psi.dimensions();
    if r_ind==None:
        r_ind={k:k for k in range(m)};
    if c_ind==None:
        c_ind={k:k for k in range(n)};
    if in_rows==None:
        in_rows=r_ind.keys();
    if in_columns==None:
        in_columns=c_ind.keys();
    current_rows=copy(in_rows);
    current_columns=copy(in_columns);
    again=True;
    while len(in_columns)>0 and again:
        again=False;
        eff_rows=effective_rows(Psi,r_ind,c_ind,current_rows,current_columns,avoid);
        f=find_next_force(Psi,r_ind,c_ind,eff_rows,current_columns,avoid);
        if f!=[]:
            again=True;
            if return_chain:
                print("alpha:",f[0]);
                print("beta:",f[1]);
                if return_invertible_block:
                    f0_repr=[r_ind[r] for r in f[0]];
                    f1_repr=[c_ind[c] for c in f[1]];
                    print("invertible_block:");
                    print(Psi[f0_repr,f1_repr]);
                print("---")
            for r in f[0]:
                current_rows.remove(r);
            for c in f[1]:
                current_columns.remove(c);
    return current_columns;
    
def SSPmatrix_matrix_zero_forcing(g,return_chain=False,return_invertible_block=False):
    """
    Input:
        g: a simple graph;
        return_chain,return_invertible_block: boolean;
    Output:
        return the remaining unknown columns;
        if return [], then the SSPmatrix is always full rank;
        if return_chain==True, print the process;
        if return_invertible_block==True, print the invertible block (only work when return_chain==True);
    """
    A=var_matrix(g)
    Psi,r_ind,c_ind=SSPmatrix(A,True)
    avoid=[A[i,i] for i in range(g.order())];
    return matrix_zero_forcing(Psi,r_ind,c_ind,avoid=avoid,return_chain=return_chain,return_invertible_block=return_invertible_block);
 