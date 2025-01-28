"""
Objective: To apply McTaggart's A-series and B-series philosophical frameworks to stock market analysis, drawing parallels between temporal relationships and market dynamics. 
Inspired by McTaggart's "The Unreality of Time," this approach explores how market events can be categorized as sequences of "future, present, and past" (A-series) or 
as relationships of "earlier and later" (B-series). By integrating phenomenological and metaphysical insights, the project seeks to uncover whether stock market events exhibit properties of temporal change (A-series) 
or enduring relationships (B-series), and whether this duality can provide a novel perspective on market behavior.

A-series: 
This approach categorizes time into past, present, and future using a sliding window methodology. 
It reflects a dynamic perspective of time that evolves as events unfold. 
The analysis will focus on real-time stock price data over a specified duration
- Past: Utilize data from the previous month to train machine learning models, including Random Forest Regressor, 
        LSTM networks, ARIMA, XGBoost, and LightGBM.
- Present: Data with current prices used to make predictions.
- Future:  Employ the trained models to forecast future prices and compare these predictions with actual prices as time progresses.

B-series: This approach organizes time into "before" and "after" relationships, which are fixed and maintain a consistent order among events. 
The analysis will examine stock price movements surrounding significant corporate events.
- Calculate the average price before and after the event, determine the impact of the event and visualize the results.
"""
