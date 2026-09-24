# V2R cluster inventory

2026-09-24T00:37:07.878374+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325544898560 available bytes; 81.84% used; 112500517 free inodes.

server1 `/home`: 325544898560 available bytes; 81.84% used; 112500517 free inodes.

server1 `/tmp`: 325544898560 available bytes; 81.84% used; 112500517 free inodes.

server1 `/var/tmp`: 325544898560 available bytes; 81.84% used; 112500517 free inodes.

server1 `/mnt/raid5`: 1114461097984 available bytes; 94.89% used; 337735055 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40992980992 available bytes; 97.71% used; 110432316 free inodes.

server2 `/home`: 40992980992 available bytes; 97.71% used; 110432316 free inodes.

server2 `/tmp`: 40992980992 available bytes; 97.71% used; 110432316 free inodes.

server2 `/var/tmp`: 40992980992 available bytes; 97.71% used; 110432316 free inodes.

server2 `/mnt/raid5`: 532559777792 available bytes; 96.32% used; 445203212 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292522053632 available bytes; 83.68% used; 114206121 free inodes.

server3 `/home`: 292522053632 available bytes; 83.68% used; 114206121 free inodes.

server3 `/data`: 82237505536 available bytes; 98.86% used; 225844102 free inodes.

server3 `/tmp`: 292522053632 available bytes; 83.68% used; 114206121 free inodes.

server3 `/var/tmp`: 292522053632 available bytes; 83.68% used; 114206121 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106067718144 available bytes; 94.08% used; 114350154 free inodes.

server4 `/home`: 106067718144 available bytes; 94.08% used; 114350154 free inodes.

server4 `/data`: 292921839616 available bytes; 95.95% used; 225414583 free inodes.

server4 `/tmp`: 106067718144 available bytes; 94.08% used; 114350154 free inodes.

server4 `/var/tmp`: 106067718144 available bytes; 94.08% used; 114350154 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
