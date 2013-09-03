#!/bin/env python
" Example Subversion pre-commit hook. "

def command_output(cmd):
  " Capture a command's standard output. "
  import subprocess
  return subprocess.Popen(
      cmd.split(), stdout=subprocess.PIPE).communicate()[0]

def files_changed(look_cmd):
  """ List the files added or updated by this transaction.

"svnlook changed" gives output like:
  U   trunk/file1.cpp
  A   trunk/file2.cpp
  """
  def filename(line):
      return line[4:]
  def added_or_updated(line):
      return line and line[0] in ("A", "U")
  return [
      filename(line)
      for line in command_output(look_cmd % "changed").split("\n")
      if added_or_updated(line)]

def info(look_cmd):
  """ List the author and svn log.

"svnlook info" gives output like:
    sally
    2003-02-22 17:44:49 -0600 (Sat, 22 Feb 2003)
    15
    Rearrange lunch.
  """
  lines = command_output(look_cmd % "info").splitlines()
  return [lines[0], lines[3:]]

  def filename(line):
      return line[4:]
  def added_or_updated(line):
      return line and line[0] in ("A", "U")
  return [
      filename(line)
      for line in command_output(look_cmd % "changed").split("\n")
      if added_or_updated(line)]



def file_contents(filename, look_cmd):
  " Return a file's contents for this transaction. "
  return command_output(
     "%s %s" % (look_cmd % "cat", filename))

def contains_tabs(filename, look_cmd):
  " Return True if this version of the file contains tabs. "
  return "\t" in file_contents(filename, look_cmd)

def check_cpp_files_for_tabs(look_cmd):
  " Check C++ files in this transaction are tab-free. "
  def is_cpp_file(fname):
      import os
      return os.path.splitext(fname)[1] in ".cpp .cxx .h".split()
  cpp_files_with_tabs = [
      ff for ff in files_changed(look_cmd)
      if is_cpp_file(ff) and contains_tabs(ff, look_cmd)]
  if len(cpp_files_with_tabs) > 0:
      sys.stderr.write("The following files contain tabs:\n%s\n"
                       % "\n".join(cpp_files_with_tabs))
  return len(cpp_files_with_tabs)

def main():
  usage = """usage: %prog REPOS TXN

Run pre-commit options on a repository transaction."""
  from optparse import OptionParser
  parser = OptionParser(usage=usage)
  parser.add_option("-r", "--revision",
                    help="Test mode. TXN actually refers to a revision.",
                    action="store_true", default=False)
  errors = 0
  try:
      (opts, (repos, txn_or_rvn)) = parser.parse_args()
      print opts
      look_opt = ("--transaction", "--revision")[opts.revision]
      look_cmd = "svnlook %s %s %s %s" % (
          "%s", repos, look_opt, txn_or_rvn)
      errors += check_cpp_files_for_tabs(look_cmd)
  except:
      parser.print_help()
      errors += 1
  return errors

if __name__ == "__main__":
  import sys
  sys.exit(main())
