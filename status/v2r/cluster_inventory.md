# V2R cluster inventory

2026-09-24T09:30:48.766731+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324458106880 available bytes; 81.90% used; 112489854 free inodes.

server1 `/home`: 324458106880 available bytes; 81.90% used; 112489854 free inodes.

server1 `/tmp`: 324458106880 available bytes; 81.90% used; 112489854 free inodes.

server1 `/var/tmp`: 324458106880 available bytes; 81.90% used; 112489854 free inodes.

server1 `/mnt/raid5`: 502497464320 available bytes; 97.69% used; 337713289 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57768194048 available bytes; 96.78% used; 110430807 free inodes.

server2 `/home`: 57768194048 available bytes; 96.78% used; 110430807 free inodes.

server2 `/tmp`: 57768194048 available bytes; 96.78% used; 110430807 free inodes.

server2 `/var/tmp`: 57768194048 available bytes; 96.78% used; 110430807 free inodes.

server2 `/mnt/raid5`: 514577125376 available bytes; 96.44% used; 445177526 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85437394944 available bytes; 95.23% used; 114174531 free inodes.

server3 `/home`: 85437394944 available bytes; 95.23% used; 114174531 free inodes.

server3 `/data`: 165802209280 available bytes; 97.71% used; 225820858 free inodes.

server3 `/tmp`: 85437394944 available bytes; 95.23% used; 114174531 free inodes.

server3 `/var/tmp`: 85437394944 available bytes; 95.23% used; 114174531 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757716480 available bytes; 94.10% used; 114349047 free inodes.

server4 `/home`: 105757716480 available bytes; 94.10% used; 114349047 free inodes.

server4 `/data`: 154587299840 available bytes; 97.86% used; 225273271 free inodes.

server4 `/tmp`: 105757716480 available bytes; 94.10% used; 114349047 free inodes.

server4 `/var/tmp`: 105757716480 available bytes; 94.10% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
