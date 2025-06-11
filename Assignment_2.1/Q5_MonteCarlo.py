import numpy as np

def monte_carlo_simulation(num_steps=2160, target_ticks=1000, p_up=0.10, p_same=0.85, p_down=0.05, trials=10000):
    outcomes = []
    for _ in range(trials):
        # increments: +1, 0, -1 with given probabilities
        increments = np.random.choice([1, 0, -1], size=num_steps, p=[p_up, p_same, p_down])
        # Cumulative sum gives position in ticks
        positions = increments.cumsum()
        # if target is ever reached
        outcomes.append(np.any(positions >= target_ticks))
    
    # probability
    return np.mean(outcomes)

estimated_prob = monte_carlo_simulation()
print(f"Estimated probability of hitting +1000 ticks in 2160 steps: {estimated_prob:.5f}")
