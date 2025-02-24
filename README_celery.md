# Celery Task Configuration

## 1. Celery Configuration (`tasks.py`)

### Initializing Celery

```python
from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab
import json, time
from datetime import datetime
from apps.config import Config

logger = get_task_logger(__name__)

celery_app = Celery(
    Config.CELERY_HOSTMACHINE,
    backend=Config.CELERY_RESULT_BACKEND,
    broker=Config.CELERY_BROKER_URL
)

celery_app.conf.timezone = 'UTC'
```

### Celery Beat Schedule
A periodic task is scheduled to run every minute:

```python
celery_app.conf.beat_schedule = {
    'run_celery_beat_test_every_minute': {
        'task': 'celery_beat_test',
        'schedule': crontab(minute='*/1'),
        'args': (json.dumps({'test': 'data'}),)
    },
}
```

## 2. Task Definitions

### Regular Task (`celery_test`)

```python
@celery_app.task(name="celery_test", bind=True)
def celery_test(self, task_input):
    task_json = json.loads(task_input)

    logger.info('*** Started')
    logger.info(' > task_json:' + str(task_json))

    task_json['state'] = 'STARTING'
    task_json['info'] = 'Task is starting'
    self.update_state(state='STARTING', meta={'info': 'Task is starting'})
    time.sleep(1)

    task_json['state'] = 'RUNNING'
    task_json['info'] = 'Task is running'
    self.update_state(state='RUNNING', meta={'info': 'Task is running'})
    time.sleep(1)

    task_json['state'] = 'CLOSING'
    task_json['info'] = 'Task is closing'
    self.update_state(state='CLOSING', meta={'info': 'Task is closing'})
    time.sleep(1)

    task_json['state'] = 'FINISHED'
    task_json['info'] = 'Task is finished'
    task_json['result'] = 'SUCCESS'
    self.update_state(state='FINISHED', meta={'info': 'Task is finished'})

    return task_json
```

### Periodic Task (`celery_beat_test`)

```python
@celery_app.task(name="celery_beat_test", bind=True)
def celery_beat_test(self, task_input):
    task_json = {'info': 'Beat is running'}
    return task_json
```

## 3. Flask Route for Testing Tasks (`routes.py`)

A Flask route to trigger the Celery task and return the task ID:

```python
@blueprint.route('/tasks-test')
def tasks_test():
    input_dict = {"data1": "04", "data2": "99"}
    input_json = json.dumps(input_dict)

    task = celery_test.delay(input_json)

    return f"TASK_ID: {task.id}, output: {task.get()}"
```

## 4. Running Celery

### Start the Celery Worker
Run the following command to start the worker:

```bash
celery -A apps.tasks worker --loglevel=info
```

### Start Celery Beat (for periodic tasks)
Run the following command to start Celery Beat:

```bash
celery -A apps.tasks beat --loglevel=info
```

