import hashlib
import time

def solve_nonce(challenge_string, difficulty_zeros):
    """
    Logika utama solver untuk menemukan nilai nonce 
    berdasarkan target awalan nol pada hash SHA-256.
    """
    target_prefix = '0' * int(difficulty_zeros)
    nonce = 0
    
    while True:
        input_data = f"{challenge_string}{nonce}".encode('utf-8')
        generated_hash = hashlib.sha256(input_data).hexdigest()
        
        if generated_hash.startswith(target_prefix):
            return {
                "status": "Success",
                "nonce": nonce,
                "hash": generated_hash
            }
        nonce += 1
