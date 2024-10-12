import unittest
import hashlib

class TestDataHashing(unittest.TestCase):

	def test_md5_hashing(self):
		data = b"Hello, this is a test!"
		expected_hash = '645102c3e4a886012154735a1511045b'
		result_hash = hashlib.md5(data).hexdigest()
		self.assertEqual(result_hash, expected_hash, "MD5 hashing failed")

	def test_sha256_hashing(self):
		data = b"Hello, this is a test!"
		expected_hash = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
		result_hash = hashlib.sha256(data).hexdigest()
		self.assertEqual(result_hash, expected_hash, "SHA-256 hashing failed")

if __name__ == '__main__':
	unittest.main()
