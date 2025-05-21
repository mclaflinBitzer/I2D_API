from api_call import api_call
from data_transformation import data_transformations
from data_export import export_data


print("running api call function")
all_articles = api_call()

print("running data transformation function")
transformed_data = data_transformations(all_articles)

print("running data export function")
export_data(transformed_data)
