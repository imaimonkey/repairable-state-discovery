# V2R cluster inventory

2026-09-26T00:45:32.923067+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318650056704 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318650056704 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318650056704 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318650056704 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 345601544192 available bytes; 98.41% used; 337546767 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22933553152 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22933553152 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22933553152 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22933553152 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 294649749504 available bytes; 97.96% used; 445057573 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342202368 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84342202368 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124941189120 available bytes; 98.27% used; 225818777 free inodes.

server3 `/tmp`: 84342202368 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84342202368 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105349353472 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349353472 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148673466368 available bytes; 97.95% used; 224917383 free inodes.

server4 `/tmp`: 105349353472 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349353472 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
