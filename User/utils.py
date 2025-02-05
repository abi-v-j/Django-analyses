import csv
from pymongo import MongoClient
from django.conf import settings

def insert_csv_into_mongodb(collection_name, csv_file_path):
    """
    Reads a CSV file and inserts its data into the specified MongoDB collection.

    Args:
        collection_name (str): The name of the MongoDB collection.
        csv_file_path (str): The path to the CSV file.

    Returns:
        dict: A summary of the insertion result.
    """
    try:
        # Connect to MongoDB
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]

        # Select the collection
        collection = db[collection_name]

        # Read the CSV file and prepare the dataset
        with open(csv_file_path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            dataset = [row for row in reader]  # Convert rows to dictionaries

        # Insert the dataset into MongoDB
        if dataset:
            result = collection.insert_many(dataset)
        else:
            raise ValueError("CSV file is empty.")

        # Close the connection
        client.close()

        # Return a summary of the operation
        return {
            "status": "success",
            "inserted_count": len(result.inserted_ids),
            "inserted_ids": result.inserted_ids
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
