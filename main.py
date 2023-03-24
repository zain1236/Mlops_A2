# Import necessary libraries
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Define the ticker symbol of the stock you want to train the model on
ticker = 'AAPL'

# Define the period of time for which you want to download the live data
period = '12mo'

# Download the live data using yfinance
stock_data = yf.download(ticker, period=period)

# Split the live data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(stock_data.drop('Close', axis=1),
                                                    stock_data['Close'],
                                                    test_size=0.3,
                                                    random_state=42)

# Initialize a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict the target variable for the testing set
y_pred = model.predict(X_test)

# Evaluate the model's performance using a suitable metric
score = model.score(X_test, y_test)

# Print the score
print(f"Model score: {score}")