from graphviz import Digraph

def plot_dfa():
    try:
        # Create a directed graph (digraph)
        dot = Digraph(comment='DFA Example')

        # Set global attributes for the diagram
        dot.attr(size='10,10')  # Set the size of the entire diagram (width, height)

        # Add nodes (states), making state 0 an accepting state (double circle)
        dot.node('0', 'State 0 (Start, Accepting)', shape='doublecircle', width='1.3', height='1.3', fontsize='10')  # Double circle for accepting state, with size and font
        dot.node('1', 'State 1', width='1.2', height='1.2', fontsize='12')  # Size and font for state 1
        dot.node('2', 'State 2', width='1.2', height='1.2', fontsize='12')  # Size and font for state 2

        # Add the initial state arrow
        dot.node('start', '', shape='point')  # Invisible starting point node
        dot.edge('start', '0')  # Arrow pointing to state 0 (initial state)

        # Add edges (transitions) with stack operations
        dot.edge('0', '0', '0,3,6,9', penwidth='2')  # From state 0 to state 0 with 0,3,6,9
        dot.edge('0', '1', '1,4,7', penwidth='2')    # From state 0 to state 1 with 1,4,7
        dot.edge('0', '2', '2,5,8', penwidth='2')    # From state 0 to state 2 with 2,5,8
        dot.edge('1', '1', '0,3,6,9', penwidth='2')  # From state 1 to state 1 with 0,3,6,9
        dot.edge('1', '2', '1,4,7', penwidth='2')    # From state 1 to state 2 with 1,4,7
        dot.edge('1', '0', '2,5,8', penwidth='2')    # From state 1 to state 0 with 2,5,8
        dot.edge('2', '2', '0,3,6,9', penwidth='2')  # From state 2 to state 2 with 0,3,6,9
        dot.edge('2', '0', '1,4,7', penwidth='2')    # From state 2 to state 0 with 1,4,7
        dot.edge('2', '1', '2,5,8', penwidth='2')    # From state 2 to state 1 with 2,5,8

        # Render and display the DFA diagram
        dot.render('dfa_diagram_with_size', format='png', view=True)
        print("DFA Diagram with size adjustments has been successfully created and displayed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to generate and display the DFA
plot_dfa()
