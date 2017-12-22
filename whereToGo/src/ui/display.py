import sys

def display(
        target_heading,
        target_distance,
        target_time_left,
        target_velocity,
        estimated_duration,
        estimated_toa):
    sys.stdout.write(
'''display:
    %s %s
    %s %s
    %s %s
    %s %s
    %s %s
    %s %s
'''        % (
            'target_heading    ', str(target_heading),
            'target_distance   ', str(target_distance),
            'target_time_left  ', str(target_time_left),
            'target_velocity   ', str(target_velocity),
            'estimated_duration', str(estimated_duration),
            'estimated_toa     ', str(estimated_toa)
        )
    )
