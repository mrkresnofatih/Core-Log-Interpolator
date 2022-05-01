# Core & Log Interpolator

## Generate CSV File of the Core-Log Interpolations

The code below is for generating a CSV of core depth with their corresponding Log values. 
The Core Values to be written in the output CSV can be cherry-picked by listing down the core-data column names. 
The Log Values to be interpolated & written in the output CSV can be cherry-picked by listing down the log-data column names.

```python
import coreloginterpolate as cli

cli.interpolate_core_with_log(
    "T1-GRH2.txt",                                      # Core Data File in Folder: ./input_core
    ["DEPTH", "KHINF", "KHAIR", "PORHE", "KVINF"],      # Core Data Columns cherry-picked: must be selected in order
    0,                                                  # Depth Column Index of Core Data
    "L1-GRH2.txt",                                      # Log Data File in Folder: ./input_log
    ["DEPTH", "CLI", "DCOR", "GR", "LLD", "LLD"],       # Log Data Columns cherry-picked: must be selected in order
    0,                                                  # Depth Column Index of Log Data
    "M1-GRH2.csv"                                       # Output Filename in Folder: output
)
```

## What are Input Core & Input Log files?

They are a `.txt` file containing core and log data which its empty values have been replaced with 0. 
The table is copied into a `.txt` which results in a form of space delimited text.