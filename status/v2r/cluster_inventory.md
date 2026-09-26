# V2R cluster inventory

2026-09-26T02:54:44.913908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417600512 available bytes; 82.24% used; 112476263 free inodes.

server1 `/home`: 318417600512 available bytes; 82.24% used; 112476263 free inodes.

server1 `/tmp`: 318417600512 available bytes; 82.24% used; 112476263 free inodes.

server1 `/var/tmp`: 318417600512 available bytes; 82.24% used; 112476263 free inodes.

server1 `/mnt/raid5`: 331099328512 available bytes; 98.48% used; 337545990 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22935535616 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22935535616 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22935535616 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22935535616 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 288276340736 available bytes; 98.01% used; 445053760 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84310413312 available bytes; 95.30% used; 114152367 free inodes.

server3 `/home`: 84310413312 available bytes; 95.30% used; 114152367 free inodes.

server3 `/data`: 125447630848 available bytes; 98.27% used; 225831288 free inodes.

server3 `/tmp`: 84310413312 available bytes; 95.30% used; 114152367 free inodes.

server3 `/var/tmp`: 84310413312 available bytes; 95.30% used; 114152367 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105919016960 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105919016960 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109769089024 available bytes; 98.48% used; 224915384 free inodes.

server4 `/tmp`: 105919016960 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105919016960 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
