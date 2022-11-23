import os
def order_total_movies_per_country(xml_id):

    order = "asc"

    print("a - asc order")
    print("b - desc order")
    opcao = input("choose an option: ")
    os.system("clear")

    match opcao:
        case "a":
            order = "asc"
        case "b":
            order = "desc"

    return f"select unnest(xpath('.//type/release_year/country/@country', xml))::text as countries, count(*) as total_movies from imported_documents where id = {xml_id} group by countries order by total_movies {order};"


def order_movie_per_score(xml_id):
    order = "asc"
    mininum = input("insert minimum score: ")

    print("a - asc order")
    print("b - desc order")
    opcao = input("choose an option: ")
    os.system("clear")

    match opcao:
        case "a":
            order = "asc"
        case "b":
            order = "desc"

    return f"select unnest(xpath('(.//type/release_year/country/movie[number(score)>number({mininum})])/title/text()', xml))::text as title,unnest(xpath('(.//type/release_year/country/movie[number(score)>number({mininum})])/score/text()', xml))::text::float as score from imported_documents where id = {xml_id} order by score {order};"


def get_all_data_movie(xml_id):

    movie = input("insert movie name: ")
    
    return f'''with movie as (
                SELECT 
                    unnest(xpath('(.//movie[title =\"{movie}\"])', xml)) as m 
                from 
                    imported_documents 
                where 
                    id={xml_id}) 
                SELECT 
                    (xpath('//title/text()', m))[1]::text as title, 
                    (xpath('//score/text()', m))[1]::text::float as score, 
                    (xpath('//duration/text()', m))[1]::text as duration, 
                    (xpath('//rating/text()', m))[1]::text as rating, 
                    (xpath('//city/text()', m))[1]::text as city, 
                    (xpath('//listed_in/text()', m))[1]::text as category, 
                    (xpath('//director/text()', m))[1]::text as director 
                FROM movie'''
   

def count_movies_per_rating(xml_id):

    year = input("insert year: ")

    return f"select unnest(xpath('(.//type/release_year[@release_year=number({year})]/country/movie)/rating/text()', xml))::text as rating, count(*) as totalMovies from imported_documents where id = {xml_id} group by rating order by totalmovies desc;"


queries = [
    {
        "query_id": 1,
        "function": order_total_movies_per_country,
        "head": ["country", "total movies"],
    },
    {
        "query_id": 2,
        "function": order_movie_per_score,
        "head": ["title", "score"],
    },
    {
        "query_id": 3,
        "function": get_all_data_movie,
        "head": ["title", "score","duration", "rating","city", "category","director"],
    },
    {
        "query_id": 4,
        "function": count_movies_per_rating,
        "head": ["rating", "total movies"],
    }
]
