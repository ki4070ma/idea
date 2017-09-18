
from controller import Controller
from checker import check_word_in_view, check_focused_word

def test_more_from_settings():
  ctrl = Controller()
  ctrl.start_settings()
  assert check_word_in_view('Device connection')
  ctrl.execute('DOWN DOWN')
  assert check_focused_word('More')

if __name__ == '__main__':
  test_more_from_settings()
