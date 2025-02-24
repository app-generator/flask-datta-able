# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json, time
from datetime import datetime

from apps.config import *

from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab

logger = get_task_logger(__name__)

celery_app = Celery(Config.CELERY_HOSTMACHINE, backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL)


celery_app.conf.beat_schedule = {
    'run_celery_beat_test_every_minute': {
        'task': 'celery_beat_test',
        'schedule': crontab(minute='*/1'),  # Runs every 1 minute
        'args': (json.dumps({'test': 'data'}),)
    },
}
celery_app.conf.timezone = 'UTC'


# task used for tests
@celery_app.task(name="celery_test", bind=True)
def celery_test( self, task_input ):

    task_json = json.loads( task_input )

    logger.info( '*** Started' )
    logger.info( ' > task_json:' + str( task_json ) )

    task_json['result'] = 'NA'
    task_json['ts_start'] = datetime.now()

    # get current task id
    task_id = celery_app.current_task.request.id

    # ######################################################
    # Task is STARTING (prepare the task)

    # Update Output JSON
    task_json['state'] = 'STARTING'
    task_json['info'] = 'Task is starting'

    self.update_state(state='STARTING',
                      meta={ 'info':'Task is starting' })

    time.sleep(1) 

    # ######################################################
    # Task is RUNNING (execute MAIN stuff)

    # Update Output JSON
    task_json['state'] = 'RUNNING'
    task_json['info'] = 'Task is running'

    self.update_state(state='RUNNING',
                      meta={ 'info':'Task is running' })

    time.sleep(1)

    # ######################################################
    # Task is CLOSING (task cleanUP)

    # Update Output JSON
    task_json['state'] = 'CLOSING'
    task_json['info'] = 'Task is closing'

    self.update_state(state='CLOSING',
                    meta={ 'info':'Task is running the cleanUP' })

    task_json['ts_end'] = datetime.now()

    time.sleep(1) 

    # ######################################################
    # Task is FINISHED (task cleanUP)

    # Update Output JSON
    task_json['state'] = 'FINISHED'
    task_json['info'] = 'Task is finished'
    task_json['result'] = 'SUCCESS'

    self.update_state(state='FINISHED',
                    meta={ 'info':'Task is finisled' })    

    return task_json



@celery_app.task(name="celery_beat_test", bind=True)
def celery_beat_test( self, task_input ):
    task_json = {'info': 'Beat is running'}
    return task_json