import boto3

client = boto3.client('s3')
res = client.list_buckets()
print(res)

