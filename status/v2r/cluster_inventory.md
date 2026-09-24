# V2R cluster inventory

2026-09-24T16:51:43.958673+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324023799808 available bytes; 81.92% used; 112481444 free inodes.

server1 `/home`: 324023799808 available bytes; 81.92% used; 112481444 free inodes.

server1 `/tmp`: 324023799808 available bytes; 81.92% used; 112481444 free inodes.

server1 `/var/tmp`: 324023799808 available bytes; 81.92% used; 112481444 free inodes.

server1 `/mnt/raid5`: 416524226560 available bytes; 98.09% used; 337650846 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57073680384 available bytes; 96.82% used; 110418111 free inodes.

server2 `/home`: 57073680384 available bytes; 96.82% used; 110418111 free inodes.

server2 `/tmp`: 57073680384 available bytes; 96.82% used; 110418111 free inodes.

server2 `/var/tmp`: 57073680384 available bytes; 96.82% used; 110418111 free inodes.

server2 `/mnt/raid5`: 500276121600 available bytes; 96.54% used; 445163756 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84417622016 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84417622016 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 159197503488 available bytes; 97.80% used; 225787558 free inodes.

server3 `/tmp`: 84417622016 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84417622016 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105682792448 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105682792448 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89195270144 available bytes; 98.77% used; 225255206 free inodes.

server4 `/tmp`: 105682792448 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105682792448 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
