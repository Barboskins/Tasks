import multiprocessing
import os
#
# def do_this(what):
#     whoami(what)
# def whoami(what):
#     print("Process %s says: %s" % (os.getpid(), what))
# if __name__ == "__main__":
#     whoami("I'm the main program")
#     for n in range(4):
#         p = multiprocessing.Process(target=do_this,
#                                     args=("I'm function %s" % n,))
#         p.start()


# import time
#
# def whoami(name):
#     print("I'm %s, in process %s" % (name, os.getpid()))
# def loopy(name):
#     whoami(name)
#     start = 1
#     stop = 1000000
#     for num in range(start, stop):
#         print("\tNumber %s of %s. Honk!" % (num, stop))
#         time.sleep(1)
# if __name__ == "__main__":
#     whoami("main")
#     p = multiprocessing.Process(target=loopy, args=("loopy",))
#     p.start()
#     time.sleep(5)
#     p.terminate()