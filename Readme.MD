# Stimulating Memory Leak

### Install the requirements
```
    pip install -r requirements.txt
```

### Run in Flask
- Run the server in one terminal
```
    mprof run --multiprocess python flask_app.py
```
- Run s.py
```
    python s.py
``` 
- After s.py is done, run
```
    mprof plot --flame
```

### Run in Fastapi with uvicorn
- Run the server in one terminal
```
    mprof run --multiprocess uvicorn uvicorn_app:app
```
- Run s.py
```
    python s.py
``` 
- After s.py is done, run
```
    mprof plot --flame
```

### Run in Fastapi with hypercorn
- Run the server in one terminal
```
    mprof run --multiprocess hypercorn hypercorn_app:app
```
- Run s.py
```
    python s.py
``` 
- After s.py is done, run
```
    mprof plot --flame
```