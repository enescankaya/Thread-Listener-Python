import psutil

def print_threads_info(pid):
    try:
        # PID'ye ait işlem bilgisini al
        process = psutil.Process(pid)
        
        # İşlem adı ve diğer temel bilgileri yazdır
        print(f"Process Name: {process.name()}")
        print(f"PID: {pid}")
        print(f"Thread Count: {process.num_threads()}")
        print("-" * 40)

        # Thread bilgilerini al
        threads = process.threads()
        for thread in threads:
            print(f"Thread ID: {thread.id}")
            print(f"User Time: {thread.user_time:.2f} sec")
            print(f"System Time: {thread.system_time:.2f} sec")
            print("-" * 40)
    except psutil.NoSuchProcess:
        print(f"No process found with PID: {pid}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Kullanıcıdan PID al
    try:
        pid = int(input("Enter the PID of the process: "))
        print_threads_info(pid)
    except ValueError:
        print("Please enter a valid PID.")
