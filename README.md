
# 🧬 Genetic Mutation Detector

## 📌 Overview

The **Genetic Mutation Detector** is a simple Python-based project that compares a normal DNA sequence with a mutated DNA sequence. It identifies differences between the two sequences and reports the position and nucleotide involved in each mutation.

This project provides a basic introduction to how programming can be used in **genetics and bioinformatics** to analyze DNA sequences.

## 🎯 Objective

The main objective of this project is to:

* Compare two DNA sequences.
* Identify changes in nucleotide bases.
* Detect substitutions, insertions, and deletions.
* Display the location of detected mutations.
* Calculate the total number of mutations.

## 🧬 DNA Sequences

DNA consists of four nucleotide bases:

* **A** – Adenine
* **T** – Thymine
* **G** – Guanine
* **C** – Cytosine

A mutation occurs when the DNA sequence undergoes a change, such as a nucleotide being replaced, added, or removed.

## 🔬 Types of Mutations

### 1. Substitution

A nucleotide is replaced by another nucleotide.

```text
Normal  : ATGCGTA
Mutated : ATGCGTT
                 ↑
```

### 2. Insertion

One or more nucleotides are added to the DNA sequence.

```text
Normal  : ATGCGTA
Mutated : ATGCCGTA
             ↑
```

### 3. Deletion

One or more nucleotides are removed from the DNA sequence.

```text
Normal  : ATGCCGTA
Mutated : ATGCGTA
             ↑
```

## 💻 Technologies Used

* Python 3
* String manipulation
* Functions
* Loops
* Conditional statements

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/genetic-mutation-detector.git
```

Navigate to the project directory:

```bash
cd genetic-mutation-detector
```

Run the Python program:

```bash
python genetic_mutation.py
```

## 📊 Example

### Input

```text
Normal DNA  : ATGCGTACGCTA
Mutated DNA : ATGCGTTCGCTA
```

### Output

```text
GENETIC MUTATION ANALYSIS
------------------------------
Normal DNA  : ATGCGTACGCTA
Mutated DNA : ATGCGTTCGCTA

Mutations detected:
Position 7: A → T

Total mutations: 1
```

## 🌍 Applications

DNA sequence analysis is used in areas such as:

* Genetic research
* Disease research
* Biotechnology
* Bioinformatics
* Personalized medicine
* Evolutionary studies

## 🔮 Future Improvements

Future versions of this project could include:

* Analysis of larger DNA sequences.
* FASTA file support.
* Visualization of mutations.
* More detailed mutation classification.
* Analysis of real genetic datasets.
* Integration with biological databases.

## ⚠️ Disclaimer

This project is intended **for educational purposes only**. It is a basic DNA sequence comparison tool and should not be used for medical diagnosis or clinical genetic analysis.

## 👩‍💻 Author

**Your Name**

### 🧬 Project: Genetic Mutation Detector

**Language:** Python
**Domain:** Genetics & Bioinformatics
