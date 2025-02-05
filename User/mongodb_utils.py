import json
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb+srv://aj123:aj123@shoppify.fsyemvp.mongodb.net/")
db = client['db_dataset']  
collection = db['collection_travel']

def clean_data(data):
    """Convert numeric fields to appropriate types."""
    return {
        "_id": str(data["_id"]),  # Convert ObjectId to string
        "Location": data["Location"],
        "Country": data["Country"],
        "Category": data["Category"],
        "Visitors": int(data["Visitors"]),  # Ensure integer conversion
        "Rating": float(data["Rating"]),  # Ensure float conversion
        "Revenue": float(data["Revenue"]),  # Ensure float conversion
        "Accommodation_Available": data["Accommodation_Available"]
    }

def get_most_visited_locations(limit=10):
    """Get the most visited locations."""
    pipeline = [
        {"$sort": {"Visitors": -1}},
        {"$limit": limit},
        {"$project": {"_id": 0, "Location": 1, "Visitors": 1}}
    ]
    return list(collection.aggregate(pipeline))
    
def get_highest_revenue_categories():
    """Get total revenue by category."""
    pipeline = [
        {"$match": {"Revenue": {"$gt": 0}}},  # Ignore zero or missing revenue
        {"$group": {"_id": "$Category", "Total_Revenue": {"$sum": "$Revenue"}}},
        {"$sort": {"Total_Revenue": -1}}
    ]
    results = list(collection.aggregate(pipeline))

    # Convert ObjectId to string
    for item in results:
        item["_id"] = str(item["_id"])

    return results


def get_average_ratings_by_country():
    """Get average ratings by country."""
    pipeline = [
        {"$group": {"_id": "$Country", "Average_Rating": {"$avg": "$Rating"}}},
        {"$sort": {"Average_Rating": -1}}
    ]
    results = list(collection.aggregate(pipeline))

    # Convert ObjectId to string
    for item in results:
        item["_id"] = str(item["_id"])

    return results
