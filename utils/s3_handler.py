import os
import uuid
import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION")
BUCKET_NAME = "resume-analyzer-user-files"

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def generate_session_id():
    return str(uuid.uuid4())

def upload_file_to_s3(local_path: str, s3_key: str):
    s3.upload_file(local_path, BUCKET_NAME, s3_key)
    print(f"Uploaded {local_path} to {s3_key}")

def download_file_from_s3(s3_key: str, local_path: str):
    s3.download_file(BUCKET_NAME, s3_key, local_path)
    print(f"Downloaded {s3_key} to {local_path}")

def get_default_paths(session_id: str):
    return {
        "resume_local": "test_data/Ali_Boussi_Resume_2025.pdf",
        "resume_s3": f"test_data/uploads/{session_id}/Ali_Boussi_Resume_2025.pdf",
        "resume_downloaded": f"test_data/local_{session_id}_Ali_Boussi_Resume_2025.pdf",
    }