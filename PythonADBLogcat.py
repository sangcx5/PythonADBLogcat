import subprocess, sys, shlex

def log_cat(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode('utf-8'))
    rc = process.poll()
    return rc

def main():
    if len(sys.argv) == 1:
        print("Usage:")
        print("python PythonADBLogcat.py com.package.name")
        return
    package_name = sys.argv[1]
    pid = subprocess.run("adb shell pidof -s " + package_name, capture_output=True, shell=True, text=True).stdout
    command = "adb logcat --pid " + pid.strip()
    log_cat(command)


main()
