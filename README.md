# Historical Data Analysis Over The Last 14 Years  

## Project Overview  
Bitcoin, as a digital currency, has emerged as one of the most popular and volatile investment assets. Its market attracts both investors and speculators, making it a critical subject for financial analysis.  
The purpose of this project is to investigate the volatility and risk associated with Bitcoin by analyzing market data over a span of several years.  

## Dataset Description  
The final dataset is a merged collection of two sources:  
- **Historical Bitcoin prices** (from the CryptoCompare API)  
- **Additional data** sourced from [Kaggle](https://www.kaggle.com/datasets/shiivvvaam/bitcoin-historical-data)  

## Hypotheses Tested  

1. **Bitcoin's average closing price is higher in specific seasons.**  
   ![Bitcoin Seasonal Prices](<Screenshot 2025-02-11 at 14.31.57.png>)  

2. **Bitcoin is more volatile during weekdays compared to weekends.**  
   ![Bitcoin Weekday Volatility](<Screenshot 2025-02-11 at 14.32.48.png>)  

3. **There is a significant correlation between trading volume and both price movements and volatility.**  
   ![Trading Volume vs. Volatility](<Screenshot 2025-02-11 at 14.33.24-1.png>)  

## Data Cleaning Process  
Several steps were taken to prepare the dataset for analysis:  
- **Date formatting:** Aligned date formats and extracted useful time features (year, season, weekday/weekend).  
- **Handling missing data:** Addressed gaps in trading volume and other missing values.  
- **Data consistency:** Ensured accurate merging of data across both sources while maintaining consistent formatting.  

## Analysis Approach  
- **Exploratory Data Analysis (EDA):** Explored the distribution of prices, trading volumes, and seasonal trends.  
- **Correlation Analysis:** Investigated relationships between trading volume, price movements, and volatility.  
- **Trend Analysis:** Examined Bitcoin price trends over the years, identifying notable spikes and dips during specific periods.  

## Results  

- **Hypothesis 1:** Bitcoin prices were found to be higher during **spring** compared to other seasons.  
- **Hypothesis 2:** **Weekdays** showed higher volatility compared to weekends.  
- **Hypothesis 3:** No significant correlation was found between trading volume and price movements or volatility.  

A high standard deviation in volatility suggests that Bitcoin experiences large swings in daily price, reinforcing its reputation as a **risky asset**. A volatile market is unpredictable and can lead to sudden price shifts.  

These findings provide valuable insights into Bitcoin's inherent volatility and its limited correlation with trading volume, helping investors assess the associated risks.  

---

📌 **Technologies Used:**  
- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- CryptoCompare API  
- Kaggle Dataset  

🚀 **Future Improvements:**  
- Investigate additional macroeconomic factors affecting Bitcoin prices.  
- Analyze the impact of major news events on Bitcoin volatility.  
- Explore deep learning models for enhanced predictive insights.  
