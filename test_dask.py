import time
import psutil
import numpy as np
import dask.array

def main():
    start = time.time()
    result = np.arange(10**7).sum()
    ex = time.time() - start
    print('execution time =', ex)

    start = time.time()
    work = dask.array.arange(10**7).sum()
    result = work.compute()
    ex = time.time() - start
    print('execution time =', ex)


    N_physical_cores = psutil.cpu_count(logical=False)
    N_logical_cores = psutil.cpu_count(logical=True)
    print(f"The number of physical/logical cores is {N_physical_cores}/{N_logical_cores}")


    x = []
    for n in range(1, 9):
        start = time.time()
        dask.array.arange(5*10**7).sum().compute(num_workers=n)
        end = time.time()
        ellapsed = end - start
        x.append(ellapsed)
        print(ellapsed)

if __name__ == "__main__":
    main()
