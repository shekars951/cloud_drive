import boto3
from botocore.client import Config


ACCESS_KEY = 'AKIAUU76WWZNK4W43VWD'
SECRET_KEY = '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'


def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response


def show_image(bucket):
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY,
                             config=Config(signature_version='s3v4'), region_name='ap-south-1')
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object',
                                                             Params={'Bucket': bucket, 'Key': item['Key']},
                                                             ExpiresIn=100)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    # print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls
