# from kaggle_environments import make

# # Initialize chess environment
# env = make("chess", debug=True)

# # Run a game between your bot and a random bot
# result = env.run(["main.v3.py", "random"])

# # Display results
# print("Agent exit status/reward/time left: ")

# for agent in result[-1]:
#     print("\t", agent.status, "/", agent.reward, "/", agent.observation.remainingOverageTime)





import numpy as np
from kaggle_environments import make

def run_multiple_tests(num_tests=10):
    rewards = []  # Store rewards for each test
    
    # Loop to run the bot multiple times
    for _ in range(num_tests):
        # Initialize chess environment
        env = make("chess", debug=True)

        # Run a game between your bot (main.py) and a random bot
        result = env.run(["main.py", "random"])

        # Extract the reward for your bot (first agent in the list)
        agent_status = result[-1][0].status
        agent_reward = result[-1][0].reward
        rewards.append(agent_reward)  # Save the reward to the list
        
        # Optionally: You can print the results for each test
        print(f"Game {_ + 1}: Status: {agent_status}, Reward: {agent_reward}")

    # Calculate the average reward
    average_reward = np.mean(rewards)
    return average_reward

# Run the tests and get the average result
average_result = run_multiple_tests(10)
average_result