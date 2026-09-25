# V2R cluster inventory

2026-09-25T18:04:57.532062+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318762225664 available bytes; 82.22% used; 112476342 free inodes.

server1 `/home`: 318762225664 available bytes; 82.22% used; 112476342 free inodes.

server1 `/tmp`: 318762225664 available bytes; 82.22% used; 112476342 free inodes.

server1 `/var/tmp`: 318762225664 available bytes; 82.22% used; 112476342 free inodes.

server1 `/mnt/raid5`: 371225096192 available bytes; 98.30% used; 337542400 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23105531904 available bytes; 98.71% used; 110407932 free inodes.

server2 `/home`: 23105531904 available bytes; 98.71% used; 110407932 free inodes.

server2 `/tmp`: 23105531904 available bytes; 98.71% used; 110407932 free inodes.

server2 `/var/tmp`: 23105531904 available bytes; 98.71% used; 110407932 free inodes.

server2 `/mnt/raid5`: 314718146560 available bytes; 97.83% used; 445067461 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84392333312 available bytes; 95.29% used; 114152615 free inodes.

server3 `/home`: 84392333312 available bytes; 95.29% used; 114152615 free inodes.

server3 `/data`: 131474595840 available bytes; 98.18% used; 225810393 free inodes.

server3 `/tmp`: 84392333312 available bytes; 95.29% used; 114152615 free inodes.

server3 `/var/tmp`: 84392333312 available bytes; 95.29% used; 114152615 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105616568320 available bytes; 94.11% used; 114349604 free inodes.

server4 `/home`: 105616568320 available bytes; 94.11% used; 114349604 free inodes.

server4 `/data`: 229742710784 available bytes; 96.82% used; 224932358 free inodes.

server4 `/tmp`: 105616568320 available bytes; 94.11% used; 114349604 free inodes.

server4 `/var/tmp`: 105616568320 available bytes; 94.11% used; 114349604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
