# Pachyderm Demo

## Links

- [Local Deploy](https://docs.pachyderm.com/latest/getting-started/local-deploy/docker/)
- [Cloud Deploy](https://docs.pachyderm.com/latest/getting-started/cloud-deploy/aws/)
- [Beginner Tutorial](https://docs.pachyderm.com/latest/getting-started/beginner-tutorial/)

## Local Deploy

Command Line Interface
```sh
brew tap pachyderm/tap && brew install pachyderm/tap/pachctl@2.4
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