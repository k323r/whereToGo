import sys

def sonar_ping(target_heading, target_velocity, estimated_toa):
    sys.stdout.write(
        'sonar_ping: %s %s %s\n\n' % (
            str(target_heading),
            str(target_velocity),
            str(estimated_toa)
        )
    )
