#Funtion 1

def dna_to_protein(sequence):
    codon_to_aminoacid = {
        "GCA": "Alanine", "GCC": "Alanine", "GCG": "Alanine", "GCU": "Alanine",
        "AGA": "Arginine", "AGG": "Arginine", "CGA": "Arginine", "CGC": "Arginine",
        "AAC": "Asparagine", "AAT": "Asparagine",
        "GAC": "Aspartic_acid", "GAT": "Aspartic_acid",
        "TGC": "Cysteine", "TGT": "Cysteine",
        "CAA": "Glutamine", "CAG": "Glutamine",
        "GAA": "Glutamic_acid", "GAG": "Glutamic_acid",
        "GGA": "Glycine", "GGC": "Glycine", "GGG": "Glycine", "GGT": "Glycine",
        "ATA": "Isoleucine", "ATC": "Isoleucine", "ATT": "Isoleucine",
        "CTA": "Leucine", "CTC": "Leucine", "CTG": "Leucine", "CTT": "Leucine", "TTA": "Leucine", "TTG": "Leucine",
        "AAA": "Lysine", "AAG": "Lysine",
        "ATG": "Methionine",
        "TTC": "Phenylalanine", "TTT": "Phenylalanine",
        "CCA": "Proline", "CCC": "Proline", "CCG": "Proline", "CCT": "Proline",
        "AGC": "Serine", "AGT": "Serine", "TCA": "Serine", "TCC": "Serine", "TCG": "Serine", "TCT": "Serine",
        "ACA": "Threonine", "ACC": "Threonine", "ACG": "Threonine", "ACT": "Threonine",
        "TGG": "Tryptophan",
        "TAC": "Tyrosine", "TAT": "Tyrosine",
        "GTA": "Valine", "GTC": "Valine", "GTG": "Valine", "GTT": "Valine",
        "TAA": "STOP", "TAG": "STOP", "TGA": "STOP",
    }
    protein_sequence =[]
    for i in range(0,len(sequence),3):
        codon = sequence[i:i+3]
        if codon in codon_to_aminoacid:
            protein_sequence.append(codon_to_aminoacid[codon])

    return protein_sequence

dna_sequence ="ATGCGTACGTACGTACGTACG"
print(dna_to_protein(dna_sequence))


#Function 2

import math

def simulate_population_growth(initial_population, growth_rate, generations,):
    population = initial_population
    for generation in range(generations):
            hour = generation + 1
            population = initial_population * math.exp(growth_rate * hour) 
            print(f"Generation {generation + 1}: Population = {population:.2f}: hour {hour}")

    return population 

simulate_population_growth(100, 1.05, 100)


#Function 3
import math

def time_to_reach_80_percent_carrying_capacity_for_loop(initial_population, growth_rate, carrying_capacity, max_generations):
    target_population = 0.8 * carrying_capacity
    population = initial_population

    for generation in range(max_generations):
        population = population * growth_rate
        if population >= target_population:
            return generation + 1  

    return None  

hours_to_reach_80_percent = time_to_reach_80_percent_carrying_capacity_for_loop(100,1.05,1000,200)

print(f"Hours to reach 80% carrying capacity: {hours_to_reach_80_percent}")


#Function 4
def hamming_distance(str1, str2):
    distance = 0  
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1 
    return distance

distance = hamming_distance("idera121","iydee200")
print(f"Hamming distance: {distance}")
