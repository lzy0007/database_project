
#Overview

overview_totalSales = """

SELECT sum(amount) sales
FROM payment;

"""

overview_totalFilms = """

SELECT count(film_id) total_filmx
FROM film

"""

overview_totalInventory = """

SELECT count(inventory_id) total_inventory
FROM inventory

"""

overview_totalRental = """

SELECT count(rental_id) total_rental
FROM rental

"""

overview_totalCustomers = """

SELECT count(customer_id) total_customer
FROM customer

"""

overview_salesYear = """

SELECT YEAR(p.payment_date) year, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY YEAR(p.payment_date)

"""

#Film
film_highSalesFilm = """

SELECT f.title, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.film_id
ORDER BY sales DESC
LIMIT 1;

"""
film_highSalesCat = """

SELECT cat.name, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category cat ON cat.category_id = fc.category_id
GROUP BY cat.category_id
ORDER BY sales DESC
LIMIT 1;

"""

film_highRatioSalesNumFilmAct = """

SELECT CONCAT(a.first_name, " ", a.last_name) `name`, sum(p.amount) / count(distinct f.film_id) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id
GROUP BY a.actor_id
ORDER BY sales DESC
LIMIT 1;

"""

film_byAct = """

SELECT f.title, CONCAT(a.first_name, " ", a.last_name) `actor`
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON fa.actor_id = a.actor_id

"""

film_byCat = """

SELECT f.title, cat.name category
FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category cat ON cat.category_id = fc.category_id

"""

film_byLang = """

SELECT f.title, l.name language
FROM film f
JOIN language l on l.language_id = f.language_id;

"""

film_byYear = """

SELECT title, release_year
FROM film f;

"""

film_numByAct = """

SELECT CONCAT(a.first_name, " ", a.last_name) `actor`, count(f.film_id) count
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON fa.actor_id = a.actor_id
GROUP BY a.actor_id

"""

film_numByCat = """ 

SELECT cat.name `category`, count(f.film_id) count
FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category cat ON cat.category_id = fc.category_id
GROUP BY cat.category_id

"""

film_numByLang = """

SELECT l.name language, count(f.film_id) count
FROM film f
JOIN language l on l.language_id = f.language_id
GROUP BY l.language_id

"""

film_numByYear = """

SELECT release_year `release year`, count(f.film_id) count
FROM film f
GROUP BY f.release_year;

"""

film_salesByRent = """

SELECT f.rental_rate `Rental Rate`, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.rental_rate

"""

film_salesByDur = """

SELECT f.rental_duration `Rental Duration`, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.rental_duration

"""

film_salesByRat = """

SELECT f.rating `Rating`, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.rating

"""

film_salesByCat = """

SELECT cat.name `Category`, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category cat ON cat.category_id = fc.category_id
GROUP BY cat.category_id

"""


film_salesByFea = """

SELECT f.special_features `Features`, sum(p.amount) sales
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.special_features

"""

#store



#customer



#staff



