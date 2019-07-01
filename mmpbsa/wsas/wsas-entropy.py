import pandas as pd
import numpy as np
import os
import glob

mmpbsa_data = pd.read_csv('../pb_1traj.tsv', sep='\t')

all_ligs = np.array([])

for dirname in glob.glob('l*'):

    tmp_data = np.loadtxt(f"{dirname}/nm-approx-avg.dat", delimiter='\t')

    if all_ligs.any():
        all_ligs = np.vstack((all_ligs, tmp_data))
    else:
        all_ligs = tmp_data

mmpbsa_data['neg_wsas'] = -1.0 * all_ligs[:,0]
mmpbsa_data['neg_wsas_se'] = all_ligs[:,1] / np.sqrt(25)
mmpbsa_data['neg_wsas'] = mmpbsa_data['pb_tot_avg'] + mmpbsa_data['pb_tot_se']
mmpbsa_data['dg_wsas_avg'] = mmpbsa_data['pb_tot_avg'] + mmpbsa_data['neg_wsas']
mmpbsa_data['dg_wsas_se'] = mmpbsa_data['pb_tot_se'] + mmpbsa_data['neg_wsas_se']

mmpbsa_data.to_csv('pb_1traj_wsas_entropy.csv', sep='\t', index=False)


