# V2R cluster inventory

2026-09-26T00:47:04.491014+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318649675776 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318649675776 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318649675776 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318649675776 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 345591750656 available bytes; 98.41% used; 337546751 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22933164032 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22933164032 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22933164032 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22933164032 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 294605144064 available bytes; 97.96% used; 445057404 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341772288 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84341772288 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124939763712 available bytes; 98.27% used; 225818762 free inodes.

server3 `/tmp`: 84341772288 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84341772288 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105349308416 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349308416 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148676943872 available bytes; 97.95% used; 224917382 free inodes.

server4 `/tmp`: 105349308416 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349308416 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
