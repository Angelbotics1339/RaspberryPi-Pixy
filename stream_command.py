import subprocess
from networktables import NetworkTable 
p = subprocess.Popen("sudo ~/pixycam_nt/pixy/build/hello_pixy/hello_pixy", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
retcode = p.poll() #returns None while subprocess is running
NetworkTable.setIPAddress("roborio-1339-frc.local")
NetworkTable.setClientMode()
NetworkTable.initialize()
sd = NetworkTable.getTable("SmartDashboard")

while True:
    line = p.stdout.readline()
    if (len(line.split(":")) > 2):
        pixyX = line.replace('\n', '').split(":")[2].split(" ")[1]
        sd.putString("pixy X", pixyX)
        print("put X: " + str(pixyX))
