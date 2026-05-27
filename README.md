# eBay US iPhone Pricing Analysis

## Project Overview
This repository contains a data analysis project tracking resale prices and market trends for used iPhones on eBay US. The dataset covers over 2,100 listings across five generations: iPhone XR, 11 Pro Max, 12 Pro Max, 13 Pro Max, and 14 Pro Max.

The goal is to analyze how hardware factors (storage, condition, color) and market age affect secondary market value compared to original Apple retail pricing.

---

## Tech Stack & Methodology
* **Stack:** Python (Pandas, NumPy, Matplotlib, Seaborn)
* **Data Prep:** Cleaned multi-currency listings, handled price ranges, and extracted storage capacities and color names from unstructured titles using Regex. 
* **Data Timeline Note:** Based on Apple retail benchmarks and data distributions (e.g., median iPhone 14 Pro Max at $1,019), this dataset represents market conditions around November 2023, shortly after the iPhone 15 launch.

---

## Key Findings

### 1. Value Depreciation Curves
* Older models follow a standard depreciation curve, with the iPhone 11 Pro Max holding about 38% of its original value after 4 years.
* The latest flagship (iPhone 14 Pro Max) shows a flat median depreciation curve (~$1,019 secondary vs. $1,099 original retail). Near-retail pricing suggests high immediate demand and low supply elasticity for the latest models on secondary channels.

### 2. Storage Price Premiums
* Buyers pay a consistent premium for higher storage capacities (256GB/512GB). This price delta remains stable across different generations, showing that physical storage capacity retains a rigid value premium even as the base device depreciates.

### 3. "Hero" Colors & Pricing Noise
* Apple's annual flagship colors (e.g., Midnight Green for the 11 Pro Max, Deep Purple for the 14 Pro Max) command a slight pricing premium or tighter price stability over basic black and white models.
* The raw dataset contains severe pricing outliers (e.g., optimistic sellers listing devices at $2,500). Using median-based metrics instead of averages is mandatory to avoid heavily skewed valuations.

### 4. Keyword Impact on Value
* Unstructured title keywords heavily dictate price. Text flags indicating damage ("cracked", "broken", "parts") drop the median market value by 50% to 60%. Conversely, standard condition keywords like "mint" or "sealed" successfully pull price premiums.

---

## Repository Structure
* `pricing_analysis.ipynb`: Data cleaning pipeline, processing logic, and exploratory data visualizations.
* `ebay_iphone_cleaned_dataset.csv`: The final, processed dataset used for the analysis.
