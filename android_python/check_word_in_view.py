
def check_word_in_view(word):
  import xml.etree.ElementTree as ET
  root = ET.fromstring(dump_ui())
  for node in root.iter('node'):
    text = node.attrib['text']
    # if text:
    #   print text
    if word in text:
      return True
  return False

def dump_ui():
  # xml = ''  # For Debug
  # with open('dump.txt', 'r') as fr:
  #  xml = fr. read()
  import subprocess as sp
  return sp.check_output('adb shell uiautomator dump | adb shell cat /sdcard/window_dump.xml | tidy -xml -utf8 -i 2>/dev/null', shell=True).strip()

if __name__ == '__main__':
  import sys
  argvs = sys.argv
  argc = len(argvs)
  if argc != 2:
    print '****Usage: # python {} word'.format(argvs[0])
    sys.exit(1)
  print check_word_in_view(argvs[1])
