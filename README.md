# piClustering


***

## Dockerfile

This can be used to build the docker images necessary to run the test app

### Build the image

```
docker build -t welshsean/testapp:latest .
```

### Run the image as a Daemon

Note that you need to pass AWS region and AWS access key details

```
docker run -d -e AWS_DEFAULT_REGION='eu-west-2' -e AWS_ACCESS_KEY_ID='your key id' -e AWS_SECRET_ACCESS_KEY='your key'  welshsean/testapp:latest
```
