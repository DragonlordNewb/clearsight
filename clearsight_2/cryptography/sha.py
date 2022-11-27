import hashlib

def hash(string):
    return hashlib.sha256(string.encode("utf-8")).hexdigest()
