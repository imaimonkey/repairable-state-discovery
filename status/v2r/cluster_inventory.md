# V2R cluster inventory

2026-09-25T21:25:22.358213+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318702686208 available bytes; 82.22% used; 112476333 free inodes.

server1 `/home`: 318702686208 available bytes; 82.22% used; 112476333 free inodes.

server1 `/tmp`: 318702686208 available bytes; 82.22% used; 112476333 free inodes.

server1 `/var/tmp`: 318702686208 available bytes; 82.22% used; 112476333 free inodes.

server1 `/mnt/raid5`: 347444273152 available bytes; 98.41% used; 337539342 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22906548224 available bytes; 98.72% used; 110405690 free inodes.

server2 `/home`: 22906548224 available bytes; 98.72% used; 110405690 free inodes.

server2 `/tmp`: 22906548224 available bytes; 98.72% used; 110405690 free inodes.

server2 `/var/tmp`: 22906548224 available bytes; 98.72% used; 110405690 free inodes.

server2 `/mnt/raid5`: 301417000960 available bytes; 97.92% used; 445055286 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84363870208 available bytes; 95.29% used; 114152618 free inodes.

server3 `/home`: 84363870208 available bytes; 95.29% used; 114152618 free inodes.

server3 `/data`: 125900992512 available bytes; 98.26% used; 225807081 free inodes.

server3 `/tmp`: 84363870208 available bytes; 95.29% used; 114152618 free inodes.

server3 `/var/tmp`: 84363870208 available bytes; 95.29% used; 114152618 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389162496 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389162496 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217451220992 available bytes; 96.99% used; 224920133 free inodes.

server4 `/tmp`: 105389162496 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389162496 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
