import numpy as np
import matplotlib.pyplot as plt
import imageio

# Parameters
true_mean = 5  # True parameter we are estimating
sample_size = 30  # Sample size per experiment
num_experiments = 50  # Number of experiments

# Generate samples and compute estimates
estimates = []
for _ in range(num_experiments):
    sample = np.random.normal(loc=true_mean, scale=2, size=sample_size)
    estimate = np.mean(sample)
    estimates.append(estimate)

# Create frames for the GIF
frames = []
fig, ax = plt.subplots(figsize=(6, 4))
for i in range(1, num_experiments + 1):
    ax.clear()
    ax.hist(estimates[:i], bins=10, alpha=0.6, color='b', edgecolor='black')
    ax.axvline(true_mean, color='red', linestyle='--', label='True Mean')
    ax.set_xlim(true_mean - 2, true_mean + 2)
    ax.set_ylim(0, num_experiments // 4)
    ax.set_title(f"Unbiased Estimation (n={i})")
    ax.set_xlabel("Estimated Mean")
    ax.set_ylabel("Frequency")
    ax.legend()
    
    # Save frame
    frame_path = f"/mnt/data/frame_{i}.png"
    plt.savefig(frame_path)
    frames.append(imageio.imread(frame_path))

# Save as GIF
gif_path = "/mnt/data/unbiased_estimator.gif"
imageio.mimsave(gif_path, frames, duration=0.2)

# Show GIF path
gif_path
