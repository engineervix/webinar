import gunicorn

# Tell gunicorn to run our app
wsgi_app = "webinar.wsgi:application"

# Replace gunicorn's 'Server' HTTP header to avoid leaking info to malicious actors
gunicorn.SERVER = ""

# Restart gunicorn worker processes every 1200-1250 requests
max_requests = 1200
max_requests_jitter = 50

# Log to stdout
accesslog = "-"
loglevel = "info"
# Use X-Forwarded-For header to get real client IP instead of Nginx proxy IP
access_log_format = '%({X-Forwarded-For}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Time out after 25 seconds (notably shorter than Heroku's)
# timeout = 25

# Workers can be overridden by `$WEB_CONCURRENCY`
workers = 5

# Load app pre-fork to save memory and worker startup time
preload_app = True
