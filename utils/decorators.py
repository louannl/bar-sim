def retry_input(func, max_tries=3):
    def inner(*args, **kwargs):
        for i in range(max_tries):
            try:
                func(*args, **kwargs)
                break
            except (KeyError, ValueError) as e:
                print("\n ----- Input value is invalid ----- \n")
                if i == max_tries:
                    print("----- Max retries exceeded, exiting Game -----")
                    raise e
                continue
    return inner
