from api_call import api_call, article_call
from data_transformation import data_transformations
from data_export import export_data, email_records_export


print("running api call function")
all_articles = api_call()

print("running data transformation function")
transformed_data = data_transformations(all_articles)

print("running data export function")
export_data(transformed_data)

print("running article call function")
article_data = article_call()

print("running data transformation function for article data")
article_transformed = data_transformations(article_data)

print("running data export function for article data")
email_records_export(article_transformed)
