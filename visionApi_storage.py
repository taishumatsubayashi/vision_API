import requests
import io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import storage

bucket_name = "taishuvisionapi"

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
blobs = bucket.list_blobs()

blob_list = [blob.name for blob in blobs]

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print(imageName + 'Labels:')

    for label in labels:
        print(label.description)

if __name__ == "__main__":
    for imageName in blob_list:
        uri = "gs://taishuvisionapi/" + imageName
        detect_labels_uri(uri)
