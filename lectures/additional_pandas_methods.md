# Additional Useful Pandas Methods

Here are some additional useful pandas methods that weren't covered in the lecture:

## 1. Data Cleaning and Transformation
- `df.replace()`: Replace values in DataFrame
- `df.duplicated()`: Find duplicate rows
- `df.drop_duplicates()`: Remove duplicate rows
- `df.fillna()`: Fill missing values with specified values
- `df.interpolate()`: Fill missing values using interpolation

## 2. Advanced Indexing and Selection
- `df.query()`: Filter using a query expression
- `df.where()`: Replace values where condition is False
- `df.mask()`: Replace values where condition is True
- `df.between()`: Select values between two values
- `df.nlargest()` and `df.nsmallest()`: Get n largest/smallest values

## 3. Time Series Operations
- `df.resample()`: Resample time series data
- `df.rolling()`: Rolling window calculations
- `df.expanding()`: Expanding window calculations
- `df.shift()`: Shift index by desired number of periods
- `df.diff()`: Calculate difference between consecutive elements

## 4. Data Aggregation and Grouping
- `df.agg()`: Aggregate using multiple operations
- `df.transform()`: Transform data using a function
- `df.pivot_table()`: Create a pivot table
- `df.crosstab()`: Compute a cross-tabulation
- `df.melt()`: Unpivot DataFrame from wide to long format

## 5. String Operations
- `df.str.contains()`: Test if pattern is contained in string
- `df.str.extract()`: Extract capture groups
- `df.str.split()`: Split strings on delimiter
- `df.str.cat()`: Concatenate strings
- `df.str.replace()`: Replace occurrences of pattern

## 6. Memory and Performance
- `df.memory_usage()`: Get memory usage of columns
- `df.convert_dtypes()`: Convert columns to best possible dtypes
- `df.astype()`: Cast to specified dtype
- `df.select_dtypes()`: Select columns based on dtype

## 7. Visualization
- `df.plot()`: Create various plots
- `df.hist()`: Create histogram
- `df.boxplot()`: Create box plot
- `df.scatter_matrix()`: Create scatter plot matrix

## 8. File Operations
- `df.to_excel()`: Write to Excel file
- `df.to_json()`: Convert to JSON string
- `df.to_sql()`: Write to SQL database
- `df.to_parquet()`: Write to Parquet file

## 9. Advanced Operations
- `df.eval()`: Evaluate string expression
- `df.applymap()`: Apply function element-wise
- `df.combine_first()`: Combine two DataFrames
- `df.update()`: Update values in place
- `df.merge()`: Merge DataFrames (more flexible than join)

## 10. Data Quality
- `df.isna()`: Detect missing values
- `df.notna()`: Detect non-missing values
- `df.isin()`: Check if values are contained in list
- `df.describe()`: Generate descriptive statistics

These methods can be particularly useful for:
- Data cleaning and preprocessing
- Time series analysis
- Statistical analysis
- Data visualization
- Performance optimization
- Data export/import in various formats 