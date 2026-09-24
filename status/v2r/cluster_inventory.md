# V2R cluster inventory

2026-09-24T20:24:55.996052+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323981262848 available bytes; 81.93% used; 112481435 free inodes.

server1 `/home`: 323981262848 available bytes; 81.93% used; 112481435 free inodes.

server1 `/tmp`: 323981262848 available bytes; 81.93% used; 112481435 free inodes.

server1 `/var/tmp`: 323981262848 available bytes; 81.93% used; 112481435 free inodes.

server1 `/mnt/raid5`: 415650840576 available bytes; 98.09% used; 337635052 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30160379904 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30160379904 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30160379904 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30160379904 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 492429508608 available bytes; 96.60% used; 445156755 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84391727104 available bytes; 95.29% used; 114156109 free inodes.

server3 `/home`: 84391727104 available bytes; 95.29% used; 114156109 free inodes.

server3 `/data`: 151556374528 available bytes; 97.91% used; 225804512 free inodes.

server3 `/tmp`: 84391727104 available bytes; 95.29% used; 114156109 free inodes.

server3 `/var/tmp`: 84391727104 available bytes; 95.29% used; 114156109 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640587264 available bytes; 94.10% used; 114348392 free inodes.

server4 `/home`: 105640587264 available bytes; 94.10% used; 114348392 free inodes.

server4 `/data`: 85501132800 available bytes; 98.82% used; 225258229 free inodes.

server4 `/tmp`: 105640587264 available bytes; 94.10% used; 114348392 free inodes.

server4 `/var/tmp`: 105640587264 available bytes; 94.10% used; 114348392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
