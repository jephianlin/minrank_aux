URL='https://raw.githubusercontent.com/jephianlin/minimum_rank_aux/master/'
files=['oc_diag_analysis.sage','xi_dict.py','mu_dict.py', 'general_Lib.py','SXP.py']
for f in files:
    print "Loading %s..."%f;
    load(URL+f);
