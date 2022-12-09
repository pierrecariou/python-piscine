import time

def ft_progress(lst):
    time_start = time.perf_counter()
    size = len(lst)
    inc = 1
    for elem in lst:
        ratio = int((inc/size)*100)
        progress_bar = "="*int((ratio/10)*2)+">"
        elapsed_time = time.perf_counter() - time_start
        estimated_remaining_time = 0 if ratio == 0 else ((100/ratio) * elapsed_time) - elapsed_time
        print(f"ETA: {estimated_remaining_time:0.2f}s [ {ratio}%][{progress_bar.ljust(21, ' ')}] {inc}/{size} | elapsed time {elapsed_time:0.2f}s", end="\r")
        yield elem
        inc+=1

def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)

if __name__ == '__main__':
    main()
