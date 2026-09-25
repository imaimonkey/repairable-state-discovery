# V2R cluster inventory

2026-09-25T01:22:40.862315+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319079358464 available bytes; 82.20% used; 112480772 free inodes.

server1 `/home`: 319079358464 available bytes; 82.20% used; 112480772 free inodes.

server1 `/tmp`: 319079358464 available bytes; 82.20% used; 112480772 free inodes.

server1 `/var/tmp`: 319079358464 available bytes; 82.20% used; 112480772 free inodes.

server1 `/mnt/raid5`: 416501731328 available bytes; 98.09% used; 337613815 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23058374656 available bytes; 98.71% used; 110410774 free inodes.

server2 `/home`: 23058374656 available bytes; 98.71% used; 110410774 free inodes.

server2 `/tmp`: 23058374656 available bytes; 98.71% used; 110410774 free inodes.

server2 `/var/tmp`: 23058374656 available bytes; 98.71% used; 110410774 free inodes.

server2 `/mnt/raid5`: 491354411008 available bytes; 96.60% used; 445161745 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84359684096 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84359684096 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 146814779392 available bytes; 97.97% used; 225812442 free inodes.

server3 `/tmp`: 84359684096 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84359684096 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779085312 available bytes; 94.10% used; 114348292 free inodes.

server4 `/home`: 105779085312 available bytes; 94.10% used; 114348292 free inodes.

server4 `/data`: 53315817472 available bytes; 99.26% used; 225030705 free inodes.

server4 `/tmp`: 105779085312 available bytes; 94.10% used; 114348292 free inodes.

server4 `/var/tmp`: 105779085312 available bytes; 94.10% used; 114348292 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
