SENTENCES = {

# ==========================================
# FILE COMMANDS
# ==========================================

"P001": "set file A as base file",
"P002": "set file B as base file",
"P003": "load file A",
"P004": "load file B",
"P005": "load file C as reference file",
"P006": "load file C as mapping file",
"P007": "create working copy of file A",
"P008": "create output file from file A",
"P009": "replace file A with file B",
"P010": "remove file B from workflow",

# ==========================================
# KEY COMMANDS
# ==========================================

"P011": "use column 1 in file A as matching key",
"P012": "use column 2 in file A as matching key",
"P013": "use column 3 in file A as matching key",
"P014": "use column 4 in file A as matching key",
"P015": "use column 5 in file A as matching key",
"P016": "use column 1 and column 2 in file A as composite key",
"P017": "create composite key in file A using column 1 and column 2",
"P018": "create composite key in file B using column 1 and column 2",
"P019": "normalize values in column 1 of file A",
"P020": "replace matching key column in file B",

# ==========================================
# JOIN COMMANDS
# ==========================================

"P021": "match file B against file A using column 1",
"P022": "match file C against file A using column 1",
"P023": "left join file B to file A using column 1",
"P024": "right join file B to file A using column 1",
"P025": "inner join file B to file A using column 1",
"P026": "full join file B to file A using column 1",
"P027": "append file B side by side to file A using column 1",
"P028": "append file C side by side to file A using column 1",
"P029": "merge file B into file A using column 1",
"P030": "lookup records from file B using column 1",

# ==========================================
# COLUMN TRANSFER COMMANDS
# ==========================================

"P031": "copy column 2 from file B to column 3 in file A on matching column 1",
"P032": "copy column 4 from file B to column 5 in file A on matching column 1",
"P033": "copy column 6 from file B to column 7 in file A on matching column 1",
"P034": "copy column 8 from file B to column 9 in file A on matching column 1",
"P035": "copy all matching columns from file B to file A using column 1",
"P036": "take column 2 from file B",
"P037": "paste column 2 from file B into column 5 in file A",
"P038": "transfer column 3 from file B to column 3 in file A on matching column 1",
"P039": "transfer column 4 from file B to column 4 in file A on matching column 1",
"P040": "populate blank values in column 5 of file A from column 5 of file B on matching column 1",

# ==========================================
# COLUMN MAINTENANCE
# ==========================================

"P041": "add new column 10 to file A",
"P042": "rename column 2 in file A",
"P043": "rename column 3 in file A",
"P044": "delete column 4 from file A",
"P045": "move column 5 after column 2 in file A",
"P046": "insert new column after column 6 in file A",
"P047": "duplicate column 7 in file A",
"P048": "create derived column 8 in file A using column 2 and column 3",

# ==========================================
# DATA CLEANSING
# ==========================================

"P049": "trim spaces from column 1 in file A",
"P050": "trim spaces from column 2 in file A",
"P051": "convert values in column 1 of file A to uppercase",
"P052": "convert values in column 2 of file A to uppercase",
"P053": "remove special characters from column 3 in file A",
"P054": "normalize date format in column 4 of file A",
"P055": "replace blank values in column 5 of file A with zero",
"P056": "replace null values in column 5 of file A with blank",
"P057": "round values in column 6 of file A to two decimals",
"P058": "standardize values in column 7 of file A",

# ==========================================
# FILTER COMMANDS
# ==========================================

"P059": "keep records in file A where column 1 exists in file B",
"P060": "keep records in file A where column 1 does not exist in file B",
"P061": "remove records in file A where column 1 exists in file B",
"P062": "remove records in file A where column 1 does not exist in file B",
"P063": "filter records in file A where column 2 equals zero",
"P064": "filter records in file A where column 2 is not zero",
"P065": "exclude records in file A where column 3 equals value",
"P066": "keep records in file A where column 3 equals value",

# ==========================================
# COMPARISON COMMANDS
# ==========================================

"P093": "compare column 2 in file A with column 2 in file B on matching column 1",
"P094": "compare column 3 in file A with column 3 in file B on matching column 1",
"P095": "compare column 4 in file A with column 4 in file B on matching column 1",
"P096": "compare column 5 in file A with column 5 in file B on matching column 1",
"P097": "compare column 6 in file A with column 6 in file B on matching column 1",
"P098": "compare column 7 in file A with column 7 in file B on matching column 1",
"P099": "compare number of records in file A with file B",

# ==========================================
# DIFFERENCE COMMANDS
# ==========================================

"P100": "calculate difference between column 2 in file A and column 2 in file B on matching column 1 and store result in column 10 of file A",

"P101": "calculate difference between column 3 in file A and column 3 in file B on matching column 1 and store result in column 11 of file A",

"P102": "calculate percentage difference between column 4 in file A and column 4 in file B on matching column 1 and store result in column 12 of file A",

# ==========================================
# CONDITIONAL TRANSFER COMMANDS
# ==========================================

"P149": "if column 2 in file A is blank populate column 2 in file A from column 2 in file B on matching column 1",

"P150": "if column 3 in file A is blank populate column 3 in file A from column 3 in file B on matching column 1",

"P151": "if column 4 in file A contains value populate column 5 in file A from column 6 in file B on matching column 1",

"P152": "if column 7 in file A equals zero populate column 7 in file A from column 7 in file B on matching column 1",

"P153": "if column 8 in file A is not blank populate column 9 in file A from column 9 in file B on matching column 1",

# ==========================================
# ADVANCED CONDITIONAL TRANSFER
# ==========================================

"P154": "if column 2 in file A is not blank and column 3 in file A is blank populate column 3 in file A from column 3 in file B on matching column 1",

"P155": "if column 2 in file A contains value populate column 4 in file A from column 6 in file B on matching column 1",

"P156": "if column 2 in file A equals value populate column 8 in file A from column 8 in file B on matching column 1",

"P157": "if column 3 in file A exceeds value populate column 9 in file A from column 9 in file B on matching column 1",

# ==========================================
# LOOKUP COMMANDS
# ==========================================

"P158": "lookup column 2 from file B using column 1 and populate column 2 in file A",

"P159": "lookup column 3 from file B using column 1 and populate column 3 in file A",

"P160": "lookup column 4 from file C using column 2 and populate column 5 in file A",

# ==========================================
# DUPLICATE COMMANDS
# ==========================================

"P161": "identify duplicate values in column 1 of file A",
"P162": "remove duplicate values from column 1 of file A",
"P163": "keep first occurrence of duplicate values in column 1 of file A",
"P164": "keep latest occurrence of duplicate values in column 1 of file A",

# ==========================================
# OUTPUT COMMANDS
# ==========================================

"P165": "generate matched records report from file A",
"P166": "generate unmatched records report from file A",
"P167": "generate break report from file A",
"P168": "generate reconciliation summary from file A",
"P169": "generate final reconciliation report from file A",
"P170": "export file A as output file",


# ==========================================
# CONDITIONAL COLUMN POPULATION
# ==========================================

"P149": "populate quantity from file B into file A on matching isin",
"P150": "populate market value from file B into file A on matching isin",
"P151": "populate nav from file B into file A on matching isin",
"P152": "populate currency from file B into file A on matching isin",
"P153": "populate trade date from file B into file A on matching isin",


# ==========================================
# CONDITIONAL POPULATION - DATE CHECK
# ==========================================

"P154": "if trade date exists in file A populate quantity from file B on matching isin",
"P155": "if trade date exists in file A populate market value from file B on matching isin",
"P156": "if settlement date exists in file A populate quantity from file B on matching isin",
"P157": "if settlement date exists in file A populate nav from file B on matching isin",
"P158": "if date column xyz contains value populate column abc from file B on matching isin",


# ==========================================
# CONDITIONAL POPULATION - BLANK CHECK
# ==========================================

"P159": "if quantity is blank in file A populate quantity from file B on matching isin",
"P160": "if market value is blank in file A populate market value from file B on matching isin",
"P161": "if currency is blank in file A populate currency from file B on matching isin",
"P162": "if nav is blank in file A populate nav from file B on matching isin",
"P163": "if column xyz is blank populate column abc from file B on matching isin",


# ==========================================
# CONDITIONAL POPULATION - NOT BLANK CHECK
# ==========================================

"P164": "if quantity is not blank in file A populate quantity difference",
"P165": "if currency is not blank in file A populate mapped currency",
"P166": "if isin is not blank in file A populate security type from reference file",


# ==========================================
# CONDITIONAL POPULATION - VALUE CHECK
# ==========================================

"P167": "if quantity equals zero populate quantity from file B on matching isin",
"P168": "if quantity is greater than zero populate market value from file B on matching isin",
"P169": "if market value exceeds threshold populate tolerance status",
"P170": "if currency equals usd populate exchange rate",
"P171": "if fund code equals abc populate account code",


# ==========================================
# CONDITIONAL POPULATION - MATCH CHECK
# ==========================================

"P172": "if isin matches populate quantity from file B",
"P173": "if isin matches populate market value from file B",
"P174": "if account and isin match populate quantity from file B",
"P175": "if trade id matches populate settlement amount from file B",
"P176": "if security code matches populate security name from file B",


# ==========================================
# CONDITIONAL POPULATION - MULTIPLE CONDITIONS
# ==========================================

"P177": "if isin matches and trade date exists populate quantity from file B",
"P178": "if isin matches and quantity is blank populate quantity from file B",
"P179": "if isin matches and market value is blank populate market value from file B",
"P180": "if account matches and currency matches populate nav from file B",
"P181": "if account and isin match populate market value from file B",


# ==========================================
# CONDITIONAL COLUMN TO COLUMN TRANSFER
# ==========================================

"P182": "populate column xyz in file A from column abc in file B on matching isin",
"P183": "populate column xyz in file A from column abc in file B on matching account",
"P184": "populate column xyz in file A from column abc in file B on matching trade id",
"P185": "copy column abc from file B into column xyz in file A on matching isin",
"P186": "transfer column abc from file B into column xyz in file A on matching isin",


# ==========================================
# CONDITIONAL COLUMN TO COLUMN TRANSFER WITH CHECKS
# ==========================================

"P187": "if column date1 contains value populate column quantity1 from column quantity2 on matching isin",
"P188": "if column trade date contains value populate column market value from file B on matching isin",
"P189": "if column xyz is blank populate column abc from file B on matching isin",
"P190": "if column xyz equals zero populate column abc from file B on matching isin",
"P191": "if column xyz is not blank populate column abc from file B on matching isin",


# ==========================================
# LOOKUP + POPULATE COMMANDS
# ==========================================

"P192": "lookup file B using isin and populate quantity",
"P193": "lookup file B using isin and populate market value",
"P194": "lookup file B using account and populate account description",
"P195": "lookup reference file using security code and populate security type",
"P196": "lookup mapping file using fund code and populate account code",


# ==========================================
# ADVANCED RECON OPERATIONS
# ==========================================

"P197": "populate difference only when quantity mismatch exists",
"P198": "populate break reason when market value mismatch exists",
"P199": "populate exception flag when records are unmatched",
"P200": "populate reconciliation status based on comparison result",
"P201": "populate matched status when quantity and market value match",
"P202": "populate unmatched status when no matching isin found",


"P311": "populate column 1 in file A from column 1 in file B on matching column 1",

"P312": "copy column 1 from file B to file A",

"P313": "compare column 1 in file A with column 1 in file B on matching column 1",

"P314": "calculate difference between column 1 in file A and column 1 in file B",

"P315": "sum column 1 in file A",

"P316": "group file A by column 1",

"P317": "filter file A where column 1 is blank",

"P318": "filter file A where column 1 is not blank",

"P319": "filter file A where column 1 equals value",

"P320": "filter file A where column 1 contains value",

"P321": "remove duplicate values from column 1 in file A",

"P322": "identify duplicate values in column 1 of file A",

"P323": "create composite key in file A using column 1 and column 2",

"P324": "match file B against file A using column 1",

"P325": "lookup column 2 from file B using column 1",

"P326": "populate column 5 in file A from column 7 in file B on matching column 1",

"P327": "if column 3 in file A is blank populate from column 4 in file B on matching column 1",

"P328": "if column 3 in file A is not blank compare with column 4 in file B on matching column 1",

"P329": "store comparison result in column 10 of file A",

"P330": "store difference result in column 11 of file A",

}