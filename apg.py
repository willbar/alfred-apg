# encoding: utf-8

import sys
import subprocess
from workflow import Workflow

def main(wf):
  output = subprocess.check_output(["/usr/local/bin/apg", "-m", sys.argv[1], "-M", sys.argv[2]])
  passwords = output.splitlines()
  for password in passwords:
    wf.add_item(title=password,valid=True,arg=password)

	# Send the results to Alfred as XML
  wf.send_feedback()

if __name__ == u"__main__":
  wf = Workflow()
  sys.exit(wf.run(main))