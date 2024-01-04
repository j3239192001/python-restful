### Build image
```
docker build -t py37-flask203:0.0.1 .
```
### Run application
```
docker run -d -p 8080:8080 py37-flask203:0.0.1
```