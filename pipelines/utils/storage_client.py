import os
import boto3
from botocore.client import Config

"""Client class to interact with Scaleway Object Storage."""


class ObjectStorageClient:

    region_name = "fr-par"
    endpoint_url = "https://s3.fr-par.scw.cloud"
    bucket_name = "pollution-eau-s3"
    def __init__(self):
        # Need to use V2 signature for upload and V4 for download
        self.client_v2 = self.build_client("s3")
        self.client_v4 = self.build_client("s3v4")

    @staticmethod
    def build_client(signature_version: str = "s3v4"):
        return boto3.session.Session().client(
            service_name='s3',
            config=Config(signature_version=signature_version),
            region_name=ObjectStorageClient.region_name,
            use_ssl=True,
            endpoint_url=ObjectStorageClient.endpoint_url,
            aws_access_key_id=os.getenv('SCW_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('SCW_SECRET_KEY'),
        )

    def list_buckets(self):
        response = self.client_v4.list_buckets()
        return response['Buckets']

    def list_objects(self):
        response = self.client_v4.list_objects(Bucket=self.bucket_name)
        return response['Contents']

    def download_object(self, key, local_path):
        self.client_v4.download_file(self.bucket_name, key, local_path)

    def upload_object(self, local_path, object_name=None):
        if object_name is None:
            object_name = os.path.basename(local_path)
        self.client_v2.upload_file(local_path, self.bucket_name, object_name)

    def delete_object(self, key):
        self.client_v4.delete_object(Bucket=self.bucket_name, Key=key)
