#!/bin/sh

if [ "${TRAVIS_BRANCH}" == "staging" ]
then
  # Install and set up awscli
  curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
  unzip awscli-bundle.zip
  ./awscli-bundle/install -b ~/bin/aws
  export PATH=~/bin:${PATH}

  # Add AWS_ACCOUNT_ID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
  aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_REGISTRY}

  # Build and push API image
  docker build ./api -t ${AWS_REGISTRY}/docker-ci-demo-api:staging -f ./api/Dockerfile
  docker push ${AWS_REGISTRY}/docker-ci-demo-api:staging
fi
