# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gns3.topology import Topology
from gns3.version import __version__


def test_topology_init():
    Topology()


def test_topology_node(vpcs_device):
    topology = Topology()
    topology.addNode(vpcs_device)
    assert len(topology.nodes()) == 1
    assert topology.getNode(vpcs_device.id()) == vpcs_device
    topology.removeNode(vpcs_device)
    assert len(topology.nodes()) == 0


def test_dump(vpcs_device, project):
    topology = Topology()
    topology.project = project
    topology.addNode(vpcs_device)

    dump = topology.dump(include_gui_data=False)
    assert dict(dump) == {
        "auto_start": False,
        "name": project.name,
        "resources_type": "local",
        "version": __version__,
        "topology": {
            "nodes": [
                {
                    "description": "VPCS device",
                    "id": vpcs_device.id(),
                    "ports": [
                        {
                            "id": vpcs_device.ports()[0].id(),
                            "name": "Ethernet0",
                            "port_number": 0
                        }
                    ],
                    "properties": {},
                    "server_id": 1,
                    "type": "VPCSDevice",
                    "vpcs_id": None
                }
            ],
            "servers": [
                {
                    "cloud": False,
                    "host": "127.0.0.1",
                    "id": 1,
                    "local": True,
                    "port": 8000,
                }
            ]
        },
        "type": "topology"
    }
