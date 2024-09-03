# financial-news-analysis
## Overview
This project involves a comprehensive analysis of financial news data to uncover potential correlations between news sentiment and stock market movements. The goal is to leverage Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE) techniques to explore how financial news influences market behavior. 
# Getting Started
## 1. Repository and Branch Setup
1. **Create a GitHub Repository:**

Create a new repository on GitHub named `financial-news-analysis`.

Clone the repository to your local machine:
```bash
git clone https://github.com/olaniSiyum/financial-news-analysis.git
```
2. **Create a New Branch**
Create and switch to a new branch named `task-1`
```bash
git checkout -b task-1
```
3. **Set Up Version Control:**
Ensure `.gitignore` is properly configured to exclude unnecessary files (virtual environment files, data).
```bash
echo "venv/" >> .gitignore
```
## 2. Development Environment Setup
1. **Create a Virtual Environment:**
Set up a virtual environment to manage dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
2. **Install Dependencies:**
Create a `requirements.txt` file listing necessary packages(like pandas
matplotlib seaborn nltk pytest numpy)
```bash
pip freeze > requirements.txt
```
## 3. Initial Exploratory Data Analysis (EDA)
**Publisher Activity:** Count the number of articles per publisher.
![Publication Trends Over Time](https://github.com/olaniSiyum/financial-news-analysis/blob/main/src/image/number_of_publication.png)

**Sentiment Analysis:**
![Sentiment Distribution](https://github.com/olaniSiyum/financial-news-analysis/blob/main/src/image/Sentiment.png)
**Topic Modeling:**
![Top 10 Common Keywords in Headlines](https://github.com/olaniSiyum/financial-news-analysis/blob/main/src/image/top10Headlines.png)
![Word Cloud of Headlines](https://github.com/olaniSiyum/financial-news-analysis/blob/main/src/image/wordcloud.png)
## 4. Correlation between News and Stock Movement
**Normalize Dates**
. Align dates in both the analyst_ratings (news) and stock datasets to ensure that each news
item corresponds to the correct trading day.
. If necessary, convert the news date column to match the format and timezone of the stock price data.
**Compute Daily Returns:**
Calculate the daily percentage changes in stock prices to represent stock movements.
**Aggregate Daily Sentiment**
If multiple articles appear on the same day, calculate the average sentiment score for that day.
**Calculate Correlation:**
Merge the daily sentiment scores with the stock daily returns.
Determine the Pearson correlation coefficient between the average daily sentiment scores and stock daily returns.
