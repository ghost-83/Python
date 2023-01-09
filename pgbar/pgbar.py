from progress.bar import ChargingBar, IncrementalBar
import time


def bar(numb):
    pbar = ChargingBar('Progress', max=numb)
    for i in range(numb):
        pbar.next()
        time.sleep(0.2)
    pbar.finish()


def bar_too(numb):
    with IncrementalBar('Progress', max=numb) as pbar:
        for i in range(numb):
            pbar.next()
            time.sleep(0.2)


if __name__ == '__main__':
    bar(5342)
    bar_too(4357)
