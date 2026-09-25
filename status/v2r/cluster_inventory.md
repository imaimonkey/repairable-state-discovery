# V2R cluster inventory

2026-09-25T19:06:04.751099+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318733811712 available bytes; 82.22% used; 112476328 free inodes.

server1 `/home`: 318733811712 available bytes; 82.22% used; 112476328 free inodes.

server1 `/tmp`: 318733811712 available bytes; 82.22% used; 112476328 free inodes.

server1 `/var/tmp`: 318733811712 available bytes; 82.22% used; 112476328 free inodes.

server1 `/mnt/raid5`: 371004350464 available bytes; 98.30% used; 337540926 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23103836160 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23103836160 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23103836160 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23103836160 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 312758816768 available bytes; 97.84% used; 445065160 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84383965184 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84383965184 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 131363520512 available bytes; 98.18% used; 225809012 free inodes.

server3 `/tmp`: 84383965184 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84383965184 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105606393856 available bytes; 94.11% used; 114349594 free inodes.

server4 `/home`: 105606393856 available bytes; 94.11% used; 114349594 free inodes.

server4 `/data`: 229675020288 available bytes; 96.83% used; 224931213 free inodes.

server4 `/tmp`: 105606393856 available bytes; 94.11% used; 114349594 free inodes.

server4 `/var/tmp`: 105606393856 available bytes; 94.11% used; 114349594 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
