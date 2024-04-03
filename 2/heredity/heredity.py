import csv
import itertools
import sys

import random

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # print(people)
    # print([*people])
    hidden = {}
    # unconditional probabilities first:
    for person in [*people]:
        hidden[person] = {}
        hidden[person]["gene"] = inherit(person, people, hidden)
    
    print(hidden)
    return hidden





    for person in [*people]:
        hidden[person] = {"gene": {0: 0, 1: 0, 2: 0}}
        if not people[person]["mother"] and not people[person]["father"]:
            for i in range(len(PROBS["gene"])):
                hidden[person]["gene"][i] = PROBS["gene"][i]
            print(hidden[person])
        
           
        
    
        
    for person in [*people]:
        if mother := people[person]["mother"]:             
            mothers_genes = hidden[mother]["gene"]
            print(mothers_genes)
            gene1 = {i: mothers_genes[i] * 0.5 for i in range(len(mothers_genes))}
            print(gene1)
        else:
            gene1 = {i: PROBS["gene"][i] for i in range(len(PROBS["gene"]))}

        if father := people[person]["father"]:
            fathers_genes = hidden[father]["gene"]
            print(fathers_genes)
            gene2 = {i: fathers_genes[i] * 0.5 for i in range(len(fathers_genes))}
            print(gene2)
        
        if person not in one_gene and person not in two_genes:
            for gene in hidden[person]["gene"]:
                hidden [person]["gene"][gene] = (gene1[gene] + gene2[gene]) * 0.5
        
        print(hidden[person])
          

            


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    raise NotImplementedError


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    raise NotImplementedError



def inherit(person, people, hidden):
    if mother := people[person]["mother"]:
        try:
            mothers_genes = hidden[mother]["genes"]
        except KeyError:
            mothers_genes = inherit(mother, people, hidden)

        gene1 = mothers_genes
    
    else:
        gene1 = {i: PROBS["gene"][i] for i in range(len(PROBS["gene"]))}
        
    
    if father := people[person]["father"]:
        try:
            fathers_genes = hidden[mother]["genes"]
        except KeyError:
            fathers_genes = inherit(father, people, hidden)
        
        gene2 = fathers_genes

    else:
        gene2 = {i: PROBS["gene"][i] for i in range(len(PROBS["gene"]))}

    persons_genes = {}
    for gene in [*gene1]:
        persons_genes[gene] = (gene1[gene] + gene2[gene]) / 2
    
    return persons_genes
        
        



def unconditional(person):
    hidden = {}
    hidden[person] = {"gene": {i: PROBS["gene"][i] for i in range(len(PROBS["gene"]))}}
    return hidden


if __name__ == "__main__":
    main()
