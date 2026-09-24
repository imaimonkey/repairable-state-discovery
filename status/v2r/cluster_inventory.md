# V2R cluster inventory

2026-09-24T00:06:11.430064+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325576617984 available bytes; 81.84% used; 112500848 free inodes.

server1 `/home`: 325576617984 available bytes; 81.84% used; 112500848 free inodes.

server1 `/tmp`: 325576617984 available bytes; 81.84% used; 112500848 free inodes.

server1 `/var/tmp`: 325576617984 available bytes; 81.84% used; 112500848 free inodes.

server1 `/mnt/raid5`: 1241877544960 available bytes; 94.30% used; 337735356 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41009901568 available bytes; 97.71% used; 110432422 free inodes.

server2 `/home`: 41009901568 available bytes; 97.71% used; 110432422 free inodes.

server2 `/tmp`: 41009901568 available bytes; 97.71% used; 110432422 free inodes.

server2 `/var/tmp`: 41009901568 available bytes; 97.71% used; 110432422 free inodes.

server2 `/mnt/raid5`: 532885438464 available bytes; 96.32% used; 445204051 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292798136320 available bytes; 83.66% used; 114213757 free inodes.

server3 `/home`: 292798136320 available bytes; 83.66% used; 114213757 free inodes.

server3 `/data`: 82266337280 available bytes; 98.86% used; 225844679 free inodes.

server3 `/tmp`: 292798136320 available bytes; 83.66% used; 114213757 free inodes.

server3 `/var/tmp`: 292798136320 available bytes; 83.66% used; 114213757 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106125590528 available bytes; 94.08% used; 114351063 free inodes.

server4 `/home`: 106125590528 available bytes; 94.08% used; 114351063 free inodes.

server4 `/data`: 292920127488 available bytes; 95.95% used; 225414606 free inodes.

server4 `/tmp`: 106125590528 available bytes; 94.08% used; 114351063 free inodes.

server4 `/var/tmp`: 106125590528 available bytes; 94.08% used; 114351063 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
