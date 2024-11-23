import threading
import queue
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# Worker Thread Class for Encryption
class EncryptionWorker(threading.Thread):
    def __init__(self, plaintext_queue, ciphertext_queue):
        threading.Thread.__init__(self)
        self.plaintext_queue = plaintext_queue
        self.ciphertext_queue = ciphertext_queue
        self.key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long

    def run(self):
        while True:
            plaintext = self.plaintext_queue.get()  # Get plaintext from queue
            if plaintext is None:  # Check for termination signal
                break

            # Create a new cipher for each encryption operation
            cipher = AES.new(self.key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)

            # Store the nonce, ciphertext, and tag in the queue
            self.ciphertext_queue.put((cipher.nonce, ciphertext, tag))

    def decrypt_message(self, nonce, ciphertext, tag):
        """Decrypts a ciphertext using the stored key."""
        try:
            # Recreate the cipher with the same nonce and key
            cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            return plaintext
        except ValueError:
            return None  # Return None if decryption or authentication fails


# Main Program
if __name__ == "__main__":
    # Create Queues for Plaintext and Ciphertext
    plaintext_queue = queue.Queue()
    ciphertext_queue = queue.Queue()

    # Create and Start the Encryption Worker
    worker = EncryptionWorker(plaintext_queue, ciphertext_queue)
    worker.start()

    # Add plaintext messages to the queue
    messages = [b"Hello, World!", b"Python is awesome!", b"Multithreading is powerful!"]
    for msg in messages:
        plaintext_queue.put(msg)

    # Add a stop signal to terminate the thread
    plaintext_queue.put(None)
    worker.join()

    # Retrieve encrypted messages from the ciphertext queue
    print("Encrypted messages:")
    encrypted_messages = []  # Store encrypted messages for decryption
    while not ciphertext_queue.empty():
        nonce, ciphertext, tag = ciphertext_queue.get()
        print(f"Nonce: {nonce}, Ciphertext: {ciphertext}, Tag: {tag}")
        encrypted_messages.append((nonce, ciphertext, tag))

    # Decrypt the messages
    print("\nDecrypted messages:")
    for nonce, ciphertext, tag in encrypted_messages:
        plaintext = worker.decrypt_message(nonce, ciphertext, tag)
        if plaintext:
            print(f"Decrypted Plaintext: {plaintext.decode()}")
        else:
            print("Decryption failed!")
