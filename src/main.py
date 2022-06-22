import codecs
from typing import List

import yaml
from jinja2 import Environment, FileSystemLoader

from arguments import Arguments


def read_gantt_template():
    env = Environment(loader=FileSystemLoader('./tmpl', encoding='utf8'))
    return env.get_template('gantt_template.j2')


def read_gantt_style_def() -> str:
    with open('def/style.txt', 'r', encoding='UTF-8') as f:
        return f.read()


def read_members() -> List[str]:
    with codecs.open('conf/members.yml', 'r', 'utf-8') as f:
        config = yaml.safe_load(f)
        return config['member']


def write_gantt_pu(sprint_num: int, content: str):
    file_path = f'out/gantt_sprint{sprint_num}.pu'
    with open(file_path, 'w', encoding='UTF-8') as f:
        f.write(content)
        print(f'Created {file_path}')


if __name__ == '__main__':
    args = Arguments(read_members())
    tmpl = read_gantt_template()
    rendered_contents = tmpl.render(
        start_date=args.start_date,
        style=read_gantt_style_def(),
        sprint_num=args.sprint_num,
        closed_dates=args.closed_dates,
        member_to_tasks=args.member_to_tasks
    )
    write_gantt_pu(args.sprint_num, rendered_contents)
