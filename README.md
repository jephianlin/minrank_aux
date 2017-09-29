minimum_rank_aux
================
auxiliary tools for the minimum rank problem

Please evaluate the line below:

```python
# First load the minimum rank library by Jason Grout et al.
URL='https://raw.githubusercontent.com/jephianlin/mr_JG/master/'
files=['Zq_c.pyx','Zq.py','zero_forcing_64.pyx','zero_forcing_wavefront.pyx','minrank.py', 'inertia.py']
for f in files:
    load(URL+f)
    
# Then load this repository.
load("https://raw.githubusercontent.com/jephianlin/minimum_rank_aux/master/load_all.py");
```
