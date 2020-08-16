# FastAPI and Amazon Rekognition

<table>
  <tr>
    <td style="width: 50%;">
      <a href="https://fastapi.tiangolo.com/" target="_blank">
        <img src="./fastapi.png" />
      </a>
    </td>
    <td style="width: 50%;">
      <a href="https://aws.amazon.com/rekognition/" target="_blank">
        <img src="./amazon-rekognition.png" />
      </a>
    </td>
  </tr>
</table>


## Features

- FastAPI
- Well structured
- API versioning
- Amazon DynamoDB
- Amazon S3 (list objects, put object)
- Amazon Rekognition (image modaration before upload)
- File upload (to local and AWS S3)
- Dockerfile
- Deploy `(soon)`
- CORS `(soon)`
- Logs `(soon)`
- Testing `(soon)`

## Getting Started

Run locally

```sh
pipenv install
pipenv shell
export AWS_PROFILE=my-profile
export AWS_DEFAULT_REGION=eu-central-1
uvicorn server:app --reload
```

Run Docker container

```sh
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=...

docker build -t smart-api .

docker run -d \
-p 80:80 \
-e AWS_ACCESS_KEY_ID \
-e AWS_SECRET_ACCESS_KEY \
-e AWS_DEFAULT_REGION \
--name smart-api \
smart-api

http localhost/healthcheck
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
