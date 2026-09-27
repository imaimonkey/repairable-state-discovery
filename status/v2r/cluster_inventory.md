# V2R cluster inventory

2026-09-27T09:31:25.556529+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314451783680 available bytes; 82.46% used; 112440740 free inodes.

server1 `/home`: 314451783680 available bytes; 82.46% used; 112440740 free inodes.

server1 `/tmp`: 314451783680 available bytes; 82.46% used; 112440740 free inodes.

server1 `/var/tmp`: 314451783680 available bytes; 82.46% used; 112440740 free inodes.

server1 `/mnt/raid5`: 635445497856 available bytes; 97.08% used; 337424409 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16509075456 available bytes; 99.08% used; 110356966 free inodes.

server2 `/home`: 16509075456 available bytes; 99.08% used; 110356966 free inodes.

server2 `/tmp`: 16509075456 available bytes; 99.08% used; 110356966 free inodes.

server2 `/var/tmp`: 16509075456 available bytes; 99.08% used; 110356966 free inodes.

server2 `/mnt/raid5`: 573590376448 available bytes; 96.04% used; 444741653 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78555971584 available bytes; 95.62% used; 114062922 free inodes.

server3 `/home`: 78555971584 available bytes; 95.62% used; 114062922 free inodes.

server3 `/data`: 1332485099520 available bytes; 81.58% used; 225762347 free inodes.

server3 `/tmp`: 78555971584 available bytes; 95.62% used; 114062922 free inodes.

server3 `/var/tmp`: 78555971584 available bytes; 95.62% used; 114062922 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111050346496 available bytes; 93.80% used; 114372850 free inodes.

server4 `/home`: 111050346496 available bytes; 93.80% used; 114372850 free inodes.

server4 `/data`: 364004417536 available bytes; 94.97% used; 224767214 free inodes.

server4 `/tmp`: 111050346496 available bytes; 93.80% used; 114372850 free inodes.

server4 `/var/tmp`: 111050346496 available bytes; 93.80% used; 114372850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
