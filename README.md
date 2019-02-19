# Association-Rule-Mining

Association rule mining is a procedure which is meant to find frequent patterns, correlations, associations, or causal structures from data sets found in various kinds of databases such as relational databases, transactional databases, and other forms of data repositories.

Given a set of transactions, association rule mining aims to find the rules which enable us to predict the occurrence of a specific item based on the occurrences of the other items in the transaction.

## Data

We used the Groceries Market Basket Dataset, which can be found [here](http://www.sci.csueastbay.edu/~esuess/classes/Statistics_6620/Presentations/ml13/groceries.csv). The dataset contains 9835 transactions by customers shopping for groceries. The data contains 169 unique items. The data can be found in the folder 'data'.

## Run
* Pre-processing of data and generation of "items" pickle file  is done using
```python
    python3 preProcess.py
```
The csv file was read transaction by transaction and each transaction was saved as a list. A mapping was created from the unique items in the dataset to integers so that each item corresponded to a unique integer. The entire data was mapped to integers to reduce the storage and computational requirement. A reverse mapping was created from the integers to the items, so that the item names could be written in the final output pickle file.
All the pickle files generated in such a way are stored inside the pkl_files folder
### Directory Structure
```
Association-Rule-Mining/
+-- Apriori
|   +-- gen_freqitemset.py (generates frequent itemset list using apriori)
|   +-- merge_itemsets.py (generates (k+1) length subsets of all k length sets)
|   +-- powerset.py (creates subsets of length k and set L greater than min support)
|   +-- ruleGeneration.py (generates interesting rules based on apriori)
|   +-- rules.txt (output file containing frequent itemsets and rules)
+-- FP_Tree
|   +-- fp_growth.py ( mine frequent itemsets by generating trees)
|   +-- transactions.py (read data from csv and preprocess)
+--  closed.py(generates closed frequent itemsets)
+--  maximal.py(generates closed frequent itemsets)
+--  preProcess.py(read data from csv and preprocess)


```
