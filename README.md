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
helm install pachyderm pachyderm/pachyderm \
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
pachctl create repo dingo-images -d "Images of the Dingo dog breed"
```

Ingest Data
```sh
pachctl put file dingo-images@main -r -f s3://pachyderm/stanford-dog/images/n02115641-dingo
```

List Data
```sh
pachctl list file dingo-images@main
```

Export Data
```sh
pachctl get file dingo-images@main -r -o ./tmp/dingo-images
```

Create Pipeline
```sh
pachctl create pipeline -f ./edges.json
```

## High Level Architecture

![High Level Architecture](./docs/images/pachyderm-high-level-arch.svg)