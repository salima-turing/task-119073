import unittest
import hashlib

class TestDataHashing(unittest.TestCase):

    def test_hashing_technique_preserves_data_integrity(self):
        """
        Test whether the selected hashing technique preserves data integrity.
        """
        data_to_hash = b"This is some data to be hashed"

        # Calculate the hash value using the selected hashing technique
        hash_value = hashlib.sha256(data_to_hash).hexdigest()

        # Compare the calculated hash value with the expected hash value
        self.assertEqual(hash_value, '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918')

if __name__ == '__main__':
    unittest.main()
