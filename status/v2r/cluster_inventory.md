# V2R cluster inventory

2026-09-25T21:13:08.569319+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698917888 available bytes; 82.22% used; 112476306 free inodes.

server1 `/home`: 318698917888 available bytes; 82.22% used; 112476306 free inodes.

server1 `/tmp`: 318698917888 available bytes; 82.22% used; 112476306 free inodes.

server1 `/var/tmp`: 318698917888 available bytes; 82.22% used; 112476306 free inodes.

server1 `/mnt/raid5`: 368458313728 available bytes; 98.31% used; 337539420 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22889541632 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22889541632 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22889541632 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22889541632 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 302037291008 available bytes; 97.91% used; 445055652 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84368650240 available bytes; 95.29% used; 114152632 free inodes.

server3 `/home`: 84368650240 available bytes; 95.29% used; 114152632 free inodes.

server3 `/data`: 125905125376 available bytes; 98.26% used; 225807272 free inodes.

server3 `/tmp`: 84368650240 available bytes; 95.29% used; 114152632 free inodes.

server3 `/var/tmp`: 84368650240 available bytes; 95.29% used; 114152632 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389568000 available bytes; 94.12% used; 114347333 free inodes.

server4 `/home`: 105389568000 available bytes; 94.12% used; 114347333 free inodes.

server4 `/data`: 217867554816 available bytes; 96.99% used; 224920501 free inodes.

server4 `/tmp`: 105389568000 available bytes; 94.12% used; 114347333 free inodes.

server4 `/var/tmp`: 105389568000 available bytes; 94.12% used; 114347333 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
