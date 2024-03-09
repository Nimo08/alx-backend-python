#!/usr/bin/env python3
"""
Parameterize and patch as decorators
Mocking a property
More patching
Parameterize
Integration test: fixtures
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test Class"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test case: org
        Intercept get_json using patch and replace with mock obj
        Call get_json once using mock_obj: mock_get_json
        """
        mock_get_json.return_value = {"name": org_name}
        client = GithubOrgClient(org_name)
        org_data = client.org
        mock_get_json.assert_called_once_with(GithubOrgClient.
                                              ORG_URL.format(org=org_name))
        self.assertEqual(org_data["name"], org_name)

    def test_public_repos_url(self):
        """
        Test case: _public_repos_url
        """
        mock_payload = {"repos_url": "http://example.com/repos"}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) \
                as mock_org:
            mock_org.return_value = mock_payload
            client = GithubOrgClient("example.org")
            repo_url = client._public_repos_url
            self.assertEqual(mock_payload["repos_url"], repo_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test case: public_repos"""
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        expected_result = ["repo1", "repo2"]
        mock_get_json.return_value = mock_payload
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://example.com/repos"
            client = GithubOrgClient("example")
            result = client.public_repos()
            mock_get_json.assert_called_once_with("https://example.com/repos")
            mock_public_repos_url.assert_called_once_with()
            self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test case: has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test Class"""
    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [cls.org_payload,
                                                      cls.repos_payload]

    def test_public_repos(self):
        """Test case: public repos"""
        client = GithubOrgClient("Google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test case: public repos with license"""
        client = GithubOrgClient("Google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
