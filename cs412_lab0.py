"""
One line summary of program.

Author: Devon Boldt

Honor Code and Acknowledgments: 
    This work complies with the JMU Honor Code.
    I worked with Tommy Lane on this lab in class

What Python collection types did you use? What are the underlying data structures for these types?
    We used a dictionary which uses a HashTable as it's datastructure  

What data structure operations did you use? (List all of them.)


Assuming a data structure of size n, what is the run time of each of the operations you identified above?

What is the expected run time of your algorithm?
    n+
"""

# Main function 
def main():
    # Getting the lines 
    n = int(input()) 
    dict = {} 
    for i in range(n):
        dict[i] = input() 

    sentence = input() 

    for i in sentence.split(" "):
        if i in dict: 
            print(dict[i], end = " ")
        else: 
            print("-1", end = " ") 

# Unused for this lab
if __name__ == "__main__":
    # main must be called when the script is executed.
    main()