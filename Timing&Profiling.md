## Use lprun to display the time used by every line (example in Jupyter)  
```
import line_profiler
def load_ipython_extension(ip):
    ip.define_magic('lprun', line_profiler.magic_lprun)
%load_ext line_profiler
%lprun -f foo foo(parameters)
```
(http://pynash.org/2013/03/06/timing-and-profiling/)  
(http://stackoverflow.com/questions/19942653/interactive-python-cannot-get-lprun-to-work-although-line-profiler-is-impor)  

