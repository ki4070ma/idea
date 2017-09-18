import subprocess as sp

class Controller(object):

  CMD = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'CENTER']

  def __init__(self):
    pass  # TODO Should have adb name

  def execute(self, steps):
    steps = steps.split()
    self.__check_steps(steps)
    for step in steps:
      print '****Executed {}'.format(step)
      sp.check_output('adb shell input keyevent DPAD_{}'.format(step).split())

  def start_settings(self):
    sp.call('adb shell am start -n com.android.settings/.Settings'.split())

  def am_start(self, package):
    sp.call('adb shell am start -n {}'.format(package).split())

  def cap(self, str=''):
    from time import localtime, strftime
    sp.call('adb shell screencap -p /sdcard/screen.png'.split())
    sp.call('adb pull /sdcard/screen.png ./screen_{}_{}.png'.format(strftime("%Y%m%d%H%M%S", localtime()), str).split())
    sp.call('adb shell rm /sdcard/screen.png'.split())

  def __check_steps(self, steps):
    for cmd in steps:
      if cmd not in self.CMD:
        raise SystemError('{} is unavailable.'.format(cmd))

if __name__ == '__main__':
  controller = Controller()
  controller.execute('DOWN DOWN DOWN')
  # controller.start_settings()
  # controller.am_start('com.android.settings/.Settings')
  # controller.cap('Settings')
