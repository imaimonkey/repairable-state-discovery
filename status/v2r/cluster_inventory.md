# V2R cluster inventory

2026-09-25T06:10:06.613540+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318878277632 available bytes; 82.21% used; 112480360 free inodes.

server1 `/home`: 318878277632 available bytes; 82.21% used; 112480360 free inodes.

server1 `/tmp`: 318878277632 available bytes; 82.21% used; 112480360 free inodes.

server1 `/var/tmp`: 318878277632 available bytes; 82.21% used; 112480360 free inodes.

server1 `/mnt/raid5`: 401494646784 available bytes; 98.16% used; 337563440 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22901104640 available bytes; 98.72% used; 110410530 free inodes.

server2 `/home`: 22901104640 available bytes; 98.72% used; 110410530 free inodes.

server2 `/tmp`: 22901104640 available bytes; 98.72% used; 110410530 free inodes.

server2 `/var/tmp`: 22901104640 available bytes; 98.72% used; 110410530 free inodes.

server2 `/mnt/raid5`: 375868178432 available bytes; 97.40% used; 445100520 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84317646848 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84317646848 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142767366144 available bytes; 98.03% used; 225814145 free inodes.

server3 `/tmp`: 84317646848 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84317646848 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105648816128 available bytes; 94.10% used; 114350386 free inodes.

server4 `/home`: 105648816128 available bytes; 94.10% used; 114350386 free inodes.

server4 `/data`: 254662160384 available bytes; 96.48% used; 225024305 free inodes.

server4 `/tmp`: 105648816128 available bytes; 94.10% used; 114350386 free inodes.

server4 `/var/tmp`: 105648816128 available bytes; 94.10% used; 114350386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
