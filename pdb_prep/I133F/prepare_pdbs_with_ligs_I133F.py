#!/usr/bin/python

from pymol import cmd
from os import sys

### First load all generated .mol2 files from ligand_prep folder
cmd.delete('*')
cmd.load('I133F_B.pdb','I133F_target')
current_cwd=os.getcwd()
loaded_ligs=[]
for file in os.listdir('../ligs'):
	if file.endswith('0001.pdb'):
		ligand_name=file.split('_')[0]
		loaded_ligs.append(ligand_name)
		cmd.load('../ligs/'+file,ligand_name)

target_atom1='I133F_target and name C12'
target_atom2='I133F_target and name C13'
target_atom3='I133F_target and name C14'

for ligand in loaded_ligs:
	mobile_atom1=ligand+' and name C12'
	mobile_atom2=ligand+' and name C13'
	mobile_atom3=ligand+' and name C14'
	cmd.pair_fit(mobile_atom1,target_atom1,mobile_atom2,target_atom2,mobile_atom3,target_atom3)

cmd.remove('I133F_target and resn PEN')

for ligand in loaded_ligs:
	cmd.fuse('I133F_target and resn LYM and name NZ',ligand+' and name C13','3')
	cmd.bond(ligand+' and resn LYM and name NZ',ligand+' and name C13')
	cmd.save('I133F_'+ligand+'.pdb',ligand,'0')

# for object in cmd.get_object_list('(all)'):
# 	cmd.alter(object,'resn="'+three_letter_code+'"')
# 	counter+=1
# 	if counter==1:
# 		target_object=object
# 		target_atom1=target_object+' and name '+atoms_to_align[0]
# 		target_atom2=target_object+' and name '+atoms_to_align[1]
# 		target_atom3=target_object+' and name '+atoms_to_align[2]
# 		for element in delete_atoms:
# 			print("got here")
# 			cmd.remove('{object} and name {element}'.format(object=object,element=element))
# 	if counter > 1:
# 		mobile_atom1=object+' and name '+atoms_to_align[0]
# 		mobile_atom2=object+' and name '+atoms_to_align[1]
# 		mobile_atom3=object+' and name '+atoms_to_align[2]
# 		print(target_atom1)
# 		print(mobile_atom1)
# 		cmd.pair_fit(mobile_atom1,target_atom1,mobile_atom2,target_atom2,mobile_atom3,target_atom3)
# 		for element in delete_atoms:
# 			cmd.remove('{object} and name {element}'.format(object=object,element=element))
# cmd.join_states(three_letter_code+'.rotlib','*')
# cmd.save(three_letter_code+'.rotlib.pdb',three_letter_code+'.rotlib','0')
# cmd.save(three_letter_code+'_edited.mol2','Molecule_Name_0001')
