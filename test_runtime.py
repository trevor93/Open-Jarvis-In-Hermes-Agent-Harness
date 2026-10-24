import unittest
from unittest.mock import patch

import runtime


class BuildCommandTests(unittest.TestCase):
    def test_system_prompt_only_on_session_initialization(self):
        session_id = "20260808_031038_0ecb14"
        with patch.object(runtime, "_hermes_base", return_value=["hermes"]):
            initial = runtime.build_command("hello", system="persona")
            resumed = runtime.build_command("next", session_id, system="persona")

        self.assertIn("persona", initial[initial.index("-q") + 1])
        self.assertIn("hello", initial[initial.index("-q") + 1])
        self.assertEqual(resumed[resumed.index("-q") + 1], "next")
        self.assertIn(session_id, resumed)


if __name__ == "__main__":
    unittest.main()
