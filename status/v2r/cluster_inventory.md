# V2R cluster inventory

2026-09-25T01:36:09.104287+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319076323328 available bytes; 82.20% used; 112480763 free inodes.

server1 `/home`: 319076323328 available bytes; 82.20% used; 112480763 free inodes.

server1 `/tmp`: 319076323328 available bytes; 82.20% used; 112480763 free inodes.

server1 `/var/tmp`: 319076323328 available bytes; 82.20% used; 112480763 free inodes.

server1 `/mnt/raid5`: 416467623936 available bytes; 98.09% used; 337612243 free inodes.
| server2 | True | ['2', '6'] | [] | reference_compatible=False |

server2 `/`: 23049441280 available bytes; 98.71% used; 110410766 free inodes.

server2 `/home`: 23049441280 available bytes; 98.71% used; 110410766 free inodes.

server2 `/tmp`: 23049441280 available bytes; 98.71% used; 110410766 free inodes.

server2 `/var/tmp`: 23049441280 available bytes; 98.71% used; 110410766 free inodes.

server2 `/mnt/raid5`: 490911698944 available bytes; 96.61% used; 445161227 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84354289664 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84354289664 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 146593116160 available bytes; 97.97% used; 225812187 free inodes.

server3 `/tmp`: 84354289664 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84354289664 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778700288 available bytes; 94.10% used; 114348287 free inodes.

server4 `/home`: 105778700288 available bytes; 94.10% used; 114348287 free inodes.

server4 `/data`: 53317779456 available bytes; 99.26% used; 225030609 free inodes.

server4 `/tmp`: 105778700288 available bytes; 94.10% used; 114348287 free inodes.

server4 `/var/tmp`: 105778700288 available bytes; 94.10% used; 114348287 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
