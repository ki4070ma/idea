import subprocess as sp

class Controller(object):

  CMD = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'CENTER']

  def __init__(self):
    pass  # TODO Should have adb name

  def execute(self, steps):
    self.__check_steps(steps)
    for step in steps:
      sp.check_output('adb shell input keyevent DPAD_{}'.format(step).split())

  def __check_steps(self, steps):
    for cmd in steps:
      if cmd not in self.CMD:
        raise SystemError('{} is unavailable.'.format(cmd))

if __name__ == '__main__':
  controller = Controller()
  controller.execute(['DOWN', 'DOWN', 'DOWN'])
