# Pascal Triangle

## Algorithm used:
Space-Optimized Algorithm:

* First, we check if the input n is a positive integer. If it's less than or equal to 0, we return an empty list since there are no columns to generate.

* We initialize triangle as a list containing the first row of Pascal's triangle, which is just the value 1.

* We also initialize prev_row as a list containing the first row. This will be used to generate subsequent rows.

* Next, we iterate i from 1 to n - 1, representing the rows of Pascal's triangle excluding the first row.

* For each row, we initialize current_row as a list with the first element set to 1, as the first element of each row in Pascal's triangle is always 1.

* Within the row, we iterate j from 1 to i-1, representing the columns excluding the first and last columns.

* In each iteration, we calculate the value at position (i, j) by summing the corresponding values from the previous row (i-1, j-1) and (i-1, j).

* We append the calculated value to current_row.

* After the inner loop completes, we append 1 to current_row, as the last element of each row in Pascal's triangle is always 1.

* We append current_row to triangle, representing the current row generated.

* Finally, we update prev_row to be current_row for the next iteration, as it will be used to generate the subsequent row.

* Once the loop finishes, we have generated Pascal's triangle up to n rows. We return triangle as the resulting Pascal's triangle.
