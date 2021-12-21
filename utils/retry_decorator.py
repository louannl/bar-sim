def retry_input(func, max_tries=3):
    def inner(*args, **kwargs):
        for i in range(max_tries):
            try:
                return func(*args, **kwargs)
            except (KeyError, ValueError):
                print("\n ----- Input value is invalid ----- \n")
                if i == (max_tries - 1):
                    print("----- Max retries exceeded, exiting Game -----")
                    exit()
                continue
    return inner
