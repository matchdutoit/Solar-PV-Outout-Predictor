# Solar Photovoltaic Plant Energy Output Predictor
### Introduction
The goal for this project is to use regression modeling to predict the energy output of solar photovoltaic plants in California. More specifically, I wanted to analyze the effectiveness of using a purely statistical model to predict energy output of California.
#### 
My work on this project was performed in consultation with kWh Analytics. It was motivated by a problem experienced in renewable energy project financing, specifically solar project financing. The cost of capital is the biggest single cost of a solar power plant, however, investors are often unable to fully leverage solar projects because banks still consider solar assets “risky”. This forces investors to commit more equity (expensive capital) rather than debt (cheap capital), ultimately making solar projects less attractive and more expensive compared to traditional revenue-generating asset classes.
#### 
To de-risk these solar projects, we would like to use data from existing projects to accurately predict their solar energy output, which can then be used to predict project revenue when project specific rates are applied. For this project, we will focus primarily on the former task, predicting solar energy output for solar photovoltaic projects.

### Data Gathering
The data used for this project was originally sourced from the California Solar Initiative (CSI) incentive program (system production/metadata) and the NASA POWER project (weather/environmental data). The CSI data was provided by kWh Analytics and included Koeppen-Geiger climate types for each system as well. The NASA data was collected via their API.

### Modeling Energy Output
I used three regression models to predict energy output: Linear, Elastic Net, and Random Forest. I used a purely biased prediction, the mean output, to establish a baseline. I used a Linear Regression model first. Then I increased the complexity of the model by introducing regularizition terms to the cost function with Elastic Net. Finally, I used a Random Forest regressor.

### Results & Conclusions
Of the three models, Random Forest produced the lowest mean absolute error. Random Forest performed well given the mix of categorical data and numerical data. Unsurprisingly, system capacity dominated in terms of feature importance, reinforcing the notion that capacity is an impressive predictor on its own. Roof mount (fixed), surface pressure, and temperature were the next largest feature importances. 

### Further Work
I would like to continue feature engineering, focusing on the NASA data, to improve my model. Additionally, I plan on building a model on a seasonal timescale to account for weather variations throughout the year. A website using Flask Server and JS is in progress.
