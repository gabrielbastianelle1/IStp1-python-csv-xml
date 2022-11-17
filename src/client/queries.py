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
]
