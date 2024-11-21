import gym
from stable_baselines3 import PPO

def reinforcement_learning_trading(env_name, total_timesteps=10000):
    """
    Deep Reinforcement Learning for Trading.
    
    :param env_name: Name of the trading environment (e.g., 'TradingEnv-v0').
    :param total_timesteps: Number of training timesteps.
    :return: Trained RL model.
    """
    env = gym.make(env_name)
    
    # Initialize and train PPO model
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    
    print("Reinforcement Learning Model Trained")
    return model
