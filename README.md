# Generic Decision Tree
A simple Python implementation of the decision tree algorithm. It is designed to be adaptive and work with any correctly formatted dataset.

Originally developed for a college class, all initial tests performed were done with [UCI's Mushroom Data Set](https://archive.ics.uci.edu/ml/datasets/Mushroom). Cross-validation of 10 (or more) folds return 100% accuracy.

### Execution Instructions
1. Create a folder called `Datasets` in the same destination as the python scripts.
2. Add your semicolon separated .csv file to the `Datasets` folder.
   - The `data_handler.py` script can be easily modified to work with other .csv format styles.
3. Execute `start.py` and follow the command prompt instructions.

### Cross-Validation Test Instructions
1. Follow Execution Instructions steps #1 and #2.
2. Execute `fold_testing.py` and follow the command prompt instructions.

### Potential Future Improvements
 - [ ] Range prediction
 - [ ] Flexible .csv handling
 - [ ] Automatically setting thresholds
 - [ ] Honestly a whole bunch of other things