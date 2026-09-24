# V2R cluster inventory

2026-09-24T03:18:19.631969+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325361979392 available bytes; 81.85% used; 112498279 free inodes.

server1 `/home`: 325361979392 available bytes; 81.85% used; 112498279 free inodes.

server1 `/tmp`: 325361979392 available bytes; 81.85% used; 112498279 free inodes.

server1 `/var/tmp`: 325361979392 available bytes; 81.85% used; 112498279 free inodes.

server1 `/mnt/raid5`: 425713577984 available bytes; 98.05% used; 337732143 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40845910016 available bytes; 97.72% used; 110431182 free inodes.

server2 `/home`: 40845910016 available bytes; 97.72% used; 110431182 free inodes.

server2 `/tmp`: 40845910016 available bytes; 97.72% used; 110431182 free inodes.

server2 `/var/tmp`: 40845910016 available bytes; 97.72% used; 110431182 free inodes.

server2 `/mnt/raid5`: 527513690112 available bytes; 96.36% used; 445197920 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292005142528 available bytes; 83.71% used; 114177822 free inodes.

server3 `/home`: 292005142528 available bytes; 83.71% used; 114177822 free inodes.

server3 `/data`: 39634493440 available bytes; 99.45% used; 225844129 free inodes.

server3 `/tmp`: 292005142528 available bytes; 83.71% used; 114177822 free inodes.

server3 `/var/tmp`: 292005142528 available bytes; 83.71% used; 114177822 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987543040 available bytes; 94.09% used; 114349612 free inodes.

server4 `/home`: 105987543040 available bytes; 94.09% used; 114349612 free inodes.

server4 `/data`: 289364312064 available bytes; 96.00% used; 225386596 free inodes.

server4 `/tmp`: 105987543040 available bytes; 94.09% used; 114349612 free inodes.

server4 `/var/tmp`: 105987543040 available bytes; 94.09% used; 114349612 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
