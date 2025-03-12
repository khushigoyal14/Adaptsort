# AdaptSort: An Adaptive Hybrid Sorting Algorithm

**AdaptSort** is a hybrid sorting algorithm that dynamically adapts based on the level of unsortedness in the input data. By integrating multiple sorting techniques, AdaptSort optimizes for different levels of pre-sortedness, achieving efficiency gains over traditional sorting methods in practical scenarios.

Key Features:
- Adaptive selection: Dynamically switches between QuickSort, InsertionSort, and stable merging depending on input characteristics.
- Efficient performance: Demonstrates lower computational overhead compared to traditional sorting algorithms for partially sorted data.
- Scalability: Designed for real-world datasets, including financial data, search indexing, and AI model preprocessing.

Installation:
Clone the repository to start using AdaptSort:
   git clone https://github.com/khushigoyal14/AdaptSort.git
   cd AdaptSort

How to Use AdaptSort (Python):
   from src/python/adapt_sort import adapt_sort_main

   arr = [4, 3, 1, 2, 5]
   sorted_arr = adapt_sort_main(arr)
   print(sorted_arr) # Output: [1, 2, 3, 4, 5]

Performance Benchmarks:
AdaptSort has been benchmarked against traditional sorting algorithms and demonstrates performance improvements in cases of partial pre-sortedness.

Table:
Algorithm | Best-Case | Average-Case | Worst-Case | Memory Usage
---------------|-------------|--------------|-------------|--------------
QuickSort | O(n log n) | O(n log n) | O(n²) | O(log n)
MergeSort | O(n log n) | O(n log n) | O(n log n) | O(n)
AdaptSort | O(n) | O(n log n) | O(n log n) | O(log n)

Citation and Research Reference:
The IEEE publication for AdaptSort is currently in process. Once published, the citation details will be updated here.

Contributing:
We welcome contributions. See CONTRIBUTING.md for details.

License:
This project is licensed under the MIT License. See LICENSE for details.
