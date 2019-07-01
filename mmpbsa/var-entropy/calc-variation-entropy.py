import pandas as pd
import numpy as np
import os

# Units = kcal/mol
kb = 0.0019872041
kbt =  kb * 300
beta = 1.0/kbt

summary_dir = '../raw-summary/'

negative_tds = []
tds_dev = []

for ligand_no in range(1, 23):

    ligand_dir = os.path.join(summary_dir, 'l{:d}'.format(ligand_no))

    com_filepath = os.path.join(ligand_dir, 'lig{:d}-com-mm.dat'.format(ligand_no))
    rec_filepath = os.path.join(ligand_dir, 'lig{:d}-rec-1traj-mm.dat'.format(ligand_no))
    lig_filepath = os.path.join(ligand_dir, 'lig{:d}-lig-1traj-mm.dat'.format(ligand_no))

    com_data = pd.read_csv(com_filepath, sep='\t', index_col = ['replica', 'frame'])
    rec_data = pd.read_csv(rec_filepath, sep='\t', index_col = ['replica', 'frame'])
    lig_data = pd.read_csv(lig_filepath, sep='\t', index_col = ['replica', 'frame'])

    rep_negative_tds = []

    for replica_no in range(1, 26):
        diff = com_data.loc[replica_no] - rec_data.loc[replica_no] - lig_data.loc[replica_no]
        diff_int = diff[['1-4_eel', '1-4_vdw', 'vdwaals', 'eel']].sum(axis=1)
        avg_int = diff_int.mean()
        change_eint = diff_int - avg_int
        rep_negative_tds.append(kbt*np.log(np.mean(np.exp((beta*change_eint)))))

    negative_tds.append(np.mean(rep_negative_tds))
    tds_dev.append(np.std(rep_negative_tds))

ligand_no = 1

mm_1traj = pd.read_csv('../pb_1traj.tsv', sep='\t')

mm_1traj['neg_tds_avg'] = negative_tds
mm_1traj['neg_tds_se'] = tds_dev/np.sqrt(25)
mm_1traj['dg_avg'] = mm_1traj['pb_tot_avg'] + mm_1traj['neg_tds_avg']
mm_1traj['dg_se'] = mm_1traj['pb_tot_se'] + mm_1traj['neg_tds_se']

mm_1traj.to_csv('pb_1traj_var_entropy.csv', sep='\t', index=False)
