import pymeshlab
import argparse



parser = argparse.ArgumentParser(description='meshlabserver wrapper for pymeshlab.')
parser.add_argument('-i', nargs='+', action='append', help='input files.')
parser.add_argument('-o', nargs='+', action='append', help='output files.')
parser.add_argument('-s', nargs='+', action='append', help='filter scripts.')
parser.add_argument('-m', nargs='+', action='append', help='output mesh\'s attributes.')
parser.add_argument('-l', help='select layer before saving.')

args = parser.parse_args()

save_options = {'vc': False,
                'vt': False,
                'wt': False}

# print(args.i)
if args.i is not None:
    input_files = [i[0] for i in args.i]
else:
    input_files = []
if args.o is not None:
    output_files = [o[0] for o in args.o]
else:
    output_files = []
if args.s is not None:
    filter_scripts = [s[0] for s in args.s]
else:
    filter_scripts=[]
if args.l is not None:
    save_layer = int(args.l[0])
else:
    save_layer = -1

print(save_layer)

if args.m is not None:
    m = [m[0] for m in args.m]
    if 'vc' in m:
        save_options['vc'] = True
    if 'vt' in m:
        save_options['vt'] = True
    if 'wt' in m:
        save_options['wt'] = True

ms = pymeshlab.MeshSet()
for i in input_files:
    ms.load_new_mesh(i)
for f in filter_scripts:
    ms.load_filter_script(f)
    ms.apply_filter_script()
for o in output_files:
    if save_layer != -1:
        ms.set_current_mesh(save_layer)
    ms.save_current_mesh(o, 
    save_vertex_coord = save_options['vt'], 
    save_vertex_color = save_options['vc'],
    save_wedge_texcoord = save_options['wt'])


# ms.save_current_mesh()