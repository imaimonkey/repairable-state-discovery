# V2R cluster inventory

2026-09-23T15:13:15.211158+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41440628736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41440628736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41440628736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41440628736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 550753656832 available bytes; 96.19% used; 445224523 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 377649643520 available bytes; 78.93% used; 114304993 free inodes.

server3 `/home`: 377649643520 available bytes; 78.93% used; 114304993 free inodes.

server3 `/data`: 124976717824 available bytes; 98.27% used; 225841116 free inodes.

server3 `/tmp`: 377649643520 available bytes; 78.93% used; 114304993 free inodes.

server3 `/var/tmp`: 377649643520 available bytes; 78.93% used; 114304993 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111673004032 available bytes; 93.77% used; 114378444 free inodes.

server4 `/home`: 111673004032 available bytes; 93.77% used; 114378444 free inodes.

server4 `/data`: 39027798016 available bytes; 99.46% used; 225495682 free inodes.

server4 `/tmp`: 111673004032 available bytes; 93.77% used; 114378444 free inodes.

server4 `/var/tmp`: 111673004032 available bytes; 93.77% used; 114378444 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
