-- View first rows
SELECT * FROM sales_data
LIMIT 10;


-- Total sales
SELECT SUM(Sales) AS total_sales
FROM sales_data;


-- Sales by Category
SELECT Category, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Category;


-- Profit by Category
SELECT Category, SUM(Profit) AS total_profit
FROM sales_data
GROUP BY Category;


-- Sales by Region
SELECT Region, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Region;


-- Top 10 Products
SELECT "Product Name", SUM(Sales) AS total_sales
FROM sales_data
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;


-- Top Customers
SELECT "Customer Name", SUM(Sales) AS total_sales
FROM sales_data
GROUP BY "Customer Name"
ORDER BY total_sales DESC
LIMIT 10;