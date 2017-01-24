# Input: List of transactions, number of transactions
# Output: List of returns, percentage of returns
# Provides return information.
def get(transactions, no_transactions):
	returns = transactions[transactions.quantity == -1]
	no_returns = len(returns)
	print("Amount of returns: " + str(no_returns))
	print("Percentage of returns: " + str(no_returns/no_transactions * 100) + "\n")
	return returns, no_returns