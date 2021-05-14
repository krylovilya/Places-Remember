# Places-Remember

[![Coverage Status](https://coveralls.io/repos/github/krylovilya/Places-Remember/badge.svg?branch=master)](https://coveralls.io/github/krylovilya/Places-Remember?branch=master)

https://placesremember.website

Delete and generate test places:
`/place/delete_and_generate_test_places/`

### First start

```
# Add to ~/.bashrc

export secret_KEY='***'
export YANDEX_API_KEY='***'
export SOCIAL_AUTH_VK_OAUTH2_KEY='***'
export SOCIAL_AUTH_VK_OAUTH2_SECRET='***'
export SOCIAL_AUTH_FACEBOOK_KEY='***'
export SOCIAL_AUTH_FACEBOOK_SECRET='***


$ source ~/.bashrc
$ git clone https://github.com/krylovilya/Places-Remember.git && cd Places-Remember/
$ chmod +x bin/*
$ ./bin/dev_build
$ ./bin/dev_up
$ ./bin/makemigrations
$ ./bin/migrate
$ ./bin/bash
[container]$ python manage.py createsuperuser
```


### Scripts

* bash - bash inside the django application container
* shell - python shell inside the django application container
* dev_build - build containers for local development
* prod_build - build containers for production development
* dev_up - start containers for local development
* prod_up - start containers for production development
* makemigrations - run makemigrations inside the django application container
* migrate - run migrate inside the django application container
* kill - kill all containers
