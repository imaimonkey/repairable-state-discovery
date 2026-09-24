# V2R cluster inventory

2026-09-24T06:45:58.234947+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324487479296 available bytes; 81.90% used; 112491512 free inodes.

server1 `/home`: 324487479296 available bytes; 81.90% used; 112491512 free inodes.

server1 `/tmp`: 324487479296 available bytes; 81.90% used; 112491512 free inodes.

server1 `/var/tmp`: 324487479296 available bytes; 81.90% used; 112491512 free inodes.

server1 `/mnt/raid5`: 517571788800 available bytes; 97.63% used; 337723685 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57871720448 available bytes; 96.77% used; 110431203 free inodes.

server2 `/home`: 57871720448 available bytes; 96.77% used; 110431203 free inodes.

server2 `/tmp`: 57871720448 available bytes; 96.77% used; 110431203 free inodes.

server2 `/var/tmp`: 57871720448 available bytes; 96.77% used; 110431203 free inodes.

server2 `/mnt/raid5`: 519773536256 available bytes; 96.41% used; 445191689 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126771654656 available bytes; 92.93% used; 114175148 free inodes.

server3 `/home`: 126771654656 available bytes; 92.93% used; 114175148 free inodes.

server3 `/data`: 139344216064 available bytes; 98.07% used; 225835424 free inodes.

server3 `/tmp`: 126771654656 available bytes; 92.93% used; 114175148 free inodes.

server3 `/var/tmp`: 126771654656 available bytes; 92.93% used; 114175148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105804615680 available bytes; 94.10% used; 114349239 free inodes.

server4 `/home`: 105804615680 available bytes; 94.10% used; 114349239 free inodes.

server4 `/data`: 314697113600 available bytes; 95.65% used; 225368455 free inodes.

server4 `/tmp`: 105804615680 available bytes; 94.10% used; 114349239 free inodes.

server4 `/var/tmp`: 105804615680 available bytes; 94.10% used; 114349239 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
