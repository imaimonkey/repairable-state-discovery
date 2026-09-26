# V2R cluster inventory

2026-09-26T01:31:22.369734+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318649118720 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318649118720 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318649118720 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318649118720 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 345497088000 available bytes; 98.42% used; 337546547 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22929190912 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22929190912 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22929190912 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22929190912 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290669989888 available bytes; 97.99% used; 445055812 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84335923200 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84335923200 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124870184960 available bytes; 98.27% used; 225818020 free inodes.

server3 `/tmp`: 84335923200 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84335923200 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105196941312 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196941312 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 134785900544 available bytes; 98.14% used; 224917281 free inodes.

server4 `/tmp`: 105196941312 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196941312 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
