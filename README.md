#### PROBLEM STATEMENT
Given transactional data of gifts bought by customers, recommend the gifts the customers can buy

#### METHOD
##### Datagathering
Transactional data of customer who bought gifts with the following columsn
InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country

##### Datapreprocessing
Since user based recommendation system needed ratings, extrapolation was done derive ratings from the amount of time the gifts were bought by customers. Customer's who have purchased atleast 50 times are only included for analysis to avoid data sparsity

##### Algorithm
User based recommendation system is used that contains the following steps

1.Build user-user matrix

2.Use cosine similarity to find out the similarity between Users 

3.Find the most similar users

4.Suggest the gifts for the chosen user depending on weighted average of ratings given to the gifts

##### Techniques involved
recommendation algorithm

##### Languages and tools used
Python

##### Results
The snippets of the results is attached


![userbasedrecomsys](https://user-images.githubusercontent.com/103910965/186057140-8e3db4ee-b94a-4c76-9cfc-d2d63456821a.PNG)

