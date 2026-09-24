# V2R cluster inventory

2026-09-24T16:23:56.316727+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024614912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324024614912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324024614912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324024614912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416580395008 available bytes; 98.09% used; 337654102 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57332273152 available bytes; 96.80% used; 110426953 free inodes.

server2 `/home`: 57332273152 available bytes; 96.80% used; 110426953 free inodes.

server2 `/tmp`: 57332273152 available bytes; 96.80% used; 110426953 free inodes.

server2 `/var/tmp`: 57332273152 available bytes; 96.80% used; 110426953 free inodes.

server2 `/mnt/raid5`: 501148917760 available bytes; 96.54% used; 445164741 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84329791488 available bytes; 95.29% used; 114154491 free inodes.

server3 `/home`: 84329791488 available bytes; 95.29% used; 114154491 free inodes.

server3 `/data`: 159554224128 available bytes; 97.79% used; 225788158 free inodes.

server3 `/tmp`: 84329791488 available bytes; 95.29% used; 114154491 free inodes.

server3 `/var/tmp`: 84329791488 available bytes; 95.29% used; 114154491 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697300480 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697300480 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89283710976 available bytes; 98.77% used; 225255858 free inodes.

server4 `/tmp`: 105697300480 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697300480 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
