# Genetic Mutation Detector
# This program compares a normal DNA sequence with a mutated DNA sequence.

def find_mutations(normal_dna, mutated_dna):
    mutations = []

    # Check each position in the DNA sequences
    for i in range(min(len(normal_dna), len(mutated_dna))):
        if normal_dna[i] != mutated_dna[i]:
            mutations.append({
                "position": i + 1,
                "normal": normal_dna[i],
                "mutated": mutated_dna[i]
            })

    # Check for insertions
    if len(mutated_dna) > len(normal_dna):
        for i in range(len(normal_dna), len(mutated_dna)):
            mutations.append({
                "position": i + 1,
                "normal": "-",
                "mutated": mutated_dna[i]
            })

    # Check for deletions
    elif len(normal_dna) > len(mutated_dna):
        for i in range(len(mutated_dna), len(normal_dna)):
            mutations.append({
                "position": i + 1,
                "normal": normal_dna[i],
                "mutated": "-"
            })

    return mutations


# Example DNA sequences
normal_dna = "ATGCGTACGCTA"
mutated_dna = "ATGCGTTCGCTA"

# Find mutations
mutations = find_mutations(normal_dna, mutated_dna)

# Display results
print("GENETIC MUTATION ANALYSIS")
print("-" * 30)

print("Normal DNA  :", normal_dna)
print("Mutated DNA :", mutated_dna)

if mutations:
    print("\nMutations detected:")

    for mutation in mutations:
        print(
            f"Position {mutation['position']}: "
            f"{mutation['normal']} → {mutation['mutated']}"
        )

    print(f"\nTotal mutations: {len(mutations)}")

else:
    print("\nNo mutations detected.")
