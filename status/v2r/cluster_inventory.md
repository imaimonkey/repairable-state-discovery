# V2R cluster inventory

2026-09-25T20:59:23.693261+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318699466752 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318699466752 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318699466752 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318699466752 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 368620367872 available bytes; 98.31% used; 337539530 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22893846528 available bytes; 98.72% used; 110405678 free inodes.

server2 `/home`: 22893846528 available bytes; 98.72% used; 110405678 free inodes.

server2 `/tmp`: 22893846528 available bytes; 98.72% used; 110405678 free inodes.

server2 `/var/tmp`: 22893846528 available bytes; 98.72% used; 110405678 free inodes.

server2 `/mnt/raid5`: 302434344960 available bytes; 97.91% used; 445055801 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84362072064 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84362072064 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 126051819520 available bytes; 98.26% used; 225807548 free inodes.

server3 `/tmp`: 84362072064 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84362072064 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655099392 available bytes; 94.10% used; 114349517 free inodes.

server4 `/home`: 105655099392 available bytes; 94.10% used; 114349517 free inodes.

server4 `/data`: 226926395392 available bytes; 96.86% used; 224926217 free inodes.

server4 `/tmp`: 105655099392 available bytes; 94.10% used; 114349517 free inodes.

server4 `/var/tmp`: 105655099392 available bytes; 94.10% used; 114349517 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
