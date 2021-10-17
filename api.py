

from storm_hasher import StormHasher

hasher = StormHasher("sha256")

print(hasher.algorithm)
print(hasher.chunk_size)

print(hasher.hash_command("python3 ola_mundo.py"))

print(hasher.hash_command(["python3", "ola_mundo.py"]))

print(type(hasher.hash_file("/home/felipe/Downloads/WLTS__IJAEOG_New.pdf")))
