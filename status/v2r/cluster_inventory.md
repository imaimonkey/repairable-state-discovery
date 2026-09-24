# V2R cluster inventory

2026-09-24T20:26:28.251038+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323981905920 available bytes; 81.93% used; 112481434 free inodes.

server1 `/home`: 323981905920 available bytes; 81.93% used; 112481434 free inodes.

server1 `/tmp`: 323981905920 available bytes; 81.93% used; 112481434 free inodes.

server1 `/var/tmp`: 323981905920 available bytes; 81.93% used; 112481434 free inodes.

server1 `/mnt/raid5`: 415647752192 available bytes; 98.09% used; 337634874 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30160072704 available bytes; 98.32% used; 110411377 free inodes.

server2 `/home`: 30160072704 available bytes; 98.32% used; 110411377 free inodes.

server2 `/tmp`: 30160072704 available bytes; 98.32% used; 110411377 free inodes.

server2 `/var/tmp`: 30160072704 available bytes; 98.32% used; 110411377 free inodes.

server2 `/mnt/raid5`: 492380762112 available bytes; 96.60% used; 445156687 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84391632896 available bytes; 95.29% used; 114156104 free inodes.

server3 `/home`: 84391632896 available bytes; 95.29% used; 114156104 free inodes.

server3 `/data`: 151530815488 available bytes; 97.91% used; 225804478 free inodes.

server3 `/tmp`: 84391632896 available bytes; 95.29% used; 114156104 free inodes.

server3 `/var/tmp`: 84391632896 available bytes; 95.29% used; 114156104 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640538112 available bytes; 94.10% used; 114348392 free inodes.

server4 `/home`: 105640538112 available bytes; 94.10% used; 114348392 free inodes.

server4 `/data`: 85488545792 available bytes; 98.82% used; 225258069 free inodes.

server4 `/tmp`: 105640538112 available bytes; 94.10% used; 114348392 free inodes.

server4 `/var/tmp`: 105640538112 available bytes; 94.10% used; 114348392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
