# Acme Corp

Back-End Track

Company: "Acme Corp" is a fast-growing startup developing innovative supply chain management software.

Team: The Acme Corp Back-End team consists of 8 people who are responsible for developing and supporting the server-side of the web application and API.

Task:

The Senior Back-End Developer at Acme Corp is looking for an intern to help with the development of new API features. As part of your test assignment, you will need to complete the following tasks:

1. Develop an API method to create a new product:

Define a data model for a product, including fields such as name, description, price, category, and so on.
Create an API method (POST /products) that accepts a JSON object with product data and saves it to the database.
Return a JSON object with information about the created product.
2. Develop an API method to get a list of products:

Create an API method (GET /products) that returns a list of all products from the database.
Add the ability to filter products by category (use the GET /products?category= parameter).
Add the ability to sort products by price (use the GET /products?sort=price parameter).
3. Develop an API method to get information about a specific product:

Create an API method (GET /products/:id) that takes a product ID and returns information about it.
Handle a 404 error if the product with the specified ID is not found.
Requirements:

Experience in developing with Python or Java (of your choice)
Knowledge of OOP
Knowledge of SQL
Experience working with APIs
Ability to write clean and readable code
Evaluation:

Your test assignment will be evaluated on the following criteria:

Correctness of task completion
Code quality
Code readability
API documentation
Effective use of technologies
Creative approach
Additional materials:

Flask (Python)
Spring Boot (Java)
PostgreSQL
REST API design
Possible questions and answers:

1. Tell us about your experience in developing with Python/Java.

I have experience in developing with Python/Java (specify language) for (specify number) years.
I have worked on such projects as (list projects).
I am familiar with the basic principles of OOP, such as encapsulation, inheritance, and polymorphism.
2. How will you implement the API method to create a new product?

I will create a data model for the product using appropriate libraries (ORM for Python/Java).
I will define an API method (POST /products) using the Flask/Spring Boot framework.
I will accept a JSON object with product data, deserialize it into a data model object, and save it to the database.
I will return a JSON object with information about the created product.
3. How will you implement the API method to get a list of products?

I will create an API method (GET /products) using the Flask/Spring Boot framework.
I will use an SQL query to get a list of products from the database.
I will process the query results and serialize them into a JSON object.
I will add the ability to filter products by category, using a WHERE clause in the SQL query.
I will add the ability to sort products by price, using an ORDER BY clause in the SQL query.
4. How will you test your API?

I will use Unit tests to test individual components of the API.
I will use Integration tests to test the interaction of different API methods.
I will use End-to-end tests to test the overall functionality of the API.
5. How will you document your API?

I will use OpenAPI Specification (Swagger) to generate API documentation.
The documentation will include descriptions of API methods, request and response formats, and error codes.
# Screenshots

![Main 1](/screenshots/main.png)
![Main 2](/screenshots/main2.png)
![Create Product Request](/screenshots/create-product-request.png)
![Create Product Response](/screenshots/create-product-response.png)
![List of Products](/screenshots/list-of-products.png)
![Product Detail](/screenshots/product-detail.png)
![Product Detail Not Found](/screenshots/product-detail-not-found.png)


# Video

Demostration - https://drive.google.com/file/d/1tt6wFUaPKJlTnU7fklC5Om_OzTivU7TP/view?usp=sharing

Work - https://drive.google.com/file/d/1SADqcYWhMBWOanvYM714XyGRlJSggUc5/view?usp=sharing