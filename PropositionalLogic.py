# experiment 6
# ---- Program A: Manual Logical Evaluation ----

# Define implication and biconditional functions
def implies(p, q):
    return (not p) or q

def iff(p, q):
    return (p and q) or (not p and not q)

# Step 1: Define truth values of propositions
# You can change the values here for different test cases
propositions = {
    'P': True,
    'Q': False,
    'R': True
}

# Step 2: Evaluate various logical expressions
def evaluate_expressions():
    print("\n--- Propositional Logic Evaluation (Program A) ---")

    # Expression 1: P ∧ Q
    result1 = propositions['P'] and propositions['Q']
    print("P ∧ Q =", result1)

    # Expression 2: P ∨ Q
    result2 = propositions['P'] or propositions['Q']
    print("P ∨ Q =", result2)

    # Expression 3: ¬Q
    result3 = not propositions['Q']
    print("¬Q =", result3)

    # Expression 4: P → Q
    result4 = implies(propositions['P'], propositions['Q'])
    print("P → Q =", result4)

    # Expression 5: P ↔ R
    result5 = iff(propositions['P'], propositions['R'])
    print("P ↔ R =", result5)

# Step 3: Call the evaluator
evaluate_expressions()



# ---- Program B: Automated Reasoning using SymPy ----

from sympy import symbols, And, Not, Implies
from sympy.logic.inference import satisfiable

print("\n--- Knowledge Base Reasoning (Program B) ---")

# Step 1: Define propositional symbols
P, Q = symbols('P Q')

# Step 2: Knowledge base (KB): (P → Q) ∧ P
kb = And(Implies(P, Q), P)

# Step 3: Query: Q
query = Q

# Step 4: Check if KB ⊨ Q using resolution (i.e., is KB ∧ ¬Q unsatisfiable?)
result = not satisfiable(And(kb, Not(query)))

# Step 5: Output
print(f"Does KB entail Q? {result}")
