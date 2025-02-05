from django.shortcuts import render

# Create your views here.
# views.py or any Django script
# from User.utils import insert_csv_into_mongodb

# # Path to your CSV file
# csv_file_path = "./tourism_dataset.csv"
# def data(request):
#     # Insert the CSV data into MongoDB
#     # result = insert_csv_into_mongodb("collection_travel", csv_file_path)

#     # print(result)
#     return render(request,"User/HomePage.html")


from .mongodb_utils import (
    get_most_visited_locations,
    get_highest_revenue_categories,
    get_average_ratings_by_country
)

def dashboard(request):
    # Fetch data
    most_visited = get_most_visited_locations(limit=10)
    print(most_visited)
    highest_revenue_categories = get_highest_revenue_categories()
    print(highest_revenue_categories)
    average_ratings_by_country = get_average_ratings_by_country()

    # Pass data to template
    context = {
        "most_visited": most_visited,
        "highest_revenue_categories": highest_revenue_categories,
        "average_ratings_by_country": average_ratings_by_country
    }
    return render(request, "User/Homepage.html", context)