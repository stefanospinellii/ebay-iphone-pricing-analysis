# ebay-iphone-pricing-analysis
Marketplace pricing and depreciation analysis on eBay iPhone datasets using Python (Pandas &amp; Seaborn) to model secondary market dynamics.
# 📱 E-Commerce Marketplace Pricing Analysis (eBay US iPhone Market)

## 📌 Project Overview
This project delivers a data-driven **Marketplace Analytics & Commercial Strategy** evaluation based on raw web-scraped data from eBay US, encompassing over 2,100 listings across multiple iPhone generations (`iPhone XR`, `11 Pro Max`, `12 Pro Max`, `13 Pro Max`, and `14 Pro Max`). 

The analysis explores the underlying economic forces of the consumer-to-consumer (C2C) secondary market. Specifically, it benchmarks secondary market performance against official retail anchor pricing to quantify **generational value retention, storage capacity premiums, color psychology, and title keyword sentiment.**

---

## 🛠️ Tech Stack & Methodology
* **Language:** Python 3.14
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Glob
* **Data Cleansing:** Standardized text inconsistencies, extracted storage sizes and colors using Regex/string mapping, handled multi-currency/range string prices, and implemented outlier-resistant median estimators to bypass marketplace noise.

> **Methodological Note on Data Timeline:**
> While the source files lacked explicit timestamps, cross-referencing the data with official Apple US launch prices places this dataset contextually around **November 2023**. The `iPhone 14 Pro Max` average price ($1,019.26) closely reflects its standard secondary market value immediately following the commercial release of the iPhone 15 series, ensuring historical data consistency.

---

## 📊 Core Business Insights & Strategic Marketplace Frameworks

### 1. Generational Value Retention & Depreciation Curves
* **The Insight:** By benchmarking secondary market prices against official Apple US retail launch prices ($1,099 for Pro Max series), we uncover a non-linear depreciation curve. The `iPhone 11 Pro Max` retains roughly **38%** of its original value after 4 years, whereas the `iPhone 14 Pro Max` experiences almost **0% median depreciation** relative to its base launch price ($1,019 secondary vs $1,099 launch). This proves a massive demand bottleneck for the latest generations in secondary channels, where consumer willingness-to-pay approaches retail ceilings due to immediate availability.
* **Strategic Application:** *Dynamic Inventory Liquidity.* Recommerce platforms can optimize seller velocity by predicting asset depreciation curves. Automated triggers can prompt users holding a device from two generations prior to re-price their listings by **15-20%** right at the launch of a new flagship, accelerating platform *Time-to-Sell* and preventing dead catalog stock.

### 2. Storage Premium Elasticity
* **The Insight:** Secondary market buyers display a high willingness-to-pay for higher storage tiers. The economic premium for 256GB and 512GB models does not decay linearly over time; instead, it maintains a consistent price delta across generations. Buyers actively choose to pay a premium for physical storage rather than dealing with hardware limitations.
* **Strategic Application:** *Feature-Based Smart Pricing Suggesters.* During the self-listing process, marketplaces should treat storage capacity as a mandatory structured variable to inject a standardized *price bump*. If a base 64GB device is valued at $500, the background algorithm should automatically recommend a ~$550 starting point for the 256GB variant, preventing private sellers from underpricing high-value assets and maximizing platform Gross Merchandise Volume (GMV).

### 3. Color Psychology & Outlier Management
* **The Insight:** Annual "Hero" colorways (such as the *Purple* on the 14 Pro Max or *Green* on the 11 Pro Max) maintain price equilibrium or slight premiums over standard *Black* and *White* variations. Furthermore, mean-based analysis showed heavy skewing from speculative pricing (e.g., individual listings at $2,500), validating that C2C platforms face heavy information asymmetry where uneducated private sellers post unrealistic prices.
* **Strategic Application:** *Outlier-Resistant Recommendation Engines.* Automated pricing tools and background valuation algorithms must utilize median-based estimators rather than simple averages to keep automated user recommendations grounded. Additionally, high-demand "Hero" colors can be prioritized in algorithmic recommendation feeds during low-liquidity periods to trigger impulse purchases.

### 4. Keyword Sentiment & Semantic Condition Impact
* **The Insight:** Semantic text inclusions like *"Cracked"*, *"Broken"*, or *"Parts"* depress the median resale value of the device by **50-60%**. Conversely, keywords like *"Mint"* or *"Sealed"* successfully command a premium. Unstructured text descriptions heavily compensate for missing or improperly selected structured condition fields.
* **Strategic Application:** *NLP-Driven Quality and Trust Controls.* Integrating real-time Natural Language Processing (NLP) during the listing creation phase can bridge the gap between user input and actual item state. If a seller inputs words implying hardware damage in the text title, the UI can dynamically adjust the structured item condition flag to "Damaged" or "Satisfactory," mitigating fraud, ensuring catalog integrity, and optimizing platform trust.

---

## 📁 Repository Structure
* 📄 `pricing_analysis.ipynb`: The complete Jupyter Notebook featuring data merging, cleaning pipelines, and data visualizations.
* 📊 `ebay_iphone_cleaned_dataset.csv`: The final, consolidated, and structured dataset ready for SQL/BI querying.
