#
# Hans de Goede <hdegoede@redhat.com>
#
# Copyright 2009 Red Hat, Inc.
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
from pykickstart.base import *
from pykickstart.options import *

import gettext
_ = lambda x: gettext.ldgettext("pykickstart", x)

class F12_FcoeData(BaseData):
    removedKeywords = BaseData.removedKeywords
    removedAttrs = BaseData.removedAttrs

    def __init__(self, *args, **kwargs):
        BaseData.__init__(self, *args, **kwargs)
        self.nic = kwargs.get("nic", None)

    def __str__(self):
        retval = BaseData.__str__(self)
        retval += "fcoe"

        if self.nic:
            retval += " --nic=%s" % self.nic

        return retval + "\n"


class F12_Fcoe(KickstartCommand):
    removedKeywords = KickstartCommand.removedKeywords
    removedAttrs = KickstartCommand.removedAttrs

    def __init__(self, writePriority=71, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.op = self._getParser()
        self.fcoe = kwargs.get("fcoe", [])

    def __str__(self):
        retval = ""
        for fcoe in self.fcoe:
            retval += fcoe.__str__()

        return retval

    def _getParser(self):
        op = KSOptionParser()
        op.add_option("--nic", dest="nic", required=1)
        return op

    def parse(self, args):
        zd = self.handler.FcoeData()
        (opts, extra) = self.op.parse_args(args=args, lineno=self.lineno)
        if len(extra) > 0:
            mapping = {"command": "fcoe", "options": extra}
            raise KickstartValueError, formatErrorMsg(self.lineno, msg=_("Unexpected arguments to %(command)s command: %(options)s") % mapping)

        self._setToObj(self.op, opts, zd)
        return zd

    def dataList(self):
        return self.fcoe