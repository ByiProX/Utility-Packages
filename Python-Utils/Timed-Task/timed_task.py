# -*- coding: utf-8 -*-
import threading
import logging
import time
from models_v2.base_model import BaseModel, CM
from configs.config import TIMED_BATCH_SENDING_INTERVAL, BATCH_SEND_TASK_STATUS_3, BATCH_SEND_TASK_STATUS_4
from core_v2.send_msg import send_msg_to_android
from configs.config import SUCCESS, UserBotR, BatchSendTask

logger = logging.getLogger('main')


class TimedTaskThread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.go_work = True

    def run(self):
        logger.info(u"Start thread id: %s." % str(self.thread_id))
        while self.go_work:
            # start_time = int(time.time())
            tasks = BaseModel.fetch_all("batch_send_task", "*",
                                        where_clause=BaseModel.and_(
                                            ["<", "send_time", int(time.time()) + TIMED_BATCH_SENDING_INTERVAL],
                                            [">", "send_time", int(time.time())],
                                            ["=", "is_deleted", 0]),
                                        order_by=BaseModel.order_by({"send_time": "ASC"})
                                        )

            if len(tasks) == 0:
                time.sleep(60)
                continue
            # print tasks
            while True:
                try:
                    task = tasks.pop(0)
                    cur_time = int(time.time())
                    send_time = task.send_time
                    time.sleep(send_time - cur_time)

                    # 传给安卓发送
                    # batch_send_task = CM(BatchSendTask)
                    ubr = BaseModel.fetch_one(UserBotR, '*',
                                              where_clause=BaseModel.where_dict({"client_id": task.client_id}))

                    status = send_msg_to_android(ubr.bot_username, task.content_list, task.chatroom_list)
                    task.send_time_real = int(time.time())
                    if status == SUCCESS:
                        logger.info(u"任务发送成功, client_id: %s." % task.client_id)
                        task.status = BATCH_SEND_TASK_STATUS_3
                        task.save()
                    else:
                        logger.info(u"任务发送失败, client_id: %s." % task.client_id)
                        task.status = BATCH_SEND_TASK_STATUS_4
                        task.save()
                except IndexError:
                    break
            # end_time = int(time.time())
            # time.sleep(TIMED_BATCH_SENDING_INTERVAL - (end_time - start_time))
            # time.sleep(5)

    def stop(self):
        logger.info(u"停止进程")
        self.go_work = False


timed_batch_sending_task_thread = TimedTaskThread(thread_id='timed_batch_sending_task')
