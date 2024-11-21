import gym
from stable_baselines3 import PPO

def reinforcement_learning_strategy(env_name):
    """
    Deep Reinforcement Learning Strategy using PPO.
    
    :param env_name: Name of the trading environment (e.g., 'TradingEnv-v0').
    :return: Trained RL model.
    """
    env = gym.make(env_name)
    
    # Initialize PPO model
    model = PPO("MlpPolicy", env, verbose=1)
    
    # Train the model
    model.learn(total_timesteps=10000)
    
    print("Reinforcement Learning Model Trained")
    return model
