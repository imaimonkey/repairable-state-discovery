# V2R cluster inventory

2026-09-26T06:31:34.476774+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318770372608 available bytes; 82.22% used; 112476274 free inodes.

server1 `/home`: 318770372608 available bytes; 82.22% used; 112476274 free inodes.

server1 `/tmp`: 318770372608 available bytes; 82.22% used; 112476274 free inodes.

server1 `/var/tmp`: 318770372608 available bytes; 82.22% used; 112476274 free inodes.

server1 `/mnt/raid5`: 219675983872 available bytes; 98.99% used; 337539786 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22314844160 available bytes; 98.76% used; 110403832 free inodes.

server2 `/home`: 22314844160 available bytes; 98.76% used; 110403832 free inodes.

server2 `/tmp`: 22314844160 available bytes; 98.76% used; 110403832 free inodes.

server2 `/var/tmp`: 22314844160 available bytes; 98.76% used; 110403832 free inodes.

server2 `/mnt/raid5`: 272974888960 available bytes; 98.11% used; 445028541 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82565152768 available bytes; 95.39% used; 114110885 free inodes.

server3 `/home`: 82565152768 available bytes; 95.39% used; 114110885 free inodes.

server3 `/data`: 123994664960 available bytes; 98.29% used; 225822276 free inodes.

server3 `/tmp`: 82565152768 available bytes; 95.39% used; 114110885 free inodes.

server3 `/var/tmp`: 82565152768 available bytes; 95.39% used; 114110885 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105914109952 available bytes; 94.09% used; 114346888 free inodes.

server4 `/home`: 105914109952 available bytes; 94.09% used; 114346888 free inodes.

server4 `/data`: 106556743680 available bytes; 98.53% used; 224923434 free inodes.

server4 `/tmp`: 105914109952 available bytes; 94.09% used; 114346888 free inodes.

server4 `/var/tmp`: 105914109952 available bytes; 94.09% used; 114346888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
