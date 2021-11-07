from retrying import retry
import traceback


@retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=5000)
def run():
    print("开始重试")
    return 1 / 0


if __name__ == '__main__':
    run()
