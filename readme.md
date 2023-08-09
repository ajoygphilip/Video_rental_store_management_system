**Design and develop a video rental store management system with the following features:**

* User Roles: There are two types of users: customers and store managers.
* Authentication: Implement a secure authentication system that allows registered users to log in.
* Movie Catalog:
    * Store managers can add, update, and delete movies in the catalog.
    * Each movie has a title, description, release year, and genre.
* Customer Rentals:
    * Customers can rent movies from the catalog.
    * Option to track the rental duration and due date(2 weeks from issue)
* Custom Logic - Late Returns and Fines:
        * Develop a custom algorithm to calculate fines for late returns based on the specified logic:
        * First week: 5 rupees fine per day
        * Subsequent days: 10 rupees fine per day
* Inventory Management:
    * Implement stock tracking for available copies of each movie.
    * Customers cannot rent a movie if all copies are currently rented out.