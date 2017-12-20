import sys

def display(target_heading, target_velocity, estimated_toa):
    sys.stdout.write(
        'display: %s %s %s\\n\n' % (
            str(target_heading),
            str(target_velocity),
            str(estimated_toa)
        )
    )
