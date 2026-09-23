# V2R cluster inventory

2026-09-23T20:59:43.566348+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325724688384 available bytes; 81.83% used; 112501604 free inodes.

server1 `/home`: 325724688384 available bytes; 81.83% used; 112501604 free inodes.

server1 `/tmp`: 325724688384 available bytes; 81.83% used; 112501604 free inodes.

server1 `/var/tmp`: 325724688384 available bytes; 81.83% used; 112501604 free inodes.

server1 `/mnt/raid5`: 1388145905664 available bytes; 93.63% used; 337740014 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41124139008 available bytes; 97.71% used; 110432727 free inodes.

server2 `/home`: 41124139008 available bytes; 97.71% used; 110432727 free inodes.

server2 `/tmp`: 41124139008 available bytes; 97.71% used; 110432727 free inodes.

server2 `/var/tmp`: 41124139008 available bytes; 97.71% used; 110432727 free inodes.

server2 `/mnt/raid5`: 539457564672 available bytes; 96.27% used; 445209379 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293461225472 available bytes; 83.62% used; 114237013 free inodes.

server3 `/home`: 293461225472 available bytes; 83.62% used; 114237013 free inodes.

server3 `/data`: 52610035712 available bytes; 99.27% used; 225850475 free inodes.

server3 `/tmp`: 293461225472 available bytes; 83.62% used; 114237013 free inodes.

server3 `/var/tmp`: 293461225472 available bytes; 83.62% used; 114237013 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106500370432 available bytes; 94.06% used; 114356065 free inodes.

server4 `/home`: 106500370432 available bytes; 94.06% used; 114356065 free inodes.

server4 `/data`: 300579270656 available bytes; 95.85% used; 225457085 free inodes.

server4 `/tmp`: 106500370432 available bytes; 94.06% used; 114356065 free inodes.

server4 `/var/tmp`: 106500370432 available bytes; 94.06% used; 114356065 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
