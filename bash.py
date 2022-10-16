import os
os.system("apt update && apt full-upgrade -Y\npip install wheel\npkg update\npkg install build-essential -Y\npkg install binutils -Y\npip install coincurve --no-binary all\npip install bit\nMATHLIB=\"m\" pip3 install numpy\npip install bitcoinlib --no-binary all\npip install eth_hash")
