import boto3
session= boto3.Session(profile_name="default")

ecr_client=session.client('ecr')
repository = "fastapi-monitoring-repo"
response = ecr_client.create_repository(repositoryName=repository)

repository_uri =response['repository']['repositoryUri']

print(repository_uri)

