# V2R cluster inventory

2026-09-24T02:15:48.799420+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325414141952 available bytes; 81.85% used; 112499057 free inodes.

server1 `/home`: 325414141952 available bytes; 81.85% used; 112499057 free inodes.

server1 `/tmp`: 325414141952 available bytes; 81.85% used; 112499057 free inodes.

server1 `/var/tmp`: 325414141952 available bytes; 81.85% used; 112499057 free inodes.

server1 `/mnt/raid5`: 708350701568 available bytes; 96.75% used; 337733458 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40905744384 available bytes; 97.72% used; 110431646 free inodes.

server2 `/home`: 40905744384 available bytes; 97.72% used; 110431646 free inodes.

server2 `/tmp`: 40905744384 available bytes; 97.72% used; 110431646 free inodes.

server2 `/var/tmp`: 40905744384 available bytes; 97.72% used; 110431646 free inodes.

server2 `/mnt/raid5`: 529452544000 available bytes; 96.34% used; 445199940 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292668092416 available bytes; 83.67% used; 114210517 free inodes.

server3 `/home`: 292668092416 available bytes; 83.67% used; 114210517 free inodes.

server3 `/data`: 18076069888 available bytes; 99.75% used; 225841228 free inodes.

server3 `/tmp`: 292668092416 available bytes; 83.67% used; 114210517 free inodes.

server3 `/var/tmp`: 292668092416 available bytes; 83.67% used; 114210517 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105932230656 available bytes; 94.09% used; 114348264 free inodes.

server4 `/home`: 105932230656 available bytes; 94.09% used; 114348264 free inodes.

server4 `/data`: 289747210240 available bytes; 96.00% used; 225388160 free inodes.

server4 `/tmp`: 105932230656 available bytes; 94.09% used; 114348264 free inodes.

server4 `/var/tmp`: 105932230656 available bytes; 94.09% used; 114348264 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
