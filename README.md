# requests-dashboard

This is a simple web application that shows requests for an api over time. 


## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Build and run

`cd` into project directory and run:
```
docker-compose up --build
```
## Usage
There are 4 different endpoints for `GET`, `POST`, `PUT` and `DELETE` requests. They are
 - http://127.0.0.1:8000/api/get/
 - http://127.0.0.1:8000/api/post/
 - http://127.0.0.1:8000/api/put/
 - http://127.0.0.1:8000/api/delete/

respectively. You can use a command line tool like [`httpie`](https://httpie.io/) to perform requests. Example:
```
http PUT http://127.0.0.1:8000/api/put/
http http://127.0.0.1:8000/api/get/
```


The dashboard is available at http://127.0.0.1:8080. Note that its port is different even though it's same application. You can continue using port `8000` if you want but it will make dashboard to freeze when you perform requests because the application `sleep`s before responding to the requests.

## Sample Screenshots
![alt text](https://i.imgur.com/YxenkyO.png "Dashboard")
![alt text](https://i.imgur.com/5t26ODP.png "Dashboard")

## Notes
- Secret key: gAAAAABgUJqwMzZTO_g2GqgORZD_LRGgIDVhfkX4Tn4pqnkx9awMU2pwZywJkcm7CmV791oNFeeiKp1WEruAHnEOBqqdS89JAzMfAvInFBaWnT5CzluI1kBElaLRUVc6U9S4VxfpJi9sZ0PCrfwaFrKzZzFENbMrG8SiAIsWPh0QEVgiQApPfKv_CcBhn-pVPFzi7gocBpn3

- Getting the challenge content: You can find the code that I wrote to get the challenge content inside `challenge_content`. It's is not the best code but it gets the job done and I won't ever use it anymore so it's OK.
