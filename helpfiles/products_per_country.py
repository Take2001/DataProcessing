# laat zien welke producten er in een bepaald land te koop zijn voor een bepaalde input_data
def products_country(input_data, country):
    products = []
    fp_country = input_data.loc[input_data['adm0_name'] == country]
    products_total = fp_country['cm_name']
    product_list = products_total.tolist()
    for item in product_list:
        if item not in products:
            products.append(item)
    return(products)
# products_country(df_foodprices, 'Mali')