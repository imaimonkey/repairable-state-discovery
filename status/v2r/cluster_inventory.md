# V2R cluster inventory

2026-09-25T21:23:50.622523+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318703149056 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318703149056 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318703149056 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318703149056 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 347444174848 available bytes; 98.41% used; 337539340 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22895185920 available bytes; 98.72% used; 110405690 free inodes.

server2 `/home`: 22895185920 available bytes; 98.72% used; 110405690 free inodes.

server2 `/tmp`: 22895185920 available bytes; 98.72% used; 110405690 free inodes.

server2 `/var/tmp`: 22895185920 available bytes; 98.72% used; 110405690 free inodes.

server2 `/mnt/raid5`: 301451128832 available bytes; 97.92% used; 445055195 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84365860864 available bytes; 95.29% used; 114152626 free inodes.

server3 `/home`: 84365860864 available bytes; 95.29% used; 114152626 free inodes.

server3 `/data`: 125904318464 available bytes; 98.26% used; 225807105 free inodes.

server3 `/tmp`: 84365860864 available bytes; 95.29% used; 114152626 free inodes.

server3 `/var/tmp`: 84365860864 available bytes; 95.29% used; 114152626 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389199360 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389199360 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217532899328 available bytes; 96.99% used; 224920198 free inodes.

server4 `/tmp`: 105389199360 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389199360 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
