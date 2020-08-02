from fastapi import APIRouter
import boto3
from boto3.dynamodb.conditions import Key, Attr

router = APIRouter()
dynamodb = boto3.resource("dynamodb")
dictionary_table = dynamodb.Table("Dictionary")


@router.get("/countries")
async def read_countries():
    response = dictionary_table.query(KeyConditionExpression=Key("pk").eq("country"))
    items_raw = response["Items"]
    items = []

    for item in items_raw:
        items.append(
            {
                "code": item["sk"],
                "name": item.get("name", ""),
                "native": item.get("native", ""),
                "phone": item.get("phone", ""),
            }
        )

    return items

