select * from imported_documents;

select unnest(xpath('.//type/release_year/country/@country', xml))::text as countries, count(*) as total_movies
from imported_documents
where id = 1
group by countries
order by total_movies asc;

select
unnest(xpath('(.//type/release_year/country/movie[number(score)>number("7")])/title/text()', xml))::text as title,
unnest(xpath('(.//type/release_year/country/movie[number(score)>number("7")])/score/text()', xml))::text::float as score
from imported_documents
where id = 1
order by score desc;

select unnest(xpath('.//type/@type', xml))::text as tipo  from imported_documents
where xpath('.//type/@type', xml)::text = 'Movie';



select
unnest(xpath('(.//movie[title = "Midnight Mass"])/title/text()', xml))::text as title,
unnest(xpath('(.//movie[title = "Midnight Mass"])/score/text()', xml))::text::float as score,
unnest(xpath('(.//movie[title = "Midnight Mass"])/duration/text()', xml))::text as duration,
unnest(xpath('(.//movie[title = "Midnight Mass"])/rating/text()', xml))::text as rating,
unnest(xpath('(.//movie[title = "Midnight Mass"])/city/text()', xml))::text as city,
unnest(xpath('(.//movie[title = "Midnight Mass"])/listed_in/text()', xml))::text as category,
unnest(xpath('(.//movie[title = "Midnight Mass"])/director/text()', xml))::text as director
from imported_documents
where id = 1;








select
unnest(xpath('(.//type/release_year/country/movie/title/text()', xml))::text as title,
unnest(xpath('(.//type/release_year/country/movie/duration/text()', xml))::text::float as score
unnest(xpath('(.//type/release_year/country/movie/listed_in/text()', xml))::text as listed_in
from imported_documents
where id = 1
order by score desc;

select unnest(xpath('.//type/release_year/country/movie/title/@title', xml))::text as title  from imported_documents 
where xpath('.//type/@type', xml)::text = 'Movie' 
and xpath('.//type/release_year/country/movie/title/@title', xml)::text = 'India';


select unnest(xpath('.//type/release_year/country/movie/title/@title', xml))::text as title  from imported_documents 
where xpath('.//type/release_year/@release_year', xml)::text::float = '2020' 
or xpath('.//type/release_year/@release_year', xml)::text::float = '2021'


 