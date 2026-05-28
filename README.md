# Python eBay iPhone Resale — Price Analysis

## Why this project

I wanted to understand how second-hand markets actually price things. iPhones are a good test case: everyone knows the retail price, so you can measure real depreciation instead of guessing it.

The dataset has 2,172 eBay US listings across five generations (XR through 14 Pro Max). I cleaned it, explored it, and tried to answer one core question: what actually drives resale price?

## What I found

**Depreciation isn't linear.** The 11 Pro Max holds about 38% of its original value after 4 years — but the 14 Pro Max was still selling near retail ($1,019 vs $1,099 original). High demand, low supply right after the iPhone 15 launch.

**Storage premiums are sticky.** People consistently pay more for 256GB/512GB — and that delta barely moves as the device ages.

**Condition keywords do exactly what you'd expect.** Listings with "cracked" or "broken" drop median price by 50-60%. "Mint" or "sealed" pull it back up. The title is basically a pricing signal.

**Outliers are everywhere.** Some sellers list at $2,500. Median beats average here, always.

## Stack

Python — pandas, seaborn, matplotlib, regex for parsing unstructured titles
