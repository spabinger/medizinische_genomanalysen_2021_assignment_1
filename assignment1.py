import pysam
import pybedtools

__author__ = 'XXX'

##
## Concept:
## TODO
##

class Assignment1:

    def __init__(self):
        self.bamfile_path = "chr21_small.bam"

    def get_gene_information(self):
        return {"symbol": "RRP1B",
                "refseq": "NM_015056",
                "chr": "chr21",
                "tx_start": 43659559,
                "tx_end": 43696079,
                "strand": "+",
                "num_exons": 16,
                "exons_start": "43659559,43669883,43672307,43673869,43674635,43675033,43676271,43676732,43683278,43684552,43685769,43686803,43687515,43690287,43691438,43693189",
                "exons_end": "43659794,43669966,43672365,43673955,43674697,43675163,43676336,43676914,43683373,43684650,43685789,43686935,43688240,43690440,43691502,43696079"
                }

    def get_gene_symbol(self):
        return None

    ## Return: chr:start-end
    def get_region_of_gene(self):
        return None

    def get_number_of_exons(self):
        return None

    def get_number_mapped_reads(self):
        return None

    def get_aligner_from_sam_header(self):
        return None

    def get_number_of_properly_paired_reads_of_gene(self):
        return None

    ## Use bedtools - genome_coverage
    def calculate_average_genome_coverage_of_file(self):
        return None
