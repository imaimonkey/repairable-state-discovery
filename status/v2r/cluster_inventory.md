# V2R cluster inventory

2026-09-25T19:09:19.781664+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318733225984 available bytes; 82.22% used; 112476328 free inodes.

server1 `/home`: 318733225984 available bytes; 82.22% used; 112476328 free inodes.

server1 `/tmp`: 318733225984 available bytes; 82.22% used; 112476328 free inodes.

server1 `/var/tmp`: 318733225984 available bytes; 82.22% used; 112476328 free inodes.

server1 `/mnt/raid5`: 371002843136 available bytes; 98.30% used; 337540909 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23103000576 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23103000576 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23103000576 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23103000576 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 312675569664 available bytes; 97.84% used; 445065314 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84383440896 available bytes; 95.29% used; 114152631 free inodes.

server3 `/home`: 84383440896 available bytes; 95.29% used; 114152631 free inodes.

server3 `/data`: 130320900096 available bytes; 98.20% used; 225808942 free inodes.

server3 `/tmp`: 84383440896 available bytes; 95.29% used; 114152631 free inodes.

server3 `/var/tmp`: 84383440896 available bytes; 95.29% used; 114152631 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105675591680 available bytes; 94.10% used; 114349591 free inodes.

server4 `/home`: 105675591680 available bytes; 94.10% used; 114349591 free inodes.

server4 `/data`: 229642989568 available bytes; 96.83% used; 224931087 free inodes.

server4 `/tmp`: 105675591680 available bytes; 94.10% used; 114349591 free inodes.

server4 `/var/tmp`: 105675591680 available bytes; 94.10% used; 114349591 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
