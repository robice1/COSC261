def epsilon_closure(state, nfa):
    closure = set()
    stack = [state]

    while stack:
        current_state = stack.pop()
        closure.add(current_state)

        if current_state in nfa and '_' in nfa[current_state]:
            epsilon_transitions = nfa[current_state]['_']
            for next_state in epsilon_transitions:
                if next_state not in closure:
                    stack.append(next_state)

    return closure

multi_transition_nfa = {
       0: {"_": {2, 1}, "a": {1}, "b": {2}},
       1: {"a": {1}, "b": {0}},
       2: {"_": {3, 1}, "a": {1}, "b": {2}},
       3: {"a": {2}}
      }
for i in range(4):
    print(f"Epsilon closure for q{i}: {sorted(epsilon_closure(i, multi_transition_nfa))}")