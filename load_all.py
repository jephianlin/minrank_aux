URL='https://raw.githubusercontent.com/jephianlin/minimum_rank_aux/master/'
files=['general_Lib.sage','oc_diag_analysis.sage','xi_dict.py','mu_dict.py','SXP.sage','matrix_forcing.py']
for f in files:
    print("Loading %s..."%f);
    load(URL+f);
