import sys
import subprocess as sp


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 tp1BoF.py <executable_path>")
        exit(1)

    exec_name = sys.argv[1]

    buffer_size = 1
    while True:
        buffer = b'a'*buffer_size + b'\n'
        #buffer = b"hello"
        res = sp.run([exec_name], input=buffer, capture_output=True)
        
        if res.returncode == -11:
            print(f"Buffer overflow detected at {buffer_size} bytes")
            break
        elif buffer_size == 1000000:
            print("Buffer overflow not detected")
            break
        else:
            buffer_size += 1
        

if __name__ == "__main__":
    main()