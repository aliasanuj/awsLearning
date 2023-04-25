'''checking the connection with S3 buckets'''
# import boto3
# client = boto3.client('s3')
# res = client.list_buckets()
# print(res)


'''https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html'''
###creating S3 buckets
# import logging
# import boto3
# from botocore.exceptions import ClientError
# def create_bucket(bucket_name, region=None):
#     """Create an S3 bucket in a specified region
#     If a region is not specified, the bucket is created in the S3 default
#     region (us-east-1).
#     :param bucket_name: Bucket to create
#     :param region: String region to create bucket in, e.g., 'us-west-2'
#     :return: True if bucket created, else False
#     """
#     # Create bucket
#     try:
#         if region is None:
#             s3_client = boto3.client('s3')
#             s3_client.create_bucket(Bucket=bucket_name)
#         else:
#             s3_client = boto3.client('s3', region_name=region)
#             location = {'LocationConstraint': region}
#             s3_client.create_bucket(Bucket=bucket_name,
#                                     CreateBucketConfiguration=location)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True
#
# create_bucket('demo-bucket-creation')

'''Retrieve the list of existing buckets'''
# import boto3
# s3 = boto3.client('s3')
# response = s3.list_buckets()
# # Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')



