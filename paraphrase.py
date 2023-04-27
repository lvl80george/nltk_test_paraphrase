from nltk.tree import Tree
# trees in natural language toolkit, needed to handle syntactic trees
from itertools import permutations
# to do permutations

#           PARAPHRASING NP's IN A SYNTAX TREE
#   task
#   1) find all the noun phrases that consist of several noun phrases
#   2) find all the possible permutations of children NP's in the parent NP

def paraphrase(original, limit=-1):
    # find all the noun phrases that consist of several noun phrases (step 1)
    # Generate all the subtrees of this tree,
    # restricted to trees matching the filter function (that's NP's with multiple NP's inside)
    def filter (t):
        if t.label() != 'NP': return False
        nested_np_count = 0
        for child in t:
            if child.label() == 'NP': nested_np_count += 1
        if nested_np_count > 1: return True
        return False
    # find all the possible permutations of children NP's in the parent NP(step2)   
    np_subtrees = original.subtrees(filter) # returns a generator object to iterate through
    nodes_for_permutations = [] # nodes/ subtrees to be processed
    for i in np_subtrees: # prepare these to permutations
        child_nps = [] # list of an NP's children that are NP's + their indices
        for j, child in enumerate(i):
            if child.label() == 'NP': child_nps.append((j, child))
        nodes_for_permutations.append((i, child_nps))
    
    
    results = []
    def rec(level):
        if(len(nodes_for_permutations) == level):# finished one variant
            results.append(original.copy(deep=True))# save a tree variant to results
            return # exit recursion
        if(limit != -1)and(len(results) == limit):
            return # we hit the maximum number of results needed
        # otherwise do a permutation
        processed_node, children = nodes_for_permutations[level]
        permutations_ids = permutations(range(0, len(children)))#[1,2,3][2,1,3]...
        for p in permutations_ids:
            # do the permutations
            for i in range(0, len(children)):
                processed_node[children[i][0]] = children[p[i]][1]#rearrange
            rec(level+1)
    
    rec(0) # start recursion
    return results
    
        

        

#   DRIVER CODE

def paraphrase_driver():
    t = Tree.fromstring("""(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )""")
    results = paraphrase(t)
    for r in results:
        print(r)
