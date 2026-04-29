import numpy as np

def monte_carlo_option_price(S0, K, T, r, sigma, n_sim=100000, option_type='call'):
    """
    Monte Carlo simulation for European option pricing
    S0: initial stock price
    K: strike price
    T: time to maturity (years)
    r: risk-free rate
    sigma: volatility
    n_sim: number of simulations
    option_type: 'call' or 'put'
    """
    # Simulate end-of-period stock prices
    Z = np.random.standard_normal(n_sim)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    # Compute payoff
    if option_type == 'call':
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)
    
    # Discount to present value
    option_price = np.exp(-r * T) * np.mean(payoff)
    return option_price

# Example usage
S0 = 100       # current stock price
K = 105        # strike price
T = 1          # 1 year
r = 0.05       # 5% risk-free
sigma = 0.2    # 20% volatility

price = monte_carlo_option_price(S0, K, T, r, sigma, option_type='call')
print(f"Estimated Call Option Price: {price:.2f}")