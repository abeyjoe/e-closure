# ε-closure Algorithm Implementation in Python

# Example NFA transition table
transitions = {
    0: {'epsilon': [1, 2]},  # State 0 has ε-transitions to states 1 and 2
    1: {'epsilon': [3]},     # State 1 has ε-transition to state 3
    2: {'epsilon': []},      # State 2 has no ε-transitions
    3: {'epsilon': [4]},     # State 3 has ε-transition to state 4
    4: {'epsilon': []}       # State 4 has no ε-transitions
}

def epsilon_closure(start_state, transitions):
    """
    Compute the ε-closure of a given state in an NFA.
    :param start_state: The starting state for which ε-closure needs to be computed.
    :param transitions: Dictionary representing ε-transitions of the NFA.
    :return: A set containing all states in the ε-closure of the given state.
    """
    closure_set = set()  # To store the ε-closure states
    stack = []  # Stack for iterative processing

    # Initialize with the start state
    closure_set.add(start_state)
    stack.append(start_state)

    # Process stack while it's not empty
    while stack:
        current_state = stack.pop()
        # Get ε-transitions from the current state
        epsilon_transitions = transitions.get(current_state, {}).get('epsilon', [])

        for next_state in epsilon_transitions:
            if next_state not in closure_set:
                closure_set.add(next_state)  # Add to closure set
                stack.append(next_state)     # Push to stack for further exploration

    return closure_set

# Example usage
start_state = 0
closure = epsilon_closure(start_state, transitions)
print(f"ε-closure of state {start_state}: {closure}")
