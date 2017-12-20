import time

def _do_fusion(raw_data):
    cur_time = (2017, 12, 20, 14, 29, 0, 123456)
    cur_pos = (8.8167359, 53.0571713)
    cur_head = 3.14159
    cur_alt = 5.9
    cur_velo = 10.0
    return (cur_time, cur_pos, cur_head, cur_alt, cur_velo)

def gen_fusion(queue):
    while True:
        raw_data = []
        while not queue.empty():
            raw_data.append(queue.get())
        if raw_data:
            fused_data = _do_fusion(raw_data)
            yield fused_data
        # Wait a moment to avoid hammering the cpu.
        time.sleep(0.1)
