# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Initialize known parameters
# EBITDA for last year
initial_EBITDA = 100
# Expected annual growth rate for EBITDA
EBITDA_growth_mean = 0.02  
# Standard deviation of EBITDA growth rate
EBITDA_growth_std_dev = 0.06  
# Expected annual interest rate
interest_rate = 0.05
# Standard deviation of interest rate
interest_std_dev = 0.05
# Number of Monte Carlo simulations
num_simulations = 10000
# Number of years to simulate
num_years = 10
# Debt levels to examine (from $500 to $1000 in increments of $50)
debt_levels = np.arange(500, 1000, 50)

# Dictionary to store results: Probability of distress for each debt level
prob_of_distress = {}

# Perform simulations for each debt level
for debt in debt_levels:
    # Counter to keep track of distress events
    distress_count = 0
    
    # Run 100 simulations for each debt level
    for sim in range(num_simulations):
        # Initialize EBITDA and interest for each simulation
        EBITDA = initial_EBITDA
        interest = debt * interest_rate
        # Flag to mark distress event
        in_distress = False
        
        # Simulate for 10 years
        for year in range(num_years):
            # Randomly simulate EBITDA growth using normal distribution
            EBITDA *= np.exp(np.random.normal(EBITDA_growth_mean, EBITDA_growth_std_dev))
            # Randomly simulate interest rate change using normal distribution
            interest *= np.exp(np.random.normal(0, interest_std_dev))
            # Calculate interest coverage ratio
            interest_coverage_ratio = EBITDA / interest
            
            # Check if the firm falls into distress
            if interest_coverage_ratio < 2:
                in_distress = True
                break
                
        # Increment distress count if firm is in distress
        if in_distress:
            distress_count += 1
            
    # Calculate probability of distress for this debt level
    prob_of_distress[debt] = distress_count / num_simulations

# Print probability of distress for each debt level
for debt, prob in prob_of_distress.items():
    print(f"Debt: ${debt}, Probability of Distress: {prob * 100}%")

# Plotting the results
# Set up the figure size and style
plt.figure(figsize=(12, 8))
# Create a bar plot for the probability of distress against debt levels
plt.bar(list(prob_of_distress.keys()), list(prob_of_distress.values()), width=40, color='blue', alpha=0.7, label='Probability of Distress')
# Label the x-axis
plt.xlabel('Debt Level ($)', fontsize=14)
# Label the y-axis
plt.ylabel('Probability of Distress', fontsize=14)
# Add a title
plt.title('Probability of Distress for Different Debt Levels', fontsize=16)
# Format tick labels
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
# Add a legend to explain the bar colors
plt.legend(fontsize=12)
# Show the plot
plt.show()
