import agent
import gym

## Chương trình chính
# Khởi tạo môi trường
env = gym.make("CartPole-v1")
state, _ = env.reset()

# Định nghĩa state_size và action_size
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

# Định nghĩa tham số khác
n_episodes = int(input("Nhập episodes (vui lòng nhập số nguyên dương): "))
n_timesteps = int(input("Nhập time steps (vui lòng nhập số nguyên dương): "))
batch_size = int(input("Nhập batch size (vd: 64, 512 , ...): "))

# Khởi tạo Agent
my_agent = agent.MyAgent(state_size=state_size, action_size=action_size)
total_time_step = 0

for ep in range(n_episodes):
    ep_rewards = 0
    state, _ = env.reset()

    for t in range(n_timesteps):
        total_time_step += 1
        # Cập nhật lại target NN mỗi my_agent.update_target_nn_rate
        if total_time_step % my_agent.update_target_nn_rate == 0:
            # Có thể chọn cách khác: weight của targetnetwork = 0.9 * weight của targetnetwork + 0.1 * weight của mainnetwork
            my_agent.target_network.set_weights(my_agent.main_network.get_weights())

        action = my_agent.make_decision(state)
        next_state, reward, terminal, _, _ = env.step(action=action)
        my_agent.save_experience(state=state, action=action, reward=reward, next_state=next_state, terminal=terminal)

        state = next_state
        ep_rewards += reward

        if terminal:
            print("Ep ", ep+1, " reach terminal with reward = ", ep_rewards)
            break

        if len(my_agent.replay_buffer) > batch_size:
            my_agent.train_main_network(batch_size=batch_size)
    
    if my_agent.epsilon > my_agent.epsilon_min:
        my_agent.epsilon = my_agent.epsilon * my_agent.epsilon_decay

# Save weights
my_agent.main_network.save("train_agent.h5")