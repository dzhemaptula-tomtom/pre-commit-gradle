from __future__ import print_function

import argparse
from typing import Optional
from typing import Sequence

from pre_commit_hooks.util import run_gradle_wrapper_task, run_gradle_task


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w', '--wrapper', action='store_true',
        help='Runs commands using gradlew. Requires gradle wrapper configuration within the project.'
    )
    parser.add_argument(
        '-o', '--output', action='store_true',
        help='Prints the output of all executed gradle commands.'
    )
    parser.add_argument(
        '--exclude-tasks', action='store', dest='exclude_tasks', nargs='+', default=[],
        help='Exclude given task during the command. eg: test,integTest,compile'
    )
    args = parser.parse_args(argv)

    task = 'check'

    for arg_exclude_task in args.exclude_tasks.split(","):
        task += f" -x {arg_exclude_task}"

    if args.wrapper:
        return run_gradle_wrapper_task(args.output, task)
    else:
        return run_gradle_task(args.output, task)


if __name__ == '__main__':
    exit(main())
