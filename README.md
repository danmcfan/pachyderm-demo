# Pachyderm Demo


## Links

- [Local Deploy](https://docs.pachyderm.com/latest/getting-started/local-deploy/docker/)
- [Cloud Deploy](https://docs.pachyderm.com/latest/getting-started/cloud-deploy/aws/)
- [Beginner Tutorial](https://docs.pachyderm.com/latest/getting-started/beginner-tutorial/)

## Local Deploy

Command Line Interface
```sh
brew tap pachyderm/tap && brew install pachyderm/tap/pachctl
```

Helm Repository
```sh
helm repo add pachyderm https://helm.pachyderm.com  
helm repo update
```

Helm Install
```sh
helm install pachd pachyderm/pachyderm \
    --set deployTarget=LOCAL \
    --set proxy.enabled=true \
    --set proxy.service.type=LoadBalancer 
```

Connect
```sh
echo '{"pachd_address":"grpc://127.0.0.1:80"}' | \
    pachctl config set context local --overwrite && \
    pachctl config set active-context local
```

Test Connection
```sh
pachctl version
```

## Beginner Tutorial

Create Repo
```sh
pachctl create repo images -d "images of dog breeds"
pachctl create repo labels -d "labels of dog breeds"
```

Ingest Data
```sh
pachctl put file images@master:/ -r -f s3://pachyderm/dogs/images/batch_01/
pachctl put file labels@master:/ -r -f s3://pachyderm/dogs/labels/batch_01/
```

List Data
```sh
pachctl list file images@master
pachctl list file labels@master
```

Export Data
```sh
pachctl get file images@master:/ -r -o ./tmp/images/
pachctl get file labels@master:/ -r -o ./tmp/labels/
```

Create Pipeline
```sh
pachctl create pipeline -f ./bbox.json
```

## High Level Architecture

![High Level Architecture](./docs/images/pachyderm-high-level-arch.svg)