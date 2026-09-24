# V2R cluster inventory

2026-09-24T16:08:21.679806+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324027482112 available bytes; 81.92% used; 112481452 free inodes.

server1 `/home`: 324027482112 available bytes; 81.92% used; 112481452 free inodes.

server1 `/tmp`: 324027482112 available bytes; 81.92% used; 112481452 free inodes.

server1 `/var/tmp`: 324027482112 available bytes; 81.92% used; 112481452 free inodes.

server1 `/mnt/raid5`: 416623181824 available bytes; 98.09% used; 337655909 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57349713920 available bytes; 96.80% used; 110427119 free inodes.

server2 `/home`: 57349713920 available bytes; 96.80% used; 110427119 free inodes.

server2 `/tmp`: 57349713920 available bytes; 96.80% used; 110427119 free inodes.

server2 `/var/tmp`: 57349713920 available bytes; 96.80% used; 110427119 free inodes.

server2 `/mnt/raid5`: 501597052928 available bytes; 96.53% used; 445164597 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84323373056 available bytes; 95.29% used; 114154651 free inodes.

server3 `/home`: 84323373056 available bytes; 95.29% used; 114154651 free inodes.

server3 `/data`: 160029224960 available bytes; 97.79% used; 225805720 free inodes.

server3 `/tmp`: 84323373056 available bytes; 95.29% used; 114154651 free inodes.

server3 `/var/tmp`: 84323373056 available bytes; 95.29% used; 114154651 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697972224 available bytes; 94.10% used; 114348610 free inodes.

server4 `/home`: 105697972224 available bytes; 94.10% used; 114348610 free inodes.

server4 `/data`: 89325240320 available bytes; 98.77% used; 225256164 free inodes.

server4 `/tmp`: 105697972224 available bytes; 94.10% used; 114348610 free inodes.

server4 `/var/tmp`: 105697972224 available bytes; 94.10% used; 114348610 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
