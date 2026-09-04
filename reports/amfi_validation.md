# Data Quality Report

## AMFI Code Validation

### Objective

Check whether all AMFI codes in `fund_master` exist in `nav_history`.

### Validation Results

* Total unique AMFI codes in `fund_master`: 40
* Total unique AMFI codes in `nav_history`: 40
* Missing AMFI codes: 0

### Pandas Merge Validation

The `fund_master` and `nav_history` datasets were merged using `amfi_code`.

* Codes found in both datasets (`both`): 40
* Codes present only in `fund_master` (`left_only`): 0

### Conclusion

All 40 AMFI codes in `fund_master` exist in `nav_history`. No missing AMFI codes were identified.
