# pymeshlabserver
This is just a very bare (and perhaps bad) wrapper of pymeshlab to provide a replacement for the dismissed meshlabserver.

BE WARNED: This is far away from complete and perhaps also inconsistent (e.g. the -l option). Improvements warmly welcome.

At least the simple 3-step should work, i.e., you can replace the old command

```meshlabserver -i input.obj -s script.mlx -o output.obj```

by

```python pymeshlabserver.py -i input.obj -s script.mlx -o output.obj```

To 1) load the "input.obj", 2) execute filter script "script.mlx" and 3) save as "output.obj".

Hope this helps.

# Requirement

Install pymeshlab using 

```pip install pymeshlab```
