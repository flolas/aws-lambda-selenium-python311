# aws-lambda-selenium-python311

A minimal example of a AWS Lambda Python 3.11 with Selenium working without layers or container image.


# Build Requirements
* Docker


# Build zip package

```bash
  ./build.sh
```
**NOTE:** must upload in s3 and import from there.

# Lambda tested configuration

* 1GB RAM
* Runtime Python 3.11