from fastapi import APIRouter
import boto3

router = APIRouter()
s3 = boto3.client("s3")
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


