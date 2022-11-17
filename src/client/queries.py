def order_total_movies_per_country(xml_id):

    order = "asc"

    print("a - asc order")
    print("b - desc order")
    opcao = input("choose an option: ")

    match opcao:
        case "a":
            order = "asc"
        case "b":
            order = "desc"

    return f"select unnest(xpath('.//type/release_year/country/@country', xml))::text as countries, count(*) as total_movies from imported_documents where id = {xml_id} group by countries order by total_movies {order};"


queries = [{"query_id": 1, "function": order_total_movies_per_country}]
