"""
2026_04_16

Fibonacci sequence exercise for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.
"""

# step 1 - get number of Fibonacci terms
n_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# step 2 - compute Fibonacci sequence
fib_term_1 = 0
fib_term_2 = 1
fib_sequence = []
for _ in range(n_terms):
    temp = fib_term_2
    fib_term_2 = fib_term_1 + fib_term_2
    fib_term_1 = temp
    fib_sequence.append(fib_term_2)

# step 3 - print generated sequence
print(f"First {n_terms} of the Fibonacci sequence:")
print(fib_sequence)

# step 4 (bonus): write to fibonacci.txt
# The 'with' statement handles file closing automatically
with open("fibonacci.txt", "w") as f:
    ### alternative 1: just cast it to string
    content = str(fib_sequence)
    ### alternative 2: format it in a pretty way with commas
    # content = ", ".join(map(str, fib_sequence))
    ### alternative 3: format it in a pretty way with line breaks
    # content = ""
    # for fib_term in fib_sequence:
    #     content += str(fib_term) + '\n'
    ### write content
    f.write(content)
print("\nSuccessfully saved to 'fibonacci.txt'")