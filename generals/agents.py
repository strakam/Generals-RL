import numpy as np

from generals.config import DIRECTIONS


class Agent:
    """
    Base class for all agents.
    """

    def __init__(self, name):
        self.name = name

    def play(self):
        """
        This method should be implemented by the child class.
        It should receive an observation and return an action.
        """
        raise NotImplementedError

    def __str__(self):
        return self.name


class RandomAgent(Agent):
    def __init__(self, name, idle_prob=0.1, split_prob=0.25):
        super().__init__(name)

        self.idle_probability = idle_prob
        self.split_probability = split_prob

    def play(self, observation):
        """
        Randomly selects a valid action.
        """
        pass_turn = [0] if np.random.rand() > self.idle_probability else [1]
        split_army = [0] if np.random.rand() > self.split_probability else [1]

        mask = observation["action_mask"]
        valid_actions = np.argwhere(mask == 1)

        if len(valid_actions) == 0: # No valid actions
            return np.array([1, 0, 0, 0, 0])

        action_index = np.random.choice(len(valid_actions))

        action = np.concatenate((pass_turn, valid_actions[action_index], split_army))
        return action


class ExpanderAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

    def play(self, observation):
        """
        Heuristically selects a valid (expanding) action.
        Prioritizes capturing opponent and then neutral cells.
        """
        mask = observation["action_mask"]
        army = observation["army"]

        valid_actions = np.argwhere(
            mask == 1
        )  # List of [row, col, direction] indices of valid actions

        if np.sum(mask) == 0:
            return np.array([1, 0, 0, 0, 0])  # IDLE move

        opponent = observation["opponent_cells"]
        neutral = observation["neutral_cells"]

        # Find actions that capture opponent or neutral cells
        actions_to_opponent = np.zeros(len(valid_actions))
        actions_to_neutral = np.zeros(len(valid_actions))
        for i, action in enumerate(valid_actions):
            di, dj = action[:-1] + DIRECTIONS[action[-1]] # Destination cell indices
            if army[action[0], action[1]] <= army[di, dj] + 1: # Can't capture
                continue
            elif opponent[di, dj]:
                actions_to_opponent[i] = 1
            if neutral[di, dj]:
                actions_to_neutral[i] = 1

        if np.any(actions_to_opponent): # If possible, capture random opponent cell
            action_index = np.random.choice(np.nonzero(actions_to_opponent)[0])
            action = valid_actions[action_index]
        elif np.any(actions_to_neutral): # If possible, capture random neutral cell
            action_index = np.random.choice(np.nonzero(actions_to_neutral)[0])
            action = valid_actions[action_index]
        else: # Otherwise, move randomly
            action_index = np.random.choice(len(valid_actions))
            action = valid_actions[action_index]

        # [0] to indicate we want to move, [0] to indicate we want to move all troops
        action = np.concatenate(([0], action, [0]))

        return action
