import sys

def get_user_input():
    try:
        target_pos, target_time = sys.argv[1:]
    except ValueError:
        target_pos = '57,8'
        target_time = '2018-12-18_06:12:38.123456'
    return (target_pos, target_time)
