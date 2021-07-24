try:
    i = 1/0
except RuntimeError as r:
    print(r)
except Exception as e:
    print(e)
except RuntimeWarning as r:
    print(r)
finally:
    print("end")
