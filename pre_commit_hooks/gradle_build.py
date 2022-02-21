from __future__ import print_function

import argparse
from typing import Optional
from typing import Sequence

from pre_commit_hooks.util import cmd_output, run_gradle_wrapper_task, run_gradle_task


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
        '--exclude-task', action='store', dest='exclude_task',
        help='Exclude given task during the command.'
    )
    args = parser.parse_args(argv)

    skip_test_arg = f' -x {args.exclude_task}' if args.exclude_task else '';
    task = 'build' + skip_test_arg

    if args.wrapper:
        return run_gradle_wrapper_task(args.output, task)
    else:
        return run_gradle_task(args.output, task)


if __name__ == '__main__':
    exit(main())
