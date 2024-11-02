"""
Main module for the Finite State Machine
"""
from src.FSMFileReader import FSMFileReader
from src.DeterministicFiniteAutomata import DeterministicFiniteAutomata


class Main:
    """
    Main class for the Finite State Machine
    """

    def __init__(self):
        """
        Constructor for the main class
        """
        self.filename = "src/test.json"
        self.fsm = None
        self.input_string = None

    def check_input_string(self):
        """
        Check if the input string is acceptable
        """
        # Get the input string from the user
        self.input_string = input("Enter the input string: ")

        # Check if the input string is acceptable
        if self.fsm.isAcceptable(self.input_string):
            print("The input string is acceptable.")
        else:
            print("The input string is not acceptable.")

    def run(self):
        """
        Run the Finite State Machine
        """
        # Read the FSM configuration from the file
        reader = FSMFileReader(self.filename)
        states, alphabet, transitions, startState, acceptStates = reader.read_fsm_from_file()

        # Create the DFA
        self.fsm = DeterministicFiniteAutomata(states, alphabet, transitions, startState, acceptStates)
        # Print the DFA
        print(self.fsm)
        # make a loop to check the input string
        while True:
            self.check_input_string()
            if input("Do you want to check another string? (y/n): ") == "n":
                break
        print("Exiting the Finite State Machine.")


if __name__ == '__main__':
    print("Finite State Machine")
    fsm = Main()
    fsm.run()
