# V2R cluster inventory

2026-09-25T21:22:18.822788+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318703288320 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318703288320 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318703288320 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318703288320 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 347679612928 available bytes; 98.41% used; 337539363 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22895460352 available bytes; 98.72% used; 110405690 free inodes.

server2 `/home`: 22895460352 available bytes; 98.72% used; 110405690 free inodes.

server2 `/tmp`: 22895460352 available bytes; 98.72% used; 110405690 free inodes.

server2 `/var/tmp`: 22895460352 available bytes; 98.72% used; 110405690 free inodes.

server2 `/mnt/raid5`: 301777682432 available bytes; 97.91% used; 445055267 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366381056 available bytes; 95.29% used; 114152626 free inodes.

server3 `/home`: 84366381056 available bytes; 95.29% used; 114152626 free inodes.

server3 `/data`: 125901946880 available bytes; 98.26% used; 225807134 free inodes.

server3 `/tmp`: 84366381056 available bytes; 95.29% used; 114152626 free inodes.

server3 `/var/tmp`: 84366381056 available bytes; 95.29% used; 114152626 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389252608 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389252608 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217851564032 available bytes; 96.99% used; 224920380 free inodes.

server4 `/tmp`: 105389252608 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389252608 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
