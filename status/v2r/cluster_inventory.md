# V2R cluster inventory

2026-09-24T07:41:59.225218+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324441669632 available bytes; 81.90% used; 112490955 free inodes.

server1 `/home`: 324441669632 available bytes; 81.90% used; 112490955 free inodes.

server1 `/tmp`: 324441669632 available bytes; 81.90% used; 112490955 free inodes.

server1 `/var/tmp`: 324441669632 available bytes; 81.90% used; 112490955 free inodes.

server1 `/mnt/raid5`: 516850925568 available bytes; 97.63% used; 337722772 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57840058368 available bytes; 96.77% used; 110431140 free inodes.

server2 `/home`: 57840058368 available bytes; 96.77% used; 110431140 free inodes.

server2 `/tmp`: 57840058368 available bytes; 96.77% used; 110431140 free inodes.

server2 `/var/tmp`: 57840058368 available bytes; 96.77% used; 110431140 free inodes.

server2 `/mnt/raid5`: 517948030976 available bytes; 96.42% used; 445181515 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127154634752 available bytes; 92.90% used; 114199815 free inodes.

server3 `/home`: 127154634752 available bytes; 92.90% used; 114199815 free inodes.

server3 `/data`: 138705424384 available bytes; 98.08% used; 225833493 free inodes.

server3 `/tmp`: 127154634752 available bytes; 92.90% used; 114199815 free inodes.

server3 `/var/tmp`: 127154634752 available bytes; 92.90% used; 114199815 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780170752 available bytes; 94.10% used; 114349177 free inodes.

server4 `/home`: 105780170752 available bytes; 94.10% used; 114349177 free inodes.

server4 `/data`: 285693583360 available bytes; 96.05% used; 225366779 free inodes.

server4 `/tmp`: 105780170752 available bytes; 94.10% used; 114349177 free inodes.

server4 `/var/tmp`: 105780170752 available bytes; 94.10% used; 114349177 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
