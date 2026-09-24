# V2R cluster inventory

2026-09-24T07:28:00.896512+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324451414016 available bytes; 81.90% used; 112491160 free inodes.

server1 `/home`: 324451414016 available bytes; 81.90% used; 112491160 free inodes.

server1 `/tmp`: 324451414016 available bytes; 81.90% used; 112491160 free inodes.

server1 `/var/tmp`: 324451414016 available bytes; 81.90% used; 112491160 free inodes.

server1 `/mnt/raid5`: 517410701312 available bytes; 97.63% used; 337722799 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57850773504 available bytes; 96.77% used; 110431172 free inodes.

server2 `/home`: 57850773504 available bytes; 96.77% used; 110431172 free inodes.

server2 `/tmp`: 57850773504 available bytes; 96.77% used; 110431172 free inodes.

server2 `/var/tmp`: 57850773504 available bytes; 96.77% used; 110431172 free inodes.

server2 `/mnt/raid5`: 518344859648 available bytes; 96.42% used; 445180995 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126780194816 available bytes; 92.93% used; 114174723 free inodes.

server3 `/home`: 126780194816 available bytes; 92.93% used; 114174723 free inodes.

server3 `/data`: 138814119936 available bytes; 98.08% used; 225834165 free inodes.

server3 `/tmp`: 126780194816 available bytes; 92.93% used; 114174723 free inodes.

server3 `/var/tmp`: 126780194816 available bytes; 92.93% used; 114174723 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780826112 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105780826112 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 285870903296 available bytes; 96.05% used; 225366909 free inodes.

server4 `/tmp`: 105780826112 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105780826112 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
