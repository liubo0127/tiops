# tiops

## Install dependency packages

`pip install yaml-config IPy`

## Edit configuration

> template: `topology.yaml.template`

```yaml
- pd_servers:         # Service group
    pd1:              # A single instance
      ip: 10.0.1.11   # Host ip address
      pd_client_port: 2379
      pd_peer_port: 2380
      deploy_dir: /home/tidb/deploy
    pd2:
      ip: 10.0.1.12
    pd3:
      ip: 10.0.1.13
...
```

## Operation guide

### Initialize the management machine

- `./tiops init -v ${version} -n ${cluster_name}`

> Note:
>
> For example: ./tiops init -v 3.0.3 -n tidb-cluster
> For details please execute `./tiops init -h`

### Initialize the cluster machine

- `./tiops init_network -p ${root_password} -i ${cluster_ip_list} -P ${ssh_port}`
- `./tiops init_host -p ${root_password} -i ${cluster_ip_list} -P ${ssh_port}`

> Note:
>
> For example:
> `./tiops init_network -p 'tidbtest!@#' -i 10.0.1.11,10.0.1.12,10.0.1.13 -P 22`
> `./tiops init_host -p 'tidbtest!@#' -i 10.0.1.11,10.0.1.12,10.0.1.13 -P 22` 
> For details please execute `./tiops init_network -h` and `./tiops init_host -h`

### Deploy TiDB cluster

- `./tiops deploy -c ${config} -n ${cluster_name} -d ${deploy_dir} -p ${parallel} -b ${True/False}`

> Note:
> 
> For example:
> `./tiops deploy -c ./topology.yaml -n tidb-cluster -d /home/tidb/deploy -p  5 -b False`
> For details please execute `./tiops deploy -h`

### Start/Stop TiDB cluster

- `./tiops start -n ${cluster_name} -b ${True/False} -p ${parallel}`

> Note:
>
> For example:
> `./tiops start -n tidb-cluster -b False -p 5`
> `./tiops stop -n tidb-cluster -b False -p 5`
> For details please execute `./tiops start -h` and `./tiops stop -h`