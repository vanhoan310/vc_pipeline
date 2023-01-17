import os
import traceback
import logging
import glob

conda_dir = 'source ~/miniconda3/etc/profile.d/conda.sh && conda activate py27 && '
snpsift_bin =conda_dir+'java -Xmx100g -jar SnpSift.jar annotate -v '
# database = '/data/hoan/gwas/brca_analysis/reference/GRCh38/GRCh38_latest_clinvar.vcf'
database = '/data/hoan/gwas/brca_analysis/reference/GRCh38/GRCh38_latest_dbSNP_all.vcf'
# input_file = '/data/hoan/gwas/brca_analysis/GRCh38_out/out/filtered_snps/01_S1_L001_filtered_snps_2.vcf'
# output_file = '/data/hoan/gwas/brca_analysis/GRCh38_out/file_python.dbSnp.vcf'

# cmd_SNPSift = snpsift_bin + database + ' ' + input_file + ' > ' + output_file
# os.system(cmd_SNPSift)

vcf_list = glob.glob("/data/hoan/gwas/brca_analysis/GRCh38_out/out/filtered_indels/*2.vcf")
# vcf_list = glob.glob("/data/hoan/gwas/brca_analysis/GRCh38_out/out/filtered_indels/*.vcf")
for input_file in vcf_list:
    print(input_file)
    file_name = input_file.split("/")[-1][:10]
    output_file = '/data/hoan/gwas/brca_analysis/GRCh38_out/'+file_name+'_indels_dbSnp_ann.vcf'
    cmd_SNPSift = snpsift_bin + database + ' ' + input_file + ' > ' + output_file
    os.system(cmd_SNPSift)
    print('------------------------------------------------------------------------------------\n')
