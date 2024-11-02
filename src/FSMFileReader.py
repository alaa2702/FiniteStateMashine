import json


class FSMFileReader:
    def __init__(self, filename):
        """
        Initializes the FSMFileReader with the filename of the JSON file containing the FSM configuration.
        :param filename:  The filename of the JSON file containing the FSM configuration.
        """
        self.filename = filename

    def read_fsm_from_file(self):
        """
        Reads FSM configuration and input string from a JSON file.

        :return: Tuple containing states, alphabet, transitions, start_state, accept_states, and input_string.
        """
        with open(self.filename, 'r') as file:
            data = json.load(file)

        # Extracting FSM components from JSON data
        states = set(data["states"])
        alphabet = set(data["alphabet"])
        startState = data["startState"]
        acceptStates = set(data["acceptStates"])

        # Converting transitions from nested JSON to dictionary within a dictionary format
        transitions = data["transitions"]

        return states, alphabet, transitions, startState, acceptStates
