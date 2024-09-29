from abc import abstractmethod


class Agent:
    """
    Base class for all agents.
    """

    def __init__(self):
        pass

    @abstractmethod
    def play(self):
        """
        This method should be implemented by the child class.
        It should receive an observation and return an action.
        """
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        """
        This method allows the agent to reset its state.
        If not needed, just pass.
        """
        raise NotImplementedError

    def __str__(self):
        return self.name
