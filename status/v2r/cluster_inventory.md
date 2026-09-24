# V2R cluster inventory

2026-09-24T15:12:19.181151+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324045799424 available bytes; 81.92% used; 112481465 free inodes.

server1 `/home`: 324045799424 available bytes; 81.92% used; 112481465 free inodes.

server1 `/tmp`: 324045799424 available bytes; 81.92% used; 112481465 free inodes.

server1 `/var/tmp`: 324045799424 available bytes; 81.92% used; 112481465 free inodes.

server1 `/mnt/raid5`: 416803037184 available bytes; 98.09% used; 337663278 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57410236416 available bytes; 96.80% used; 110427683 free inodes.

server2 `/home`: 57410236416 available bytes; 96.80% used; 110427683 free inodes.

server2 `/tmp`: 57410236416 available bytes; 96.80% used; 110427683 free inodes.

server2 `/var/tmp`: 57410236416 available bytes; 96.80% used; 110427683 free inodes.

server2 `/mnt/raid5`: 503213690880 available bytes; 96.52% used; 445166709 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84869443584 available bytes; 95.26% used; 114183221 free inodes.

server3 `/home`: 84869443584 available bytes; 95.26% used; 114183221 free inodes.

server3 `/data`: 160512839680 available bytes; 97.78% used; 225807322 free inodes.

server3 `/tmp`: 84869443584 available bytes; 95.26% used; 114183221 free inodes.

server3 `/var/tmp`: 84869443584 available bytes; 95.26% used; 114183221 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105717026816 available bytes; 94.10% used; 114348635 free inodes.

server4 `/home`: 105717026816 available bytes; 94.10% used; 114348635 free inodes.

server4 `/data`: 68791685120 available bytes; 99.05% used; 225256960 free inodes.

server4 `/tmp`: 105717026816 available bytes; 94.10% used; 114348635 free inodes.

server4 `/var/tmp`: 105717026816 available bytes; 94.10% used; 114348635 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
