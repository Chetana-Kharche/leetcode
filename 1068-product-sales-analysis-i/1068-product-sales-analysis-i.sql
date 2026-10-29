select p.product_name, s.year, s.price from Sales s
left join Product p
ON p.product_id=s.product_id;