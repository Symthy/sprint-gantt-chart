import argparse
import datetime
from typing import List


class Arguments:
    def __init__(self, members: List[str]):
        self.__member_to_tasks: dict[str, dict[str, str]] = {}
        self.__parse_arguments()
        self.__input_tasks(members)

    def __parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('sprint', type=int, help='Sprint Number')
        parser.add_argument('-s', '--start', type=str, help='Project state date', default=get_date_now())
        parser.add_argument('-c', '--closed', type=str, help='Closed data (comma-separated input)')
        args = parser.parse_args()
        self.__start_data: str = args.start.strip() if args.start is not None else ""
        self.__sprint_num: int = args.sprint
        self.__closed_dates: List[str] = args.closed.strip().split(',') if args.closed is not None else []

    def __input_tasks(self, members: List[str]):
        print('# Enter the tasks for the member.')
        print('# To proceed to the next member, press Enter without typing anything.')
        for member in members:
            task_id_to_title = {}
            print(f'[{member}]')
            while True:
                task_id = input("Task ID: ").strip()
                if len(task_id) == 0:
                    break
                task_title = input("Task Title: ").strip()
                task_id_to_title[task_id] = task_title
            if len(task_id_to_title) > 0:
                self.__member_to_tasks[member] = task_id_to_title

    @property
    def start_date(self) -> str:
        return self.__start_data

    @property
    def sprint_num(self) -> int:
        return self.__sprint_num

    @property
    def closed_dates(self) -> List[str]:
        return self.__closed_dates

    @property
    def member_to_tasks(self) -> dict[str, dict[str, str]]:
        return self.__member_to_tasks


def get_date_now():
    dt_now = datetime.datetime.now()
    return dt_now.strftime('%Y/%m/%d')
