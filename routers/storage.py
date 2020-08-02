from fastapi import APIRouter
import boto3

router = APIRouter()
s3 = boto3.resource("s3")


@router.get("/storage")
async def read_storage():
    buckets = []
    for bucket in s3.buckets.all():
        buckets.append({"name": bucket.name})
    return buckets

