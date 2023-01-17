## Installation </br>
```
https://gencore.bio.nyu.edu/variant-calling-pipeline-gatk4/
conda activate nf-env
conda install -c bioconda gatk4
conda install openjdk=8 (Java 8)
conda install -c bioconda picard
conda install nextflow 
conda install -c bioconda snpeff (Need higher Java version)
https://gatk.broadinstitute.org/hc/en-us/articles/360041320571--How-to-Install-all-software-packages-required-to-follow-the-GATK-Best-Practices
https://www.youtube.com/watch?v=iHkiQvxyr5c&ab_channel=Bioinformagician
```

## Databases
```
Reference genome and variant annotation
https://www.ncbi.nlm.nih.gov/genome/guide/human/
Clinvar
https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/
https://www.ncbi.nlm.nih.gov/variation/docs/human_variation_vcf/
https://github.com/jmchilton/SnpEffect/blob/493a7615355a5f2c520b199ed6afa5532595dde8/scripts_build/db_GRCh.sh
```

## Running
```
Download GRCh38_latest_genomic.fna.gz 
gzip -dk GRCh38_latest_genomic.fna.gz
bwa index GRCh38_latest_genomic.fna.gz
samtools faidx GRCh38_latest_genomic.fna
picard CreateSequenceDictionary R=GRCh38_latest_genomic.fna O=GRCh38_latest_genomic.dict
nextflow run main2.nf
python runpythonpipeline.py
Directory: gwas/brca_analysis
```

## Remarks

To call variants in samples that are heterogeneous, such as human tumors and mixed microbial populations, in which allele frequencies vary continuously between 0 and 1 researcher should use GATK4 Mutect2 which is designed to identify subclonal events (workflow coming soon). 

## References
```
https://diagnostech.co.za/intro-to-ngs-data-analysis-workflow/
https://gencore.bio.nyu.edu/variant-calling-pipeline-gatk4/
https://pcingola.github.io/SnpEff/examples/#example-1-coding-variants
https://github.com/jmchilton/SnpEffect/blob/493a7615355a5f2c520b199ed6afa5532595dde8/scripts/annotate_demo.sh
https://www.sciencedirect.com/science/article/pii/S1525157814002402#bib24
https://genomics.sschmeier.com/ngs-annotation/index.html (full pipeline for bacteria)
https://hbctraining.github.io/In-depth-NGS-Data-Analysis-Course/sessionVI/lessons/03_annotation-snpeff.html
https://joemcgirr.github.io/files/code_tutorials/my_genome/SnpEFF.html (very good)
```
