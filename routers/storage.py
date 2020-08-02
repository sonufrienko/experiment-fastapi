from fastapi import APIRouter, File, UploadFile
import boto3

router = APIRouter()
s3 = boto3.client("s3")
rekognition = boto3.client("rekognition")
BUCKET_NAME = "itreko"


@router.get("/storage")
async def read_storage():
    objects = []

    response = s3.list_objects(Bucket=BUCKET_NAME, MaxKeys=100,)

    for obj in response["Contents"]:
        objects.append(
            {
                "key": obj["Key"],
                "last_modified": obj["LastModified"],
                "size": obj["Size"],
            }
        )

    return objects


@router.post("/storage/upload")
async def create_upload_file(file: UploadFile = File(...)):
    image_binary_content = await file.read()
    filename = file.filename

    labels = detect_moderation_labels(image_binary_content)
    passed_moderation = len(labels) == 0
    if passed_moderation:
        save_to_disk(image_binary_content, filename)
        upload_to_s3(image_binary_content, filename, BUCKET_NAME)
        return {"success": True}
    else:
        print(f"UNSAFE FILE >>> {filename}, LABELS: ", ", ".join(labels))
        return {"success": False, "error": "Inappropriate Content"}


def detect_moderation_labels(image_binary_content):
    response = rekognition.detect_moderation_labels(
        Image={"Bytes": image_binary_content}, MinConfidence=40
    )

    labels = []
    for label in response["ModerationLabels"]:
        labels.append(label["Name"])

    return labels


def save_to_disk(file_content, file_name):
    with open(f"upload/{file_name}", "w+b") as f:
        f.write(file_content)


def upload_to_s3(file_content, file_name, bucket_name):
    response = s3.put_object(Body=file_content, Bucket=bucket_name, Key=file_name)
    is_success = response["ResponseMetadata"]["HTTPStatusCode"] == 200
    return is_success

