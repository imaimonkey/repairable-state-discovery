# V2R cluster inventory

2026-09-25T04:11:57.870302+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318930808832 available bytes; 82.21% used; 112480382 free inodes.

server1 `/home`: 318930808832 available bytes; 82.21% used; 112480382 free inodes.

server1 `/tmp`: 318930808832 available bytes; 82.21% used; 112480382 free inodes.

server1 `/var/tmp`: 318930808832 available bytes; 82.21% used; 112480382 free inodes.

server1 `/mnt/raid5`: 374376239104 available bytes; 98.28% used; 337593906 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22965325824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22965325824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22965325824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22965325824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463594987520 available bytes; 96.80% used; 445110480 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340891648 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84340891648 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143895752704 available bytes; 98.01% used; 225816529 free inodes.

server3 `/tmp`: 84340891648 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84340891648 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674125312 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105674125312 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 33694035968 available bytes; 99.53% used; 224963947 free inodes.

server4 `/tmp`: 105674125312 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105674125312 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
