# V2R cluster inventory

2026-09-25T02:32:59.947929+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318969139200 available bytes; 82.21% used; 112480503 free inodes.

server1 `/home`: 318969139200 available bytes; 82.21% used; 112480503 free inodes.

server1 `/tmp`: 318969139200 available bytes; 82.21% used; 112480503 free inodes.

server1 `/var/tmp`: 318969139200 available bytes; 82.21% used; 112480503 free inodes.

server1 `/mnt/raid5`: 416208556032 available bytes; 98.09% used; 337605605 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23010410496 available bytes; 98.72% used; 110410437 free inodes.

server2 `/home`: 23010410496 available bytes; 98.72% used; 110410437 free inodes.

server2 `/tmp`: 23010410496 available bytes; 98.72% used; 110410437 free inodes.

server2 `/var/tmp`: 23010410496 available bytes; 98.72% used; 110410437 free inodes.

server2 `/mnt/raid5`: 483008274432 available bytes; 96.66% used; 445113535 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350910464 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350910464 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145550622720 available bytes; 97.99% used; 225810998 free inodes.

server3 `/tmp`: 84350910464 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350910464 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105895718912 available bytes; 94.09% used; 114350966 free inodes.

server4 `/home`: 105895718912 available bytes; 94.09% used; 114350966 free inodes.

server4 `/data`: 14093246464 available bytes; 99.81% used; 224969038 free inodes.

server4 `/tmp`: 105895718912 available bytes; 94.09% used; 114350966 free inodes.

server4 `/var/tmp`: 105895718912 available bytes; 94.09% used; 114350966 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
