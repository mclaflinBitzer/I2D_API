from api_call import api_call
from data_transformation import data_transformations
from data_export import export_data



all_articles = api_call()

transformed_data = data_transformations(all_articles)

export_data(transformed_data)
