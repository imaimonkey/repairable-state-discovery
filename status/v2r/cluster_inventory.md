# V2R cluster inventory

2026-09-26T12:48:27.317927+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318161842176 available bytes; 82.25% used; 112474505 free inodes.

server1 `/home`: 318161842176 available bytes; 82.25% used; 112474505 free inodes.

server1 `/tmp`: 318161842176 available bytes; 82.25% used; 112474505 free inodes.

server1 `/var/tmp`: 318161842176 available bytes; 82.25% used; 112474505 free inodes.

server1 `/mnt/raid5`: 679643262976 available bytes; 96.88% used; 337537754 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 19731443712 available bytes; 98.90% used; 110381951 free inodes.

server2 `/home`: 19731443712 available bytes; 98.90% used; 110381951 free inodes.

server2 `/tmp`: 19731443712 available bytes; 98.90% used; 110381951 free inodes.

server2 `/var/tmp`: 19731443712 available bytes; 98.90% used; 110381951 free inodes.

server2 `/mnt/raid5`: 637919240192 available bytes; 95.59% used; 444977997 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82648199168 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82648199168 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 1347685736448 available bytes; 81.37% used; 225823509 free inodes.

server3 `/tmp`: 82648199168 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82648199168 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899343872 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899343872 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 413687087104 available bytes; 94.28% used; 224847497 free inodes.

server4 `/tmp`: 105899343872 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899343872 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
