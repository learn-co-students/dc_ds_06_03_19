# The flatiron vetrinary hospital    

### Let's examine our database tables  
```
SELECT * FROM cats;
SELECT * FROM dogs;
SELECT * FROM owners;
```
```*``` 
means return all columns in the table.

##### Check your tables characteristics
##### get # rows
```
SELECT count(*) from cats;
```
#####  get # columns

```
SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.COLUMNS
 WHERE table_catalog = ‘mydb’ -- the database
   AND table_name = ‘cats’;
```


### <u>Conditionals </u>
When we hear conditionals we should immediately think about the 
```
WHERE
```
command usually with one or more of the following operators:

``` 
>, >=, <, <=, =, != ,IN, NOT IN, LIKE, %, _, AND, OR
``` 
Understanding the use of like and wild cards (%, _) : [like](https://www.w3schools.com/sql/sql_like.asp)



#### After getting a notification from the health administration
#### We need to find  all cats of breed starting with S to vaccinate them

```
SELECT * FROM cats
WHERE  substr(breed ,0, 2) = 'S'
```
Understanding substr: [substr](https://www.w3schools.com/sql/func_mysql_substr.asp)




#### We know that all pets in houses 2 & 4 are already vaccinated so we can filter them out

Option I:

```
SELECT * FROM cats
WHERE (house_number != 1) AND 
		(house_number != 3)
```

Option II:

```
SELECT * FROM cats
WHERE  substr(breed ,0, 2) = 'S' AND
       house_number IN (1, 3)
```

Option III:

```
SELECT * FROM cats
WHERE  substr(breed ,0, 2) = 'S' AND

house_number NOT IN (2, 4)
```




#### Or if we know all pets are vaccinated in house number 1onwards

```
SELECT * FROM cats
WHERE  substr(breed ,0, 2) = ‘S’
       AND house_number > 1;
```


### <u> GROUP BY </u>
<b> Notice: Group by has to come together with an aggregate function </b>

#### The vet comes to you and asks: how many animals would I need to vaccinate per house?
- If you need to create groups (per house) you need the ```GROUP BY``` command
- Every ```GROUP BY``` command comes together with an aggregate function/s like:
```count, avg, min, max, sum ```

- The only column/s that could be called in the select statement without an aggregate functions are the ones that are mentioned in the ```GROUP BY```



```
SELECT  house_number,
        count(name) FROM cats
        WHERE substr(breed ,0, 2) = ‘S’
GROUP BY house_number;
```



<b> Notice ```WHERE``` conditional will always appear before ```GROUP BY```! </b>


### <u> Joins & WITH </u>
An extreme catenistic organization is protesting about the ratio
of cats to dogs in veterinary facilities. Our vet got stressed
and asks us to check the ratio!

So what do we need? for each house
we want one row with total num cats and total num dogs

let’s first try for each pet to find number of animals



```
SELECT house_number, count(*) as num_cats FROM cats
         GROUP BY house_number
        ORDER BY num_cats DESC;
```
- Since we grouped by house number it's the only column we could have mentioned in the select statement without an aggregate function

<b> Notice: ```ORDER BY``` will always come after ```GROUP BY``` if there is one </b> 



##### The same query would fit for dogs

```
SELECT house_number, count(*) as num_dogs FROM dogs
         GROUP BY house_number
        ORDER BY num_dogs DESC;
```



#### We would like now to join between the two
- ```WITH``` helps to build multiple tables inside one query
these tables will only exist in our existing query and won't be accessible outside the query.




```
WITH cats_num AS

--- first table 
(SELECT house_number
, count(*) as num_cats FROM cats
         GROUP BY house_number
        ORDER BY num_cats DESC),

--- second table        
dogs_num AS (SELECT house_number
, count(*) as num_dogs FROM dogs
         GROUP BY house_number
        ORDER BY num_dogs DESC)

--- now we have two new tables in our query memory that we can access regularly 
--- with select from statements

SELECT cats_num.house_number
        , CAST(num_cats AS decimal) /  CAST(num_cats + num_dogs AS Decimal) AS cats_ratio
FROM cats_num
LEFT JOIN dogs_num ON 
					cats_num.house_number = dogs_num.house_number
ORDER BY cats_ratio desc;
```

#### Did we choose the correct Join?
Left join keeps all the records from the main table (the one called in the select from statement) but doesn't show you keys that are in the joined table (in our case dogs_num) which don't match the keys in the main table (cats_num)

#### Let’s see what would happen if dogs were also placed at house number 5

```INSERT INTO dogs VALUES (‘lulu’, ‘Hound’, 5, 3);```



#### So actually we want here a full join in order to get the keys from both tables


```
WITH cats_num AS

--first table
(SELECT house_number
, count(*) as num_cats FROM cats
         GROUP BY house_number
        ORDER BY num_cats DESC),
        
-- second table         
dogs_num AS (SELECT house_number
, count(*) as num_dogs FROM dogs
         GROUP BY house_number
        ORDER BY num_dogs DESC)

SELECT cats_num.house_number as cats_house
, dogs_num.house_number as dogs_house
        , coalesce(CAST(num_cats AS decimal) /  CAST(num_cats + num_dogs AS Decimal), 0) AS cats_ratio
FROM cats_num
FULL OUTER JOIN dogs_num ON 
				cats_num.house_number = dogs_num.house_number
				ORDER BY cats_ratio desc;
```




#### Do all cats have an owner?
#### What join will you use here?


- let's assume for fun that 0 in the owner_id column (last entry below) means that there is no owner. However we don't know it when we work on the table.


```INSERT INTO cats VALUES (‘tobi’, ‘regular’, 2, 0);```



#### Let's start with returning only cats that have an owner first

```
SELECT * FROM cats
LEFT JOIN owners ON 
			owners.id = cats.owner_id
``` 

<b> Remember: left join will keep all cats in the output. i.e. also cats that don't have an owner - so we actually need a different join</b> 

#### Luckily we have ```INNER JOIN```
- Which will return only records that match in both tables - only cats with an associated owner in the owners table 

```
SELECT * FROM cats
INNER JOIN owners ON 
			owners.id = cats.owner_id
```


#### Now let's return only cats that don’t have an owner

```
SELECT owners.name 
, cats.name AS cat_name FROM cats
LEFT JOIN owners ON 
			owners.id = cats.owner_id
			WHERE owners.name IS NULL
```


### <u> Window functions </u>
<b> Notice: window functions are one of the best things ever happened in SQL </b>

'A window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities.'

Source on window functions: [window functions](https://www.postgresql.org/docs/9.1/tutorial-window.html)

- 

#### Facebook interview question:
Assume we have a table of employee information, which includes salary information.
Write a query to find the names and salaries of the top 5 highest paid employees, in descending order.

##### We are going to use a fake e-commerce data table (pick) - this is used to solve the facebook question with the data we have.

- Let's add to all raw columns another column called 'grouping' with all of its values being 1. 

```
SELECT *
, 1 AS grouping FROM pick;
```

- We will now use the window function (rank()) in order to find the warehouse tours that took the longest time (spi column).
- Notice: we only use the ```rank()``` after we have created the 'grouping' column. This means we need a subquery to create the column 'grouping' and only then can we partition by that.
- The syntax of every window function:

```
window_func() OVER (PARTITION BY col_name_to_partition_data)  
```

#### Our answer to facebook 
```
SELECT date,outboundprocess
		, spi, rank() over (partition by
        grouping order by spi desc) FROM 
        (SELECT *, 1 AS grouping FROM pick) AS pick_w_group;
```        
        
        
# <u> More resources: </u>

-  [youtube tutorials](https://www.youtube.com/watch?v=jNq5EAb2biY&list=PLk1kxccoEnNEtwGZW-3KAcAlhI_Guwh8x) 