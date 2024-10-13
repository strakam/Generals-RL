from typing import Any, SupportsFloat

import gymnasium as gym
from copy import deepcopy

from generals.agents import Agent
from generals.core.game import Action, Game, Info, Observation
from generals.core.grid import GridFactory
from generals.core.replay import Replay
from generals.agents import Agent, AgentFactory
from generals.gui import GUI
from generals.gui.properties import GuiMode

from generals.envs.env import Reward, RewardFn


class GymnasiumGenerals(gym.Env):
    metadata = {
        "render_modes": ["human"],
        "render_fps": 6,
    }

    def __init__(
        self,
        grid_factory: GridFactory | None = None,
        npc: Agent | None = None,
        reward_fn: RewardFn | None = None,
        render_mode: str | None = None,
        agent_id: str = "Agent",
        agent_color: tuple[int, int, int] = (67, 70, 86),
    ):
        self.render_mode = render_mode
        self.grid_factory = grid_factory if grid_factory is not None else GridFactory()
        if reward_fn is not None:
            self.reward_fn = reward_fn
        else:
            self.reward_fn = GymnasiumGenerals._default_reward

        # Agents
        if npc is None:
            print('No NPC agent provided. Creating "Random" NPC as a fallback.')
            npc = AgentFactory.make_agent("random")
        self.npc = npc
        self.agent_id = agent_id
        self.agent_ids = [self.agent_id, self.npc.id]
        self.agent_data = {
            agent_id: {"color": agent_color},
            self.npc.id: {"color": self.npc.color},
        }
        assert agent_id != npc.id, "Agent ids must be unique - you can pass custom ids to agent constructors."

        # Game
        grid = self.grid_factory.grid_from_generator()
        self.game = Game(grid, [self.agent_id, self.npc.id])
        self.observation_space = self.game.observation_space
        self.action_space = self.game.action_space

    def render(self):
        if self.render_mode == "human":
            _ = self.gui.tick(fps=self.metadata["render_fps"])

    def reset(
        self, seed: int | None = None, options: dict[str, Any] | None = None
    ) -> tuple[Observation, dict[str, Any]]:
        super().reset(seed=seed)
        if options is None:
            options = {}
        if "grid" in options:
            grid = self.grid_factory.grid_from_string(options["grid"])
        else:
            map_seed = self.np_random.integers(0, 2**20)
            grid = self.grid_factory.grid_from_generator(seed=map_seed)

        self.game = Game(grid, self.agent_ids)

        if self.render_mode == "human":
            self.gui = GUI(self.game, self.agent_data, GuiMode.TRAIN)

        if "replay_file" in options:
            self.replay = Replay(
                name=options["replay_file"],
                grid=grid,
                agent_data=self.agent_data,
            )
            self.replay.add_state(deepcopy(self.game.channels))
        elif hasattr(self, "replay"):
            del self.replay

        self.observation_space = self.game.observation_space
        self.action_space = self.game.action_space

        observation = self.game.agent_observation(self.agent_id)
        info: dict[str, Any] = {}
        return observation, info

    def step(self, action: Action) -> tuple[Observation, SupportsFloat, bool, bool, dict[str, Any]]:
        # Get action of NPC
        npc_action = self.npc.act(self.game.agent_observation(self.npc.id))
        actions = {self.agent_id: action, self.npc.id: npc_action}

        observations, infos = self.game.step(actions)
        obs = observations[self.agent_id]
        info = infos[self.agent_id]
        reward = self.reward_fn(obs, action, self.game.is_done(), info)
        terminated = self.game.is_done()
        truncated = False if self.game.time < 120 else True  # Choose your constant

        if hasattr(self, "replay"):
            self.replay.add_state(deepcopy(self.game.channels))

        if terminated:
            if hasattr(self, "replay"):
                self.replay.store()
        return obs, reward, terminated, truncated, info

    @staticmethod
    def _default_reward(
        observation: dict[str, Observation],
        action: Action,
        done: bool,
        info: Info,
    ) -> Reward:
        """
        Give 0 if game still running, otherwise 1 for winner and -1 for loser.
        """
        if done:
            reward = 1 if observation["observation"]["is_winner"] else -1
        else:
            reward = 0
        return reward

    def close(self) -> None:
        if self.render_mode == "human":
            self.gui.close()
