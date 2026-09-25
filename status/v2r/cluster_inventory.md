# V2R cluster inventory

2026-09-25T17:35:55.555328+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318671085568 available bytes; 82.22% used; 112476352 free inodes.

server1 `/home`: 318671085568 available bytes; 82.22% used; 112476352 free inodes.

server1 `/tmp`: 318671085568 available bytes; 82.22% used; 112476352 free inodes.

server1 `/var/tmp`: 318671085568 available bytes; 82.22% used; 112476352 free inodes.

server1 `/mnt/raid5`: 363779522560 available bytes; 98.33% used; 337542974 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23105302528 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23105302528 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23105302528 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23105302528 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 315848462336 available bytes; 97.82% used; 445067917 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84392497152 available bytes; 95.29% used; 114152611 free inodes.

server3 `/home`: 84392497152 available bytes; 95.29% used; 114152611 free inodes.

server3 `/data`: 132539473920 available bytes; 98.17% used; 225811097 free inodes.

server3 `/tmp`: 84392497152 available bytes; 95.29% used; 114152611 free inodes.

server3 `/var/tmp`: 84392497152 available bytes; 95.29% used; 114152611 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105617534976 available bytes; 94.11% used; 114349642 free inodes.

server4 `/home`: 105617534976 available bytes; 94.11% used; 114349642 free inodes.

server4 `/data`: 229863043072 available bytes; 96.82% used; 224932782 free inodes.

server4 `/tmp`: 105617534976 available bytes; 94.11% used; 114349642 free inodes.

server4 `/var/tmp`: 105617534976 available bytes; 94.11% used; 114349642 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
