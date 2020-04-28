#!/bin/bash
if not [ -d "run" ]
	then
		mkdir run
	fi

for j in {'NB1','NB2','NB3','NB4','PP1','PP2','PEN','BUT'}; do
	if [ -d "run/${j}" ]
		then
			rm -r run/${j}
		fi
	mkdir run/${j}
  for i in {1..500}; do
    bsub -n 1 -W 00:59 -o /dev/null rosetta_scripts.hdf5.linuxgccrelease @relax.flags -extra_res_fa ligs/${j}.params -enzdes:cstfile ligs/${j}.enzdes.cst -s pdb_inp/I133F_${j}.pdb -out:path:all run/${j} -out:suffix _$i
  done
done
