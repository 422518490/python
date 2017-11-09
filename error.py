import logging

try:
    print("try...")
    r = 10/0
    print("result:",r)
except BaseException as e:
    print("BaseException:",e)
    logging.exception(e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
finally:
    print("finally...")
print("END")