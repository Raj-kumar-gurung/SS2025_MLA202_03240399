Name:Raj Kumar Gurung
Student_no:03240399

Summary of Tasks

In this practical, I worked with two classic reinforcement learning environments using Gymnasium:

Exercise 1: I explored the CartPole-v1 environment, inspecting the action space and observation space, and interpreting what the observation values mean.

Exercise 2: I implemented and ran a random agent in the FrozenLake-v1 environment for 1,000 episodes, recording the total rewards and calculating the average performance.

I also set up and used a Python virtual environment, which allowed me to install required packages (like gymnasium) in an isolated workspace.

Exercise 1: CartPole Action and Observation Spaces

Action Space:
The action space is Discrete(2). This means there are two possible actions available to the agent:

0 = move cart left

1 = move cart right

Observation Space:
The observation space is Box(4,), which means it is a continuous 4-dimensional vector. These four numbers represent:

Cart position

Cart velocity

Pole angle

Pole angular velocity

These values together describe the physical state of the cart-pole system at any given time.

Exercise 2: FrozenLake Random Agent Performance

I ran the FrozenLake-v1 environment for 1,000 episodes using a random agent.

The reward in FrozenLake is +1 if the agent reaches the goal and 0 otherwise.

Since the agent takes random actions, the performance is usually poor.
![alt text](<Screenshot 2025-09-05 184848.png>)

Challenges

The most difficult parts of this practical were:

Understanding the step() return values (observation, reward, terminated, truncated, info).

Structuring the loop correctly so that rewards were tracked per episode and the simulation stopped at the right time.

Interpreting FrozenLake’s results, since the random agent almost always fails due to the slippery dynamics.

Setting up the environment and dependencies, especially learning how to properly use a virtual environment to avoid version conflicts with libraries.

Key Takeaways

In CartPole, the action space is simple (left/right), but the observation space captures continuous physics, showing how reinforcement learning relies on state information.

In FrozenLake, sparse rewards make it hard for random agents, demonstrating why learning algorithms are needed.

I learned how important reward design is, since even simple reward rules define the difficulty of the task.

I gained practical skills in creating and managing virtual environments in Python, which is essential for keeping projects organized and preventing dependency issues.
