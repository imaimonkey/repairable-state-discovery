# V2R cluster inventory

2026-09-24T08:37:42.175495+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324395577344 available bytes; 81.90% used; 112490388 free inodes.

server1 `/home`: 324395577344 available bytes; 81.90% used; 112490388 free inodes.

server1 `/tmp`: 324395577344 available bytes; 81.90% used; 112490388 free inodes.

server1 `/var/tmp`: 324395577344 available bytes; 81.90% used; 112490388 free inodes.

server1 `/mnt/raid5`: 507465179136 available bytes; 97.67% used; 337719738 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57800048640 available bytes; 96.78% used; 110430976 free inodes.

server2 `/home`: 57800048640 available bytes; 96.78% used; 110430976 free inodes.

server2 `/tmp`: 57800048640 available bytes; 96.78% used; 110430976 free inodes.

server2 `/var/tmp`: 57800048640 available bytes; 96.78% used; 110430976 free inodes.

server2 `/mnt/raid5`: 515391393792 available bytes; 96.44% used; 445179391 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.

server3 `/home`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.

server3 `/data`: 173700870144 available bytes; 97.60% used; 225822743 free inodes.

server3 `/tmp`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.

server3 `/var/tmp`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105768837120 available bytes; 94.10% used; 114349093 free inodes.

server4 `/home`: 105768837120 available bytes; 94.10% used; 114349093 free inodes.

server4 `/data`: 255368953856 available bytes; 96.47% used; 225288378 free inodes.

server4 `/tmp`: 105768837120 available bytes; 94.10% used; 114349093 free inodes.

server4 `/var/tmp`: 105768837120 available bytes; 94.10% used; 114349093 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
