# HYP
Scripts associated with HYP analysis.
All input files provided.

Repository includes:
Zygosity - to empirically derive probability of homozygous individuals.
"Perm_probability_of_homozygous_idndividuals_based_on_population_of_alleles.py", which, based on a population of alleles ("HYP1_population.txt") randomly selects 2 "parents" for each of X individuals, and computes zygosity. Millions of permutations possible.

Simulate_HVDs - to simulate HVDs from HYP1 in silico.
"Compute_HVDs_based_on_positional_probability_and_known_pairs.py", which will generate HVDs motif by motif, based on the probability of a given motif at that position (probability of end of HVD at position 28 is 1), provided that the the selected motif is known to occur after whatever motif was in current position-1. This list can be triaged to report only those that are > length 20, and have known start or end patterns because they seem to be the most conserved arrangements, using a second custom python script "Triage_simulated_HVDs_based_on_known_starts_and_ends.py". Positional probabilities are provided as individual files ("xpos")



