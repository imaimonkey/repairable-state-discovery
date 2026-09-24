# V2R cluster inventory

2026-09-24T19:21:40.349924+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323995234304 available bytes; 81.93% used; 112481471 free inodes.

server1 `/home`: 323995234304 available bytes; 81.93% used; 112481471 free inodes.

server1 `/tmp`: 323995234304 available bytes; 81.93% used; 112481471 free inodes.

server1 `/var/tmp`: 323995234304 available bytes; 81.93% used; 112481471 free inodes.

server1 `/mnt/raid5`: 415631945728 available bytes; 98.09% used; 337633347 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54461173760 available bytes; 96.96% used; 110411891 free inodes.

server2 `/home`: 54461173760 available bytes; 96.96% used; 110411891 free inodes.

server2 `/tmp`: 54461173760 available bytes; 96.96% used; 110411891 free inodes.

server2 `/var/tmp`: 54461173760 available bytes; 96.96% used; 110411891 free inodes.

server2 `/mnt/raid5`: 495127257088 available bytes; 96.58% used; 445158920 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84406329344 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84406329344 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152343973888 available bytes; 97.89% used; 225799624 free inodes.

server3 `/tmp`: 84406329344 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84406329344 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660166144 available bytes; 94.10% used; 114348463 free inodes.

server4 `/home`: 105660166144 available bytes; 94.10% used; 114348463 free inodes.

server4 `/data`: 89892896768 available bytes; 98.76% used; 225267056 free inodes.

server4 `/tmp`: 105660166144 available bytes; 94.10% used; 114348463 free inodes.

server4 `/var/tmp`: 105660166144 available bytes; 94.10% used; 114348463 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
