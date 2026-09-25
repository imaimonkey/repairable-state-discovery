# V2R cluster inventory

2026-09-25T12:46:53.138900+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/home`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/tmp`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/var/tmp`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/mnt/raid5`: 364248698880 available bytes; 98.33% used; 337548047 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 20264247296 available bytes; 98.87% used; 110409427 free inodes.

server2 `/home`: 20264247296 available bytes; 98.87% used; 110409427 free inodes.

server2 `/tmp`: 20264247296 available bytes; 98.87% used; 110409427 free inodes.

server2 `/var/tmp`: 20264247296 available bytes; 98.87% used; 110409427 free inodes.

server2 `/mnt/raid5`: 324645019648 available bytes; 97.76% used; 445078998 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84208050176 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84208050176 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142274781184 available bytes; 98.03% used; 225810930 free inodes.

server3 `/tmp`: 84208050176 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84208050176 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665589248 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665589248 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232020541440 available bytes; 96.79% used; 224961817 free inodes.

server4 `/tmp`: 105665589248 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665589248 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
