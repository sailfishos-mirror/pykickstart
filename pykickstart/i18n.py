#
# Tomas Radej <tradej@redhat.com>
#
# Copyright 2015-2020 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.  Any Red Hat
# trademarks that are incorporated in the source code or documentation are not
# subject to the GNU General Public License and may only be used or replicated
# with the express permission of Red Hat, Inc.
#
import gettext
import os

def _find_locale_files():
    module_path = os.path.abspath(__file__)
    locale_path = os.path.join(os.path.dirname(module_path), 'locale')

    gettext.bindtextdomain("pykickstart", locale_path)
_find_locale_files()

_ = lambda x: gettext.translation("pykickstart", fallback=True).gettext(x) if x != "" else ""
