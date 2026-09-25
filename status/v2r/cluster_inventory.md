# V2R cluster inventory

2026-09-25T03:04:15.707090+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318942298112 available bytes; 82.21% used; 112480395 free inodes.

server1 `/home`: 318942298112 available bytes; 82.21% used; 112480395 free inodes.

server1 `/tmp`: 318942298112 available bytes; 82.21% used; 112480395 free inodes.

server1 `/var/tmp`: 318942298112 available bytes; 82.21% used; 112480395 free inodes.

server1 `/mnt/raid5`: 416137805824 available bytes; 98.09% used; 337601939 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22996799488 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22996799488 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22996799488 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22996799488 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 465978544128 available bytes; 96.78% used; 445112714 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84344983552 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84344983552 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144952803328 available bytes; 98.00% used; 225810399 free inodes.

server3 `/tmp`: 84344983552 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84344983552 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105693130752 available bytes; 94.10% used; 114350903 free inodes.

server4 `/home`: 105693130752 available bytes; 94.10% used; 114350903 free inodes.

server4 `/data`: 50263154688 available bytes; 99.31% used; 224967442 free inodes.

server4 `/tmp`: 105693130752 available bytes; 94.10% used; 114350903 free inodes.

server4 `/var/tmp`: 105693130752 available bytes; 94.10% used; 114350903 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
