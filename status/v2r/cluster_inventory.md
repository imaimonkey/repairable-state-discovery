# V2R cluster inventory

2026-09-25T20:46:53.060229+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318709047296 available bytes; 82.22% used; 112476326 free inodes.

server1 `/home`: 318709047296 available bytes; 82.22% used; 112476326 free inodes.

server1 `/tmp`: 318709047296 available bytes; 82.22% used; 112476326 free inodes.

server1 `/var/tmp`: 318709047296 available bytes; 82.22% used; 112476326 free inodes.

server1 `/mnt/raid5`: 368643190784 available bytes; 98.31% used; 337539574 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22945837056 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22945837056 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22945837056 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22945837056 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 302810607616 available bytes; 97.91% used; 445056862 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84372525056 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84372525056 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127104229376 available bytes; 98.24% used; 225807764 free inodes.

server3 `/tmp`: 84372525056 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84372525056 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655619584 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655619584 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228181393408 available bytes; 96.85% used; 224928296 free inodes.

server4 `/tmp`: 105655619584 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655619584 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
