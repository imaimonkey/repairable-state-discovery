# V2R cluster inventory

2026-09-24T00:24:45.835288+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325552214016 available bytes; 81.84% used; 112500645 free inodes.

server1 `/home`: 325552214016 available bytes; 81.84% used; 112500645 free inodes.

server1 `/tmp`: 325552214016 available bytes; 81.84% used; 112500645 free inodes.

server1 `/var/tmp`: 325552214016 available bytes; 81.84% used; 112500645 free inodes.

server1 `/mnt/raid5`: 1166051012608 available bytes; 94.65% used; 337735199 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40998531072 available bytes; 97.71% used; 110432358 free inodes.

server2 `/home`: 40998531072 available bytes; 97.71% used; 110432358 free inodes.

server2 `/tmp`: 40998531072 available bytes; 97.71% used; 110432358 free inodes.

server2 `/var/tmp`: 40998531072 available bytes; 97.71% used; 110432358 free inodes.

server2 `/mnt/raid5`: 532952555520 available bytes; 96.32% used; 445203508 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292636479488 available bytes; 83.67% used; 114209079 free inodes.

server3 `/home`: 292636479488 available bytes; 83.67% used; 114209079 free inodes.

server3 `/data`: 82247172096 available bytes; 98.86% used; 225844315 free inodes.

server3 `/tmp`: 292636479488 available bytes; 83.67% used; 114209079 free inodes.

server3 `/var/tmp`: 292636479488 available bytes; 83.67% used; 114209079 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106088964096 available bytes; 94.08% used; 114350487 free inodes.

server4 `/home`: 106088964096 available bytes; 94.08% used; 114350487 free inodes.

server4 `/data`: 292913369088 available bytes; 95.95% used; 225414569 free inodes.

server4 `/tmp`: 106088964096 available bytes; 94.08% used; 114350487 free inodes.

server4 `/var/tmp`: 106088964096 available bytes; 94.08% used; 114350487 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
