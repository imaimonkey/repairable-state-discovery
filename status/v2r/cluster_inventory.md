# V2R cluster inventory

2026-09-24T05:51:33.293908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324526088192 available bytes; 81.90% used; 112492022 free inodes.

server1 `/home`: 324526088192 available bytes; 81.90% used; 112492022 free inodes.

server1 `/tmp`: 324526088192 available bytes; 81.90% used; 112492022 free inodes.

server1 `/var/tmp`: 324526088192 available bytes; 81.90% used; 112492022 free inodes.

server1 `/mnt/raid5`: 517609390080 available bytes; 97.63% used; 337723871 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57905401856 available bytes; 96.77% used; 110431314 free inodes.

server2 `/home`: 57905401856 available bytes; 96.77% used; 110431314 free inodes.

server2 `/tmp`: 57905401856 available bytes; 96.77% used; 110431314 free inodes.

server2 `/var/tmp`: 57905401856 available bytes; 96.77% used; 110431314 free inodes.

server2 `/mnt/raid5`: 521721466880 available bytes; 96.40% used; 445193340 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126806949888 available bytes; 92.92% used; 114175498 free inodes.

server3 `/home`: 126806949888 available bytes; 92.92% used; 114175498 free inodes.

server3 `/data`: 185214672896 available bytes; 97.44% used; 225838606 free inodes.

server3 `/tmp`: 126806949888 available bytes; 92.92% used; 114175498 free inodes.

server3 `/var/tmp`: 126806949888 available bytes; 92.92% used; 114175498 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815941120 available bytes; 94.10% used; 114349348 free inodes.

server4 `/home`: 105815941120 available bytes; 94.10% used; 114349348 free inodes.

server4 `/data`: 251479695360 available bytes; 96.52% used; 225357934 free inodes.

server4 `/tmp`: 105815941120 available bytes; 94.10% used; 114349348 free inodes.

server4 `/var/tmp`: 105815941120 available bytes; 94.10% used; 114349348 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
