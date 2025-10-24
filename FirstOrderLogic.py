# experiment 7

from kanren import Relation, facts, run, var, conde

# Step 1: Define relations
student = Relation()
likes = Relation()

# Step 2: Add facts to the Knowledge Base (KB)
facts(student, ("alice",), ("bob",))
facts(likes, ("alice", "math"), ("bob", "science"))

# Step 3: Rule: If someone is a student and likes something, they are intelligent
def is_intelligent(person):
    return conde((student(person), likes(person, var())),)

# Step 4: Get query from user
name = input("Enter the name to check if intelligent: ").lower()

# Step 5: Logic variable for query
x = var()

# Step 6: Check if the entered person satisfies the rule
result = run(0, x, is_intelligent(name))

# Step 7: Output the result
if result:
    print(f"{name.title()} is intelligent ✅")
else:
    print(f"{name.title()} is not found or does not satisfy the rule ❌")