# V2R cluster inventory

2026-09-24T20:40:26.409892+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323981000704 available bytes; 81.93% used; 112481433 free inodes.

server1 `/home`: 323981000704 available bytes; 81.93% used; 112481433 free inodes.

server1 `/tmp`: 323981000704 available bytes; 81.93% used; 112481433 free inodes.

server1 `/var/tmp`: 323981000704 available bytes; 81.93% used; 112481433 free inodes.

server1 `/mnt/raid5`: 415609823232 available bytes; 98.09% used; 337633258 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30152663040 available bytes; 98.32% used; 110411382 free inodes.

server2 `/home`: 30152663040 available bytes; 98.32% used; 110411382 free inodes.

server2 `/tmp`: 30152663040 available bytes; 98.32% used; 110411382 free inodes.

server2 `/var/tmp`: 30152663040 available bytes; 98.32% used; 110411382 free inodes.

server2 `/mnt/raid5`: 491945095168 available bytes; 96.60% used; 445156657 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84395888640 available bytes; 95.29% used; 114156102 free inodes.

server3 `/home`: 84395888640 available bytes; 95.29% used; 114156102 free inodes.

server3 `/data`: 151288250368 available bytes; 97.91% used; 225804164 free inodes.

server3 `/tmp`: 84395888640 available bytes; 95.29% used; 114156102 free inodes.

server3 `/var/tmp`: 84395888640 available bytes; 95.29% used; 114156102 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639870464 available bytes; 94.10% used; 114348379 free inodes.

server4 `/home`: 105639870464 available bytes; 94.10% used; 114348379 free inodes.

server4 `/data`: 84175822848 available bytes; 98.84% used; 225257150 free inodes.

server4 `/tmp`: 105639870464 available bytes; 94.10% used; 114348379 free inodes.

server4 `/var/tmp`: 105639870464 available bytes; 94.10% used; 114348379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
