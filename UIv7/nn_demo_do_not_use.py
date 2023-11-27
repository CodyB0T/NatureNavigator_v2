import multiprocessing

# Define a list of script names to run
script_names = ["gui.py", "bme280test.py", "gps.py"]


def run_script(script_name):
    import subprocess

    subprocess.run(["python", script_name])


if __name__ == "__main__":
    processes = []

    # Create a process for each script in the list
    for script_name in script_names:
        process = multiprocessing.Process(target=run_script, args=(script_name,))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All scripts have finished executing.")
