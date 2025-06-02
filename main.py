from utils import generate_session_id, upload_file_to_s3, download_file_from_s3, get_default_paths, extract_text_from_pdf

if __name__ == "__main__":
    session_id = generate_session_id()
    paths = get_default_paths(session_id)

    # Upload resume to S3
    upload_file_to_s3(paths["resume_local"], paths["resume_s3"])

    # Download resume from S3 to a new file
    download_file_from_s3(paths["resume_s3"], paths["resume_downloaded"])

    # Extract text from the downloaded PDF
    resume_text = extract_text_from_pdf(paths["resume_downloaded"])
    print("Extracted Resume Text Preview:")
    print(resume_text[:1000])

