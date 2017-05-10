#
# Copyright (c) 2015 Paul Fariello <paul@fariello.eu>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
import unittest
import kptest

class TestDeleteCommand(kptest.KPTestCase):

    def test_delete_is_successful(self):
        # Given
        self.editor('date')
        self.create("test")

        # When
        self.delete("test")

        # Then
        self.assertSafeDoesntExists("test")

    def test_delete_refuse_to_delete_without_valid_password(self):
        # Given
        self.editor('date')
        self.create("test")

        # When
        self.delete("test", master="Il0v3ST20", rc=7)

        # Then
        self.assertSafeExists("test")

    @kptest.with_agent
    def test_delete_with_agent_is_successful(self):
        # Given
        self.editor('date')
        self.create("test")
        self.open("test")

        # When
        self.delete("test")

        # Then
        self.assertSafeDoesntExists("test")

    @kptest.with_agent
    def test_delete_with_agent_remove_safe_from_agent(self):
        # Given
        self.editor('date')
        self.create("test")
        self.open("test")
        self.delete("test")

        # When
        # Recreate test to ensure older test isn't in agent
        self.editor('env', env="Watch out for turtles. They'll bite you if you put your fingers in their mouths.")
        self.create("test")

        # Then
        # cat should ask for password, thus master param is not set to None
        self.cat("test")
        self.assertStdoutEquals("Watch out for turtles. They'll bite you if you put your fingers in their mouths.")

if __name__ == '__main__':
        unittest.main()
