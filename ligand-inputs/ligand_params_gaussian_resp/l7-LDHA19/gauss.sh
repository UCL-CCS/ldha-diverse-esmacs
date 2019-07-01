#!/bin/csh -f
# setting the environment for the SGE
#$ -cwd -V
#$ -q all.q
#$ -A g09_c01
#$ -pe smp 8
#$ -N lig7-ldha
 
# setting the Gaussian environment
if (-e /usr/local/g09_c01 ) then

# making and setting the scratch directory
setenv GAUSS_SCRDIR /scr/gf/dave/$JOB_ID
mkdir -p $GAUSS_SCRDIR

setenv g09root /usr/local
source $g09root/g09_c01/bsd/g09.login
setenv GAUSS_EXEDIR $g09root/g09_c01
 
# starting the job
$g09root/g09_c01/g09 < lig7.gau > lig7.out
 
endif
