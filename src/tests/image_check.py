import unittest
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from container_utils import check_image

class TestSum(unittest.TestCase):

    def test_direct_check_image(self):
        allowed_image_list = [".io", ".com", ".co", ".tr"]
        self.assertEqual(check_image("repo/kube-webhook:latest", allowed_image_list), False)

    def test_docker_hub_allowed(self):
        allowed_image_list = ["repo"]
        self.assertEqual(check_image("repo/kube-webhook:v3", allowed_image_list), True)


if __name__ == '__main__':
    unittest.main()