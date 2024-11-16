# CVM Algorithm Repository

This was the first large-scale project that I completed. It was based off [this video](https://www.youtube.com/watch?v=MZI3aL1igP8&t=158s) that piqued my interest. This project ballooned quickly, but I am happy to have completed it.

**The following is a README generated from my notes, using ChatGPT**

The CMV algorithm is an algorithm that counts unique values while favoring memory efficiency and computation speed over absolute accuracy. The CVM algorithm scales with the Law of Large Numbers, making it efficient for large datasets.

## Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Findings](#findings)
- [References](#references)

## Introduction

Counting unique values in large datasets can be resource-intensive and slow using traditional methods. The CVM algorithm provides an approximate count of unique values while significantly reducing memory usage and computation time. This trade-off between accuracy and efficiency makes it suitable for big data applications where absolute precision is less critical.

## How It Works

The CVM algorithm operates by:

1. **Probability Sampling**: Instead of storing all unique values, it stores them based on a probability factor. This reduces the memory footprint.
2. **Dynamic Probability Adjustment**: When memory limits are reached, the algorithm adjusts the probability factor to further reduce stored values.
3. **Estimation**: The final count of unique values is estimated by dividing the number of stored values by the probability factor.

## Findings

### 1. Resource Reduction

- **Observation**: The CVM algorithm reduces required resources exponentially compared to traditional methods.
- **Conclusion**: Confirmed that CVM uses significantly less memory, making it suitable for large datasets.

### 2. Execution Time Improvement

- **Observation**: Execution times are reduced but reach a ceiling quickly.
- **Conclusion**: While faster than naive methods, a bug or limitation causes execution time to plateau. Future code optimizations are needed.

### 3. Error Rates with Increasing Data Size

- **Observation**: Error rates unexpectedly increased with larger datasets.
- **Conclusion**: Contrary to expectations based on the Law of Large Numbers, error rates increased due to a suspected bug. Further investigation is required.
  - This is likely a bug in my code

## References

- **Source Video**: [CVM Algorithm Explanation](https://www.youtube.com/watch?v=MZI3aL1igP8&t=158s)
- **Research Papers**: Refer to the original paper for a complete understanding of the CVM algorithm's theoretical background.

---

*Note: This README summarizes the implementation and findings related to the CVM algorithm. Further details, including visual findings and code snippets, are available within the repository.*
