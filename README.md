# Cryptocurrency Price Analysis
## Project Overview
This project focuses on analyzing cryptocurrency market data (Bitcoin and other major coins) to identify trends, volatility, and trading patterns.  
The main goal is to clean and explore the dataset, create visualizations for better insights, and lay the foundation for predictive modeling of crypto prices.  
## Problem Statement
Cryptocurrency prices are highly volatile, making it difficult for investors to understand price patterns and make informed decisions.  
This project aims to answer questions like:  
- How do crypto prices change over time?  
- What relationships exist between Volume, Marketcap, and Price?  
- Can we identify patterns that might be useful for predicting future prices?  
## Dataset Information
- **Source**: Kaggle – Cryptocurrency Historical Data  
- **Type**: Tabular dataset  
- **Size**: ~10,000+ rows with daily price and market data  
- **Columns**:  
  - `Date`: Trading date  
  - `Open`, `High`, `Low`, `Close`: Price values  
  - `Volume`: Trading volume  
  - `Marketcap`: Total market capitalization  
  - `Name`, `Symbol`: Cryptocurrency details  
## Methodology / Approach
### 1. Data Preprocessing
- Handled missing values and duplicates  
- Converted `Date` column into datetime format  
- Removed irrelevant columns for correlation analysis (`Name`, `Symbol`)  
### 2. Exploratory Data Analysis (EDA)
- Trend analysis using line charts and candlestick charts  
- Distribution of prices using boxplots  
- Scatter plots for Volume vs Marketcap  
- Correlation heatmap for numerical variables  
### 3. Visualization
- **Matplotlib & Seaborn** → Line plots, heatmaps, scatter plots  
- **Plotly** → Interactive candlestick chart for crypto price movement  
### 4. (Planned) Modeling
- Use regression models (Linear Regression, Random Forest) to predict `High` price values  
- Evaluate performance with RMSE, MAE, and R² score  
## 🔹 Key Results / Findings
- Strong correlation found between `Volume` and `Marketcap`  
- Prices show high volatility with sharp upward and downward spikes  
- Hong Kong-like markets (from earlier Amazon dataset example) → here, crypto analysis shows **Bitcoin dominates trading volume compared to altcoins**  
- Interactive candlestick visualization makes it easier to analyze daily market fluctuations  
## 🔹 Technologies / Tools Used
- **Languages**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Plotly  
- **Tools**: VS Code, GitHub  
## 🔹 How to Run / Reproduce
1. Clone this repository  
   ```bash
   git clone https://github.com/your-username/crypto-price-analysis.git
