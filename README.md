# Description
REST API developed in Python 3.
The purpose of this work it's to monitoring and execute a health check in the SO/Services through the Python+REST and export this data to JSON or HTML.

## Default URL path
/metrics
/health

### Configure HOST / PORT
Change the file "webserver.py" in lines 11 and 12.

## Metrics
### URL Default
127.0.0.1:9000/metrics

### Example output
```
{
    "cpu": {
        "cpu count": 4,
        "cpu percent": 58.4
    },
    "memory": {
        "memory available (GB)": 5.789119720458984,
        "memory percent": 62.8
    }
}
```

## Health check
### URL Default
127.0.0.1:9000/health
