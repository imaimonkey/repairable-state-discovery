# V2R cluster inventory

2026-09-26T01:43:35.634989+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318648946688 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318648946688 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318648946688 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318648946688 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 324820692992 available bytes; 98.51% used; 337546417 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939660288 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22939660288 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22939660288 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22939660288 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 289784115200 available bytes; 98.00% used; 445055441 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84338663424 available bytes; 95.29% used; 114152364 free inodes.

server3 `/home`: 84338663424 available bytes; 95.29% used; 114152364 free inodes.

server3 `/data`: 124798869504 available bytes; 98.28% used; 225817780 free inodes.

server3 `/tmp`: 84338663424 available bytes; 95.29% used; 114152364 free inodes.

server3 `/var/tmp`: 84338663424 available bytes; 95.29% used; 114152364 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105196576768 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196576768 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 131392000000 available bytes; 98.18% used; 224915855 free inodes.

server4 `/tmp`: 105196576768 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196576768 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
