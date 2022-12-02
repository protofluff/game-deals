import subprocess

VERSION = str(subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']), 'UTF-8').strip() or '1.0.0'
AUTHOR = 'protofluff'
REDDIT_AUTHOR = '_protofluff_'
APP_ID = 'dev.protofluff.gamedeals'