import unittest
import hashlib


def data_hashing(data, hashing_technique):
    if hashing_technique == "md5":
        return hashlib.md5(data.encode('utf-8')).hexdigest()
    elif hashing_technique == "sha256":
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    else:
        raise ValueError("Invalid hashing technique")


class TestDataHashing(unittest.TestCase):

    def test_md5_hashing_preserves_data_integrity(self):
        data = "hello"
        expected_hash = "5d41402abc4b2a76b9719d911017c592"
        result = data_hashing(data, "md5")
        self.assertEqual(result, expected_hash, "MD5 hashing failed to preserve data integrity")

    def test_sha256_hashing_preserves_data_integrity(self):
        data = "hello"
        expected_hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        result = data_hashing(data, "sha256")
        self.assertEqual(result, expected_hash, "SHA-256 hashing failed to preserve data integrity")

    def test_invalid_hashing_technique_raises_valueerror(self):
        data = "hello"
        with self.assertRaises(ValueError):
            data_hashing(data, "invalid")


if __name__ == '__main__':
    unittest.main()
