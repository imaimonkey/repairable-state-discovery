# V2R cluster inventory

2026-09-25T03:26:50.708113+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318940553216 available bytes; 82.21% used; 112480371 free inodes.

server1 `/home`: 318940553216 available bytes; 82.21% used; 112480371 free inodes.

server1 `/tmp`: 318940553216 available bytes; 82.21% used; 112480371 free inodes.

server1 `/var/tmp`: 318940553216 available bytes; 82.21% used; 112480371 free inodes.

server1 `/mnt/raid5`: 416092909568 available bytes; 98.09% used; 337599309 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22980988928 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22980988928 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22980988928 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22980988928 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 465015595008 available bytes; 96.79% used; 445112135 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84342726656 available bytes; 95.29% used; 114156067 free inodes.

server3 `/home`: 84342726656 available bytes; 95.29% used; 114156067 free inodes.

server3 `/data`: 144576802816 available bytes; 98.00% used; 225809961 free inodes.

server3 `/tmp`: 84342726656 available bytes; 95.29% used; 114156067 free inodes.

server3 `/var/tmp`: 84342726656 available bytes; 95.29% used; 114156067 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692393472 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105692393472 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 45413134336 available bytes; 99.37% used; 224966639 free inodes.

server4 `/tmp`: 105692393472 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105692393472 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
