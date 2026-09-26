# V2R cluster inventory

2026-09-26T05:42:41.975731+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318782550016 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318782550016 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318782550016 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318782550016 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 241754402816 available bytes; 98.89% used; 337540126 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22894514176 available bytes; 98.72% used; 110403896 free inodes.

server2 `/home`: 22894514176 available bytes; 98.72% used; 110403896 free inodes.

server2 `/tmp`: 22894514176 available bytes; 98.72% used; 110403896 free inodes.

server2 `/var/tmp`: 22894514176 available bytes; 98.72% used; 110403896 free inodes.

server2 `/mnt/raid5`: 275648507904 available bytes; 98.10% used; 445036839 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83208929280 available bytes; 95.36% used; 114149585 free inodes.

server3 `/home`: 83208929280 available bytes; 95.36% used; 114149585 free inodes.

server3 `/data`: 124336062464 available bytes; 98.28% used; 225824028 free inodes.

server3 `/tmp`: 83208929280 available bytes; 95.36% used; 114149585 free inodes.

server3 `/var/tmp`: 83208929280 available bytes; 95.36% used; 114149585 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094579712 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094579712 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106990567424 available bytes; 98.52% used; 224929134 free inodes.

server4 `/tmp`: 106094579712 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094579712 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
