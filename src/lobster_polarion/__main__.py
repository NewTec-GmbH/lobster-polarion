"""The main module with the program entry point."""

# lobster-polarion - A tool to convert TRLC files to specific formats.
# Copyright (c) 2026 - 2026 NewTec GmbH
#
# This file is part of lobster-polarion program.
#
# The lobster-polarion program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# The lobster-polarion program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with lobster-polarion.
# If not, see <https://www.gnu.org/licenses/>.

# Imports **********************************************************************

import sys

# Variables ********************************************************************

# Classes **********************************************************************

# Functions ********************************************************************

def main() -> int:
    # lobster-trace: SwRequirements.sw_req_cli
    """Main program entry point.

    Returns:
        int: Program status
    """
    print("hello world")
    return 0

# Main *************************************************************************

if __name__ == "__main__":
    sys.exit(main())