Dockerator
==========

Dockerator is a tool for configuring and managing Docker containers.
You can easily have a common configuration for all containers, containers with the same image and for a specific container
and permit to overload parameters.
Also, it's possible to start / stop / reload containers with initscript or by command line.


Containers configuration
------------------------

1. Same configuration for all containers (dockerator.yml):
  ```yml
  general:
    cid_file: '/run/dockerator/%(DOCKER_NAME)s.cid'
    container_restart: always
    docker_url: 'tcp://127.0.0.1:2375'
  environment:
    TZ: Europe/Paris
  volumes:
    '/var/log/dockerator/docker/%(DOCKER_NAME)s/':
      destination: /var/log/
      mode: rw
    '/var/run/mysqld/':
      destination: /var/run/mysqld/
      mode: rw
  ```

2. Common configuration for containers with the same image (e.g.: image.d/php-fpm_5.6.yml):
  ```yml
  general:
    host_ip: 127.0.0.1
    container_port: 9000
    image: 'docker-registry.example.org/php-fpm:5.6'
  volumes:
    '/etc/dockerator/%(DOCKER_NAME)s/config/php_conf.d/*':
      destination: /etc/php5/fpm/conf.d/
      mode: ro
      glob: true
    '/etc/dockerator/%(DOCKER_NAME)s/config/fpm_pool.d/':
      destination: /etc/php5/fpm/pool.d/
      mode: rw
    '/srv/php-fpm/%(DOCKER_NAME)s': '/var/run/php-fpm'
  ```

3. Configuration for a specific container (e.g.: conf.d/foobar.yml):
  ```yml
  general:
    name: fpm_foobar
    image_cfg_file: 'php-fpm_5.6.yml'
    host_port: 9004
  environment:
    PHP_USER_UID: 10000
    PHP_USER_GID: 10000
  ports:
    '%(container_port)s': '0.0.0.0:%(host_port)s'
    '%(container_port)s': '%(host_ip)s:8080'
  volumes:
    '/var/www/foobar.com/': '/var/www/foobar.com/'
  ```

Actually, there are four variables that you can use in configuration files:
  - DOCKER_NAME (e.g. fpm_foobar)
  - container_port (e.g. 9000)
  - host_ip (e.g. 127.0.0.1)
  - host_port (e.g. 9004)


Dockerator command line
-----------------------
```sh
Usage: dockerator [options] [action]

Options:
  -h, --help            show this help message and exit
  -a ACTION             Choice action on one or many containers:
                        create, kill, list, reload, remove, restart, run,
                        start, status, stop
  -c CONFFILE           Use configuration file <conffile> instead of
                        /etc/dockerator/dockerator.yml
  --configs-dir=CONFSDIR
                        Use configuration directory <confsdir> instead of
                        /etc/dockerator/conf.d
  -f                    Force
  --image-name=IMGNAME  Choice container by image
  --image-configs-dir=IMGCONFSDIR
                        Use configuration directory <imgconfsdir> for images
                        instead of /etc/dockerator/image.d
  -n NAME               Choice container by name
  --logfile=LOGFILE     Use log file <logfile> instead of
                        /var/log/dockerator/dockerator.log
  -l LOGLEVEL           Emit traces with LOGLEVEL details, must be one of:
                        critical, error, warning, info, debug
```

## Actions:

### create:
* All containers:
```sh
$ dockerator create
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 create
```
* Container by name:
```sh
$ dockerator -n fpm_foobar create
```

### kill:
* All containers:
```sh
$ dockerator kill
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 kill
```
* Container by name:
```sh
$ dockerator -n fpm_foobar kill
```

### list:
* All containers:
```sh
$ dockerator list
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 list
```
* Container by name:
```sh
$ dockerator -n fpm_foobar list
```

### reload (stop -> remove -> create -> start):
* All containers:
```sh
$ dockerator reload
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 reload
```
* Container by name:
```sh
$ dockerator -n fpm_foobar reload
```

### remove:
* All containers:
```sh
$ dockerator remove
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 remove
```
* Container by name:
```sh
$ dockerator -n fpm_foobar remove
```

### restart (stop -> start):
* All containers:
```sh
$ dockerator restart
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 restart
```
* Container by name:
```sh
$ dockerator -n fpm_foobar restart
```

### run (create -> start):
* All containers:
```sh
$ dockerator run
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 run
```
* Container by name:
```sh
$ dockerator -n fpm_foobar run
```

### start:
* All containers:
```sh
$ dockerator start
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 start
```
* Container by name:
```sh
$ dockerator -n fpm_foobar start
```

### status:
* All containers:
```sh
$ dockerator status
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 status
```
* Container by name:
```sh
$ dockerator -n fpm_foobar status
```

### stop:
* All containers:
```sh
$ dockerator stop
```
* Containers by image:
```sh
$ dockerator --image-name=docker-registry.example.org/php-fpm:5.6 stop
```
* Container by name:
```sh
$ dockerator -n fpm_foobar stop
```


Installation
------------

python setup.py install


Requirements
------------

* python2.7
* docker-py 1.6.0
* pyyaml


License
-------

Dockerator is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) for details
