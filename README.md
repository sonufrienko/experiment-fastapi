# FastAPI and Amazon Rekognition

![](fastapi.png)

![](amazon-rekognition.png)


## Features

- FastAPI
- Well structured
- API versioning
- Amazon DynamoDB
- Amazon S3 (list objects, put object)
- Amazon Rekognition (image modaration before upload)
- File upload (to local and AWS S3)
- CORS `(soon)`
- Logs `(soon)`
- Dockerfile `(soon)`
- Deploy `(soon)`
- Testing `(soon)`

## Getting Started

```sh
pipenv install
pipenv shell
export AWS_PROFILE=my-profile
export AWS_DEFAULT_REGION=eu-central-1
uvicorn server:app --reload
```

## How to use

```
http http://127.0.0.1:8000/healthcheck
http http://127.0.0.1:8000/v1/countries
http http://127.0.0.1:8000/v1/storage
```

## OpenAPI

Open in browser

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
