class DeterministicFiniteAutomata:
    def __init__(self, states, inputs, transitionTable, startState, acceptingState):
        """
        Initializes the DFA with the given states, inputs, transition table, start state, and accepting states.
        :param states: ِA set of states.
        :param inputs: A set of input symbols.
        :param transitionTable: A dictionary with key state and value is a dictionary with key symbol and value is the next state.
        :param startState: The state to start in.
        :param acceptingState: A set of accepting states, where the DFA will accept if it lands on any of these states.
        """
        self.states = states
        self.alphabet = inputs
        self.transitions = transitionTable
        self.startState = startState
        self.acceptStates = acceptingState
        self.validateInputs()

    def validateInputs(self):
        """
        Validates the DFA's configuration to ensure all states, transitions, and accept states are valid.
        :raises ValueError: If the start state is not in the set of states,
                            a transition state is not in the set of states,
                            a transition symbol is not in the alphabet,
                            or an accept state is not in the set of states.
        """
        # Validate the start state
        if self.startState not in self.states:
            raise ValueError(f"Start state '{self.startState}' is not in the set of defined states.")
        # Validate the transition table
        for state in self.transitions:
            if state not in self.states:
                raise ValueError(f"State '{state}' in transition table is not in the set of defined states")
            for symbol in self.transitions[state]:
                if symbol not in self.alphabet:
                    raise ValueError(f"Symbol '{symbol}' in transition table is not in the alphabet.")
                if self.transitions[state][symbol] not in self.states:
                    raise ValueError(f"Next state '{self.transitions[state][symbol]}' in transition table is not in "
                                     f"the set of defined  states.")
        # Validate that all states have transitions for all symbols in the alphabet
        for state in self.states:
            for symbol in self.alphabet:
                if symbol not in self.transitions[state]:
                    raise ValueError(f"the transition for state '{state}' and symbol '{symbol}' is not defined.")

        # Validate the accept states
        for accept_state in self.acceptStates:
            if accept_state not in self.states:
                raise ValueError(f"Accept state '{accept_state}' is not in the set of defined states.")

    def valideString(self, input_string):
        """
        Validates the input string to ensure all symbols are in the alphabet.
        :param input_string: The string to validate that all symbols are in the alphabet.
        :raises ValueError: If any symbol in the input string is not in the alphabet.
        """
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Symbol '{symbol}' in input string is not in the alphabet.")
                return False
        return True


    def __str__(self):
        """
        Returns a string representation of the DFA.
        :return: A string representation of the DFA.
        """
        print("States: ", self.states)
        print("Alphabet: ", self.alphabet)
        # Print the transitions as a table
        print("Transitions:")
        for state in self.transitions:
            print(f"  {state}: {self.transitions[state]}")

        print("Start State: ", self.startState)
        print("Accept States: ", self.acceptStates)
        return ""

    def isAcceptable(self, inputString):
        """
         Checks if the input string is acceptable by the DFA.
        :param inputString: The string to check.
        :return: True if the string is acceptable, False otherwise.
        """
        # Validate the input string
        if self.valideString(inputString) is False:
            return False
        # Start at the start state
        current_state = self.startState
        print(f"Starting at state: {current_state}")
        # Process each symbol in the input string
        for symbol in inputString:
            print(f"Current state: {current_state}, symbol: '{symbol}'")
            if current_state in self.transitions:  # Check if there is a valid transition
                current_state = self.transitions[current_state][symbol]
                print(f"Transitioning to state: {current_state}")
            else:  # No valid transition
                print(f"No valid transition from state {current_state} on symbol '{symbol}'")
                return False  # Reject the input string

        # Check if the final state is an accepting state
        if current_state in self.acceptStates:
            print("Reached an accepting state.")
            return True  # Accept the input string
        else:
            print("Did not reach an accepting state.")
            return False  # Reject the input string
