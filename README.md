# awsLearning
This is all about AWS learning

#################################################
Run AWS from local : 

Some of the AWS services can be run from local (From any IDE let's say PyCharm in my case). 
If we have to interact with S3 bucket, then we need awscli configuration. For other services like interacting with lambda, we need to have SAM CLI as well.

Interacting with S3 locally (with Pycharm)

	1. Go to AWS  and create IAM user with some basic Policy AdministratorAccess and get the aws_access_key_id and aws_secret_access_key .
	2. Go to PyCharm and install the awscli pip install awscli and after inctalling , configure this with below commands :
	
	PS C:\Git> aws configure
	AWS Access Key ID [None]: AKIAUFYVX5WSZV7P
	AWS Secret Access Key [None]: fFXTacTfSW84ri3eEOnSQtua+p3jE6gE5Ue
	Default region name [None]: us-east-1
	Default output format [None]:
	PS C:\Git>  
	
	3. It will create two files in local users with .aws (as configure files will be created with .filename naming convention) which contain region, secret key and secret password
	
	
	4. Now to check the connection from yourr PyCharm with AWS console run the below code. Also install all the missing module/library like boto3 and all.

	importboto3
	client=boto3.client('s3')
	res=client.list_buckets()
	print(res)
	
	Output :
	{'ResponseMetadata': {'RequestId': 'TCYQS8KEEtyrtdfvdfyZ676BBJHHVQQDQJA', 'HostId': 'YK0Y4cJOIZAtgrtdvxcgtrJb+6YqJG/hcqbpy2ukrcvcxKznI1sUbfCNCVA/4ZkxfyShb1yMzjdcdcds1lieOnfvlJHAj9aM=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'YK0Y4cJOtrgtrgtrIZAJb+dcsdsc6YqJG/hcqbpy2ukrdcvdvdKznI1sUbfCNCVA/4ZkxfyShb1yMztdvcdvgrtgtrj1lieOnfvlJHAj9aM=', 'x-amz-request-id': 'TCYQS8KBHG76567HGHGEEZQQDQJA', 'date': 'Thu, 27 Apr 2023 15:45:57 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'demo-bucket-creation', 'CreationDate': datetime.datetime(2023, 4, 25, 21, 18, 31, tzinfo=tzutc())}], 'Owner': {'DisplayName': 'k.username', 'ID': '96c7956sdnvc6767e1c14df6054c7c00cdsbvd8a3beb313a541fea8d72c0526e6f670dnviuert6e78822cee8756'}}
	
	
	5. You can run the code from this link as well.
https://github.com/aliasanuj/awsLearning/blob/dev/S3%20bucket.py
![image](https://user-images.githubusercontent.com/40429093/234917131-f8c398d0-d862-4b25-a19d-ac5107cb1301.png)
