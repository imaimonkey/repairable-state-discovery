# V2R cluster inventory

2026-09-24T08:31:41.777154+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324400648192 available bytes; 81.90% used; 112490447 free inodes.

server1 `/home`: 324400648192 available bytes; 81.90% used; 112490447 free inodes.

server1 `/tmp`: 324400648192 available bytes; 81.90% used; 112490447 free inodes.

server1 `/var/tmp`: 324400648192 available bytes; 81.90% used; 112490447 free inodes.

server1 `/mnt/raid5`: 510078271488 available bytes; 97.66% used; 337720883 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57808433152 available bytes; 96.78% used; 110430996 free inodes.

server2 `/home`: 57808433152 available bytes; 96.78% used; 110430996 free inodes.

server2 `/tmp`: 57808433152 available bytes; 96.78% used; 110430996 free inodes.

server2 `/var/tmp`: 57808433152 available bytes; 96.78% used; 110430996 free inodes.

server2 `/mnt/raid5`: 516102930432 available bytes; 96.43% used; 445179575 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85570932736 available bytes; 95.22% used; 114185874 free inodes.

server3 `/home`: 85570932736 available bytes; 95.22% used; 114185874 free inodes.

server3 `/data`: 175052308480 available bytes; 97.58% used; 225822940 free inodes.

server3 `/tmp`: 85570932736 available bytes; 95.22% used; 114185873 free inodes.

server3 `/var/tmp`: 85570932736 available bytes; 95.22% used; 114185873 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769193472 available bytes; 94.10% used; 114349117 free inodes.

server4 `/home`: 105769193472 available bytes; 94.10% used; 114349117 free inodes.

server4 `/data`: 266460073984 available bytes; 96.32% used; 225307695 free inodes.

server4 `/tmp`: 105769193472 available bytes; 94.10% used; 114349117 free inodes.

server4 `/var/tmp`: 105769193472 available bytes; 94.10% used; 114349117 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
