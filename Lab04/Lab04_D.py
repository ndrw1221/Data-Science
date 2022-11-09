import numpy as np
import matplotlib.pyplot as plt
import math
rng = np.random.default_rng()

def transition_matrix(n):
    '''Return the transition matrix for the following Markov chain, 
       given the number of states n as an argument. 

    If current state is 𝑖 and 𝑖 < n/2
        With probability 0.60, it goes to state 𝑖 = 𝑖 + 1
        With probability 0.35, it stays at state 𝑖
        With probability 0.05, it will fall back to state 𝑖 = 0
    If current state is 𝑖 and 𝑖 ≥ 𝑛/2
        With probability 0.50, it goes to state 𝑖 = 𝑖 + 1
        With probability 0.40, it will fall back to state 𝑖 = 𝑖 − 1
        With probability 0.10, it will fall back to state 𝑖 = 0
    If current state is 𝑖 and 𝑖 = 0
        Since it cannot get any lower, 
        it will stay at state 𝑖 = 0 with probability 0.40.
    If current state is 𝑖 and 𝑖 = 𝑛 − 1
        Since it cannot go higher, 
        it will stay at state 𝑖 = 𝑛 − 1 with probability 0.50.
    '''

    P = np.zeros(shape=(n,n), dtype=float)
    half = math.ceil(n/2)
    iuf = np.arange(0, half)  # indices under n/2
    iof = np.arange(half, n)  # indices over n/2
    
    # ranges for probability of 0.05
    P[iuf[1:], 0] = 0.05
    # ranges for probability of 0.10
    P[iof, 0] = 0.10
    # ranges for probability of 0.35
    P[iuf[1:], iuf[1:]] = 0.35
    # ranges for probability of 0.40
    P[0,0] = 0.40
    P[iof, iof-1] = 0.40
    # ranges for probability of 0.50
    P[n-1,n-1]=0.50
    P[iof[:-1], iof[:-1]+1] = 0.50
    # ranges for probability of 0.60
    P[iuf, iuf+1] = 0.60

    return P

def propagate(x0, P, k):
    '''Return the probibility distribution as a 1d array after k steps,
       given the initial distribution x0 and transition matrix P
    '''
    
    return x0 @ np.linalg.matrix_power(P,k)

def create_sample(s0, P, k):
    '''Return the trajectories of a sample evolution for k steps as a list,
       given the initial sample s0 and transition matrix P
    '''
    trajectories = []
    sample = s0
    steps = 0
    while steps <= k:
        trajectories.append(sample)
        sample = int(rng.choice(10, 1, p=P[sample]))
        steps += 1

    return trajectories

def plot_distribution(x):
    plt.plot(x)
    plt.xticks(np.arange(0, len(x), step=1))
    plt.ylim(0, max(x)+0.1)
    plt.xlabel('State (i)')
    plt.ylabel('Probability')
    plt.title('Probability Distribution')
    plt.savefig('Lab04_D3.png', dpi=150)
    plt.show()

def plot_histogram(x):
    plt.hist(x, bins=max(x)+1, range=(-0.5, max(x)+0.5))
    plt.xticks(np.arange(0, max(x)+1, step=1))
    plt.xlabel('State (i)')
    plt.ylabel('Number of smaple')
    plt.title('State Histogram')
    plt.savefig('Lab04_D7.png', dpi=150)
    plt.show()
    
def main():
    # TODO_D3
    P = transition_matrix(n=10)
    x0 = np.zeros(10)
    x0.put(0,1)
    x8 = propagate(x0, P, k=8)

    plot_distribution(x8)


    # TODO_D4
    step = 0
    x = np.zeros(10)

    print('Probability of being in state 9: ')
    while x[-1] < 0.01:
        step += 1
        x = propagate(x0, P, step)
        print(f'Propagation {step}: {x[-1]}')


    # TODO_D5
    rng = np.random.default_rng(12345)
    x0 = rng.random(10)
    x0 /= sum(x0)
    x8 = propagate(x0, P, k=8)

    plot_distribution(x8)


    # TODO_D7
    count = 0
    last_steps = []

    while count < 1000:
        sample = create_sample(s0=0, P=P, k=8)
        last_steps.append(sample[-1])
        count += 1

    plot_histogram(last_steps)

if __name__ == "__main__":
    main()