
import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human")

print(f"Action Space: {env.action_space}")
print(f"Observation Space: {env.observation_space}")

observation, info = env.reset()

terminated = False
truncated = False
total_reward = 0.0

while not terminated and not truncated:

    env.render()

    action = env.action_space.sample()
    print(f"Taking action: {action} (0:L,1:R,)")


    next_observation, reward, terminated, truncated, info = env.step(action)


    total_reward += reward
    observation = next_observation


    time.sleep(1)

print(f"\nEpisode finished! Total Reward: {total_reward}")
env.close()


# What type of space is the action space? How many actions are there?
# The action space is Discrete(2).Discrete means the agent can only pick from a finite number of choices.
# In this case, there are two actions:
# 0=Push the cart to the left
# 1= Push the cart to the right

# What type of space is the observation space? The output is Box(4,). This represents a continuous space with 4 numbers. Based on the problem, what could these four numbers possibly represent?
# The observation space is Box(4,).
# Box means the values are continuous (real numbers), not discrete categories.
# (4,) means there are four numbers in the state description.
# These four numbers represent the state of the system:
# Cart Position (x) = Where the cart is on the track (left/right).
# Cart Velocity (ẋ) = How fast the cart is moving.
# Pole Angle (θ) = The angle of the pole relative to vertical.
# Pole Angular Velocity (θ̇) = How fast the pole is falling/rotating.

# Run the random agent for one episode. What does the reward seem to represent in this environment? (Hint: you get a reward for every step the pole remains balanced).
# The reward in CartPole is very simple:
# +1 for every timestep the pole stays upright.
# No extra bonuses or penalties.
# If the pole falls down or the cart goes out of bounds, the episode terminates, and the agent stops earning rewards.