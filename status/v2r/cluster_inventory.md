# V2R cluster inventory

2026-09-24T01:46:11.892971+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325454761984 available bytes; 81.84% used; 112499459 free inodes.

server1 `/home`: 325454761984 available bytes; 81.84% used; 112499459 free inodes.

server1 `/tmp`: 325454761984 available bytes; 81.84% used; 112499459 free inodes.

server1 `/var/tmp`: 325454761984 available bytes; 81.84% used; 112499459 free inodes.

server1 `/mnt/raid5`: 830147903488 available bytes; 96.19% used; 337733806 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40932982784 available bytes; 97.72% used; 110431867 free inodes.

server2 `/home`: 40932982784 available bytes; 97.72% used; 110431867 free inodes.

server2 `/tmp`: 40932982784 available bytes; 97.72% used; 110431867 free inodes.

server2 `/var/tmp`: 40932982784 available bytes; 97.72% used; 110431867 free inodes.

server2 `/mnt/raid5`: 530296815616 available bytes; 96.34% used; 445200852 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292675903488 available bytes; 83.67% used; 114210490 free inodes.

server3 `/home`: 292675903488 available bytes; 83.67% used; 114210490 free inodes.

server3 `/data`: 71394304000 available bytes; 99.01% used; 225841964 free inodes.

server3 `/tmp`: 292675903488 available bytes; 83.67% used; 114210490 free inodes.

server3 `/var/tmp`: 292675903488 available bytes; 83.67% used; 114210490 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105952169984 available bytes; 94.09% used; 114348588 free inodes.

server4 `/home`: 105952169984 available bytes; 94.09% used; 114348588 free inodes.

server4 `/data`: 289766981632 available bytes; 96.00% used; 225388487 free inodes.

server4 `/tmp`: 105952169984 available bytes; 94.09% used; 114348588 free inodes.

server4 `/var/tmp`: 105952169984 available bytes; 94.09% used; 114348588 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
