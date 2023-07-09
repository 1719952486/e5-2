import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60
    
    print("开始专注...")
    
    while time.time() < end_time:
        time_left = int(end_time - time.time())
        minutes = time_left // 60
        seconds = time_left % 60
        
        print(f"剩余时间: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
    
    print("\n专注时间结束！")

focus_duration = int(input("请输入专注时长（以分钟为单位）: "))
focus_timer(focus_duration)
