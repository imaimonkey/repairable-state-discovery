# V2R cluster inventory

2026-09-25T07:41:22.858817+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318863204352 available bytes; 82.21% used; 112480363 free inodes.

server1 `/home`: 318863204352 available bytes; 82.21% used; 112480363 free inodes.

server1 `/tmp`: 318863204352 available bytes; 82.21% used; 112480363 free inodes.

server1 `/var/tmp`: 318863204352 available bytes; 82.21% used; 112480363 free inodes.

server1 `/mnt/raid5`: 399606628352 available bytes; 98.17% used; 337558313 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22852571136 available bytes; 98.73% used; 110410515 free inodes.

server2 `/home`: 22852571136 available bytes; 98.73% used; 110410515 free inodes.

server2 `/tmp`: 22852571136 available bytes; 98.73% used; 110410515 free inodes.

server2 `/var/tmp`: 22852571136 available bytes; 98.73% used; 110410515 free inodes.

server2 `/mnt/raid5`: 334790090752 available bytes; 97.69% used; 445096256 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436848640 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84436848640 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142392729600 available bytes; 98.03% used; 225812527 free inodes.

server3 `/tmp`: 84436848640 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84436848640 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637494784 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637494784 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249062723584 available bytes; 96.56% used; 225012615 free inodes.

server4 `/tmp`: 105637494784 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637494784 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
