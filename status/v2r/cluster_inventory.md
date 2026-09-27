# V2R cluster inventory

2026-09-27T10:41:32.040962+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314439323648 available bytes; 82.46% used; 112440686 free inodes.

server1 `/home`: 314439323648 available bytes; 82.46% used; 112440686 free inodes.

server1 `/tmp`: 314439323648 available bytes; 82.46% used; 112440686 free inodes.

server1 `/var/tmp`: 314439323648 available bytes; 82.46% used; 112440686 free inodes.

server1 `/mnt/raid5`: 635411148800 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16496963584 available bytes; 99.08% used; 110355942 free inodes.

server2 `/home`: 16496963584 available bytes; 99.08% used; 110355942 free inodes.

server2 `/tmp`: 16496963584 available bytes; 99.08% used; 110355942 free inodes.

server2 `/var/tmp`: 16496963584 available bytes; 99.08% used; 110355942 free inodes.

server2 `/mnt/raid5`: 571455455232 available bytes; 96.05% used; 444738550 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543859712 available bytes; 95.62% used; 114062824 free inodes.

server3 `/home`: 78543859712 available bytes; 95.62% used; 114062824 free inodes.

server3 `/data`: 1332191858688 available bytes; 81.59% used; 225760793 free inodes.

server3 `/tmp`: 78543859712 available bytes; 95.62% used; 114062824 free inodes.

server3 `/var/tmp`: 78543859712 available bytes; 95.62% used; 114062824 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111031586816 available bytes; 93.80% used; 114372825 free inodes.

server4 `/home`: 111031586816 available bytes; 93.80% used; 114372825 free inodes.

server4 `/data`: 363284209664 available bytes; 94.98% used; 224766858 free inodes.

server4 `/tmp`: 111031586816 available bytes; 93.80% used; 114372825 free inodes.

server4 `/var/tmp`: 111031586816 available bytes; 93.80% used; 114372825 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
