select * from imported_documents;

select unnest(xpath('.//type/release_year/country/@country', xml))::text as countries, count(*) as total_movies
from imported_documents
where id = 1
group by countries
order by total_movies asc;

 

select unnest(xpath('.//type/@type', xml))::text as tipo  from imported_documents
where xpath('.//type/@type', xml)::text = 'Movie';