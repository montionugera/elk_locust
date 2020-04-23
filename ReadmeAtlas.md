# Atlas - Kaidee's Backend for Frontend

---

## Introduction

Atlas work as business logic layer, it decide result base on parameter it got.


## Table of Contents
1. [Route architecture](#route-architeccture)
2. [Prerequisite](#prerequisite)
2. [Develop](#develop)

### Route architecture

`GET /:resource/:id`: to get detail of the `resource` by `id`

`POST /:resource/:action`: to do an `action` with the `resource`

`POST /:resource/:id/:action`: to do an `action` with the `resource` by `id`

## Prerequisite

- python 3.8

## Develop

1. git clone


    ```
    # git clone git@github.com:teamkaidee/atlas-api.git
    ```

2. install depedencies


    ```
    # pip install -r dependencies/requirements-dev.txt
    ```

3. set PYTHONPATH


    ```
    # export PYTHONPATH=`pwd`
    ```

4. start service


    ```
    # python atlas/route/routing.py
    ```
    OR
    ```
    PYTHONPATH=`pwd` python atlas/route/routing.py
    ```

## Run Test

```
./scripts/run_tests.sh
```

if error try to upgrade `libcouchbase`

```
brew upgrade libcouchbase
```
