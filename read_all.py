URL='https://raw.githubusercontent.com/jephianlin/minimum_rank_aux/master/'
files=['oc_diag_analysis.sage','xi_dict.py','mu_dic.py', 'general_Lib.py']
for f in files:
    load(URL+f);
    print "Loading %s"%f;
