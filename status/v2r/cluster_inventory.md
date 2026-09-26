# V2R cluster inventory

2026-09-26T06:34:37.640180+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318769217536 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318769217536 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318769217536 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318769217536 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 219666063360 available bytes; 98.99% used; 337539764 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22313885696 available bytes; 98.76% used; 110403833 free inodes.

server2 `/home`: 22313885696 available bytes; 98.76% used; 110403833 free inodes.

server2 `/tmp`: 22313885696 available bytes; 98.76% used; 110403833 free inodes.

server2 `/var/tmp`: 22313885696 available bytes; 98.76% used; 110403833 free inodes.

server2 `/mnt/raid5`: 272880971776 available bytes; 98.11% used; 445028326 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82564440064 available bytes; 95.39% used; 114110888 free inodes.

server3 `/home`: 82564440064 available bytes; 95.39% used; 114110888 free inodes.

server3 `/data`: 123996213248 available bytes; 98.29% used; 225822222 free inodes.

server3 `/tmp`: 82564440064 available bytes; 95.39% used; 114110888 free inodes.

server3 `/var/tmp`: 82564440064 available bytes; 95.39% used; 114110888 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105905639424 available bytes; 94.09% used; 114346888 free inodes.

server4 `/home`: 105905639424 available bytes; 94.09% used; 114346888 free inodes.

server4 `/data`: 106041741312 available bytes; 98.53% used; 224923348 free inodes.

server4 `/tmp`: 105905639424 available bytes; 94.09% used; 114346888 free inodes.

server4 `/var/tmp`: 105905639424 available bytes; 94.09% used; 114346888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
