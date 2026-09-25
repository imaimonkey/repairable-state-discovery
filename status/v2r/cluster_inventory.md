# V2R cluster inventory

2026-09-25T03:11:23.053788+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318940540928 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318940540928 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318940540928 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318940540928 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 416125247488 available bytes; 98.09% used; 337601112 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22990540800 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22990540800 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22990540800 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22990540800 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 465769328640 available bytes; 96.78% used; 445112596 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84344586240 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84344586240 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 144840826880 available bytes; 98.00% used; 225810261 free inodes.

server3 `/tmp`: 84344586240 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84344586240 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692889088 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692889088 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 50242048000 available bytes; 99.31% used; 224967312 free inodes.

server4 `/tmp`: 105692889088 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692889088 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
