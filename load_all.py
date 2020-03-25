# increase timeout seconds
def loadurl(url, timeout=5):
    temp_name = tmp_filename() + '.' + os.path.splitext(url)[1][1:]

    from urllib.request import urlopen
    content = urlopen(url, timeout=timeout)
    with open(temp_name, 'wb') as f:
        f.write(content.read())
    sage.repl.load.load(temp_name, globals())
    os.unlink(temp_name)

def load_all(mr_JG=True, minrank_aux=True, timeout=5, load_func='load'):
    # load_func can be 'loadurl' (default) or 'load'
    if load_func == 'load':
        func = load
    if load_func == 'loadurl':
        func = lambda url: loadurl(url, timeout=timeout)
    
    if mr_JG:
        URL='https://raw.githubusercontent.com/jephianlin/mr_JG/master/'
        files=['Zq_c.pyx','Zq.py','zero_forcing_64.pyx','zero_forcing_wavefront.pyx','minrank.py', 'inertia.py']
        for f in files:
            print("Loading %s..."%f);
            func(URL+f) 
    
    if minrank_aux:
        URL='https://raw.githubusercontent.com/jephianlin/minrank_aux/master/'
        files=['general_Lib.sage','oc_diag_analysis.sage','xi_dict.py','mu_dict.py','SXP.sage','matrix_forcing.py']
        for f in files:
            print("Loading %s..."%f);
            func(URL+f);
