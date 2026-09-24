# V2R cluster inventory

2026-09-24T10:42:06.789178+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324405403648 available bytes; 81.90% used; 112489185 free inodes.

server1 `/home`: 324405403648 available bytes; 81.90% used; 112489185 free inodes.

server1 `/tmp`: 324405403648 available bytes; 81.90% used; 112489185 free inodes.

server1 `/var/tmp`: 324405403648 available bytes; 81.90% used; 112489185 free inodes.

server1 `/mnt/raid5`: 499797102592 available bytes; 97.71% used; 337696393 free inodes.
| server2 | True | ['5'] | [] | reference_compatible=False |

server2 `/`: 57717604352 available bytes; 96.78% used; 110430485 free inodes.

server2 `/home`: 57717604352 available bytes; 96.78% used; 110430485 free inodes.

server2 `/tmp`: 57717604352 available bytes; 96.78% used; 110430485 free inodes.

server2 `/var/tmp`: 57717604352 available bytes; 96.78% used; 110430485 free inodes.

server2 `/mnt/raid5`: 512430870528 available bytes; 96.46% used; 445174973 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85815869440 available bytes; 95.21% used; 114199452 free inodes.

server3 `/home`: 85815869440 available bytes; 95.21% used; 114199452 free inodes.

server3 `/data`: 164145090560 available bytes; 97.73% used; 225817989 free inodes.

server3 `/tmp`: 85815869440 available bytes; 95.21% used; 114199452 free inodes.

server3 `/var/tmp`: 85815869440 available bytes; 95.21% used; 114199452 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105744060416 available bytes; 94.10% used; 114348964 free inodes.

server4 `/home`: 105744060416 available bytes; 94.10% used; 114348964 free inodes.

server4 `/data`: 137449943040 available bytes; 98.10% used; 225258352 free inodes.

server4 `/tmp`: 105744060416 available bytes; 94.10% used; 114348964 free inodes.

server4 `/var/tmp`: 105744060416 available bytes; 94.10% used; 114348964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
