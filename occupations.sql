--descripción: https://stackoverflow.com/questions/36391120/mysql-query-error-using-union-union-all-and-group-by


--mi solución:

select concat(name, "(", (SUBSTRING(Occupation, 1, 1)), ")")
from OCCUPATIONS
order by name;

select concat("There are a total of ", count(occupation)," ", lower(occupation), "s.")
from OCCUPATIONS
group by occupation
order by count(occupation)asc, occupation;