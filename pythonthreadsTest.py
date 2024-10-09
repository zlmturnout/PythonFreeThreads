import sys
import time,math
import requests
import threading

def deco_count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_elapse = end_time - start_time
        print(f'Function {func.__name__:*^20} cost: {time_elapse:.4f} s')
        return result
    return wrapper

#@deco_count_time
def find_n_prime(n: int = 10000):
    x = 2
    num = 0
    prime_list = list()
    while True:
        x += 1
        for y in range(2, int(math.sqrt(x)) + 1):
            if x % y == 0:
                break
            else:
                if y == int(math.sqrt(x)):
                    # print(f'find a prime: {x}')
                    prime_list.append(x)
                    num += 1

        # print(f'now check: {x}')
        if num == n:
            # print(prime_list,len(prime_list))
            break
    return prime_list

# 例子：输出 Python 版本
print(f"Python version: {sys.version}")

# 模拟任务
def compute_task():
    total = 0
    for i in range(10**7):
        total += i

# 记录开始时间
start_time = time.time()

# 创建并启动线程
threads = [threading.Thread(target=find_n_prime) for _ in range(100)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# 记录结束时间
end_time = time.time()

# 输出执行时间
print(f"Total execution time for compute_task: {end_time - start_time:.4f} seconds")


def fetch_url():
    response = requests.get('https://baidu.com')
    return response.content

# 记录开始时间
start_time = time.time()

# 创建并启动线程
threads = [threading.Thread(target=fetch_url) for _ in range(200)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# 记录结束时间
end_time = time.time()

# 输出执行时间
print(f"Total execution time for fetch_url: {end_time - start_time:.4f} seconds")

