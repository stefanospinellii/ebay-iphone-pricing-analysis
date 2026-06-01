# iPhone Pricing Recommendation Engine

Live Demo: https://ebay-iphone-pricing-analysis-hefbg7u969edukpd7hfswg.streamlit.app/

## Overview

A simple pricing tool that estimates realistic listing prices for used iPhones based on historical eBay data.

Users select:

* Model
* Storage
* Condition
* Carrier Status

The application then suggests:

* Bargain Price
* Fair Price
* Premium Price

## Dataset

Historical eBay listing data collected in November 2023.

Models included:

* iPhone XR
* iPhone 11 Pro Max
* iPhone 12 Pro Max
* iPhone 13 Pro Max
* iPhone 14 Pro Max

After cleaning and preprocessing, the final dataset contained 843 listings.

## Methodology

Information extracted from listing titles:

* Model
* Storage Capacity
* Condition
* Carrier Status

A Random Forest Regressor was trained to estimate market value.

Performance:

```text
R² = 0.58
```

Price recommendations are generated using comparable listings:

* Bargain Price → 20th percentile
* Fair Price → Median price
* Premium Price → 80th percentile

When insufficient comparable listings are available (within ±10% of the predicted price), the model prediction is used as a fallback.

## Example

```text
PRICE RECOMMENDATION
--------------------

Device: 14 PRO MAX 256GB | EXCELLENT | UNLOCKED

Bargain: $895
Fair:    $900
Premium: $1007
```

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit

## Key Takeaway

Comparable listings often provide more interpretable pricing recommendations than machine learning predictions alone. This project combines both approaches to estimate realistic marketplace prices for used iPhones.
