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

class TestCatCommand(kptest.KPTestCase):

    def test_cat_is_successful(self):
        # Given
        self.editor('env', env="Watch out for turtles. They'll bite you if you put your fingers in their mouths.")
        self.create("test", password="42")

        # When
        self.cat("test", options=["-pm"])

        # Then
        self.assertStdoutEquals("42",
                                "Watch out for turtles. They'll bite you if you put your fingers in their mouths.")

    @kptest.with_agent
    def test_cat_is_successful_with_agent(self):
        # Given
        self.editor('env', env="Watch out for turtles. They'll bite you if you put your fingers in their mouths.")
        self.create("test", password="42")
        self.open("test")

        # When
        self.cat("test", master=None, options=["-pm"])

        # Then
        self.assertStdoutEquals("42",
                                "Watch out for turtles. They'll bite you if you put your fingers in their mouths.")

if __name__ == '__main__':
        unittest.main()
