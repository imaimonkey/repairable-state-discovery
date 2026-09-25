# V2R cluster inventory

2026-09-25T20:50:13.490752+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318699769856 available bytes; 82.22% used; 112476298 free inodes.

server1 `/home`: 318699769856 available bytes; 82.22% used; 112476298 free inodes.

server1 `/tmp`: 318699769856 available bytes; 82.22% used; 112476298 free inodes.

server1 `/var/tmp`: 318699769856 available bytes; 82.22% used; 112476298 free inodes.

server1 `/mnt/raid5`: 368635379712 available bytes; 98.31% used; 337539565 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22896570368 available bytes; 98.72% used; 110405687 free inodes.

server2 `/home`: 22896570368 available bytes; 98.72% used; 110405687 free inodes.

server2 `/tmp`: 22896570368 available bytes; 98.72% used; 110405687 free inodes.

server2 `/var/tmp`: 22896570368 available bytes; 98.72% used; 110405687 free inodes.

server2 `/mnt/raid5`: 302710370304 available bytes; 97.91% used; 445056621 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84371640320 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84371640320 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127100723200 available bytes; 98.24% used; 225807711 free inodes.

server3 `/tmp`: 84371640320 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84371640320 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655443456 available bytes; 94.10% used; 114349534 free inodes.

server4 `/home`: 105655443456 available bytes; 94.10% used; 114349534 free inodes.

server4 `/data`: 228026482688 available bytes; 96.85% used; 224926783 free inodes.

server4 `/tmp`: 105655443456 available bytes; 94.10% used; 114349534 free inodes.

server4 `/var/tmp`: 105655443456 available bytes; 94.10% used; 114349534 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
