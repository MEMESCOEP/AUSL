import base64
import os
import subprocess



filename = ""
try:
    filename = sys.argv[1]

except:
    filename = "myprogram.ausl"



def read_input_ausl():
    with open(filename) as f:
        return f.read().strip()

def read_input_runtime():
    with open('ausl_runtime.py') as f:
        return f.read().strip()



print("Input AUSL File Contents: ", read_input_ausl())
print("Input runtime File Contents: ", read_input_runtime())
data = read_input_ausl()
runtime = read_input_runtime()
command = data
runtimeausl = """
command = \"\"\"{}\"\"\"
""".format(command)


open(filename + ".py", 'w').write(runtimeausl + "\n" + runtime)
print("Compiling '" + (filename + ".py") + "'... (THIS WILL TAKE A FEW MINUTES!)")
proc = subprocess.Popen(["python3 -m nuitka --standalone --follow-imports --onefile " + (filename + ".py") + ""], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print("STATUS:", out)
print("Done building '" + (filename + ".bin") + "'.")


