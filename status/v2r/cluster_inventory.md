# V2R cluster inventory

2026-09-26T06:23:56.173024+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318770126848 available bytes; 82.22% used; 112476280 free inodes.

server1 `/home`: 318770126848 available bytes; 82.22% used; 112476280 free inodes.

server1 `/tmp`: 318770126848 available bytes; 82.22% used; 112476280 free inodes.

server1 `/var/tmp`: 318770126848 available bytes; 82.22% used; 112476280 free inodes.

server1 `/mnt/raid5`: 219698610176 available bytes; 98.99% used; 337539843 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22322249728 available bytes; 98.75% used; 110403851 free inodes.

server2 `/home`: 22322249728 available bytes; 98.75% used; 110403851 free inodes.

server2 `/tmp`: 22322249728 available bytes; 98.75% used; 110403851 free inodes.

server2 `/var/tmp`: 22322249728 available bytes; 98.75% used; 110403851 free inodes.

server2 `/mnt/raid5`: 273212567552 available bytes; 98.11% used; 445028896 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82565832704 available bytes; 95.39% used; 114110903 free inodes.

server3 `/home`: 82565832704 available bytes; 95.39% used; 114110903 free inodes.

server3 `/data`: 124000268288 available bytes; 98.29% used; 225822397 free inodes.

server3 `/tmp`: 82565832704 available bytes; 95.39% used; 114110903 free inodes.

server3 `/var/tmp`: 82565832704 available bytes; 95.39% used; 114110903 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105914355712 available bytes; 94.09% used; 114346888 free inodes.

server4 `/home`: 105914355712 available bytes; 94.09% used; 114346888 free inodes.

server4 `/data`: 106564816896 available bytes; 98.53% used; 224923521 free inodes.

server4 `/tmp`: 105914355712 available bytes; 94.09% used; 114346888 free inodes.

server4 `/var/tmp`: 105914355712 available bytes; 94.09% used; 114346888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
