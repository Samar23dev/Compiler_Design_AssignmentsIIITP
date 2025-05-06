from graphviz import Digraph

def plot_dfa():
    # Create a directed graph (digraph)
    dot = Digraph(comment='DFA Example')

    # Add nodes (states)
    dot.node('0', 'State 0 (Start, Accepting)')
    dot.node('1', 'State 1')
    dot.node('2', 'State 2')

    # Add edges (transitions)
    dot.edge('0', '0', '0,3,6,9')  # From state 0 to state 0 with 0,3,6,9
    dot.edge('0', '1', '1,4,7')    # From state 0 to state 1 with 1,4,7
    dot.edge('0', '2', '2,5,8')    # From state 0 to state 2 with 2,5,8
    dot.edge('1', '1', '0,3,6,9')  # From state 1 to state 1 with 0,3,6,9
    dot.edge('1', '2', '1,4,7')    # From state 1 to state 2 with 1,4,7
    dot.edge('1', '0', '2,5,8')    # From state 1 to state 0 with 2,5,8
    dot.edge('2', '2', '0,3,6,9')  # From state 2 to state 2 with 0,3,6,9
    dot.edge('2', '0', '1,4,7')    # From state 2 to state 0 with 1,4,7
    dot.edge('2', '1', '2,5,8')    # From state 2 to state 1 with 2,5,8

    # Render and display the DFA diagram
    dot.render('dfa_diagram', format='png', view=True)

# Call the function to generate the diagram
plot_dfa()
